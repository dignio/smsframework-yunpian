from smsframework import IProvider, exc
from . import error
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient

try: # Py3
    from urllib.request import URLError, HTTPError
except ImportError: # Py2
    from urllib2 import URLError, HTTPError


class YunpianProvider(IProvider):
    """ Yunpian provider """

    def __init__(self, gateway, name, apikey):
        """ Configure Yunpian provider
        """
        self.api_client = YunpianClient(apikey)
        super(YunpianProvider, self).__init__(gateway, name)

    def send(self, message):
        """ Send a message

            :type message: smsframework.data.OutgoingMessage.OutgoingMessage
            :rtype: OutgoingMessage
            """
        
        # Do not forget all possible exceptions
        try:
            param = {YC.MOBILE: message.dst,YC.TEXT: message.body}
            r = self.api_client.sms().single_send(param)
            if not r.is_succ():
                msg = '{} {}'.format(r.code(), r.msg())
                if r.detail():
                    msg += r.detail()
                if r.exception():
                    msg += ' Exception: {}.'.format(r.exception())
                raise error.YunpianProviderError(msg)
            message.msgid = r.data().get('sid')
            return message
        except AssertionError as e:
            raise exc.RequestError(str(e))
        except HTTPError as e:
            raise exc.MessageSendError(str(e))
        except URLError as e:
            raise exc.ConnectionError(str(e))

    def make_receiver_blueprint(self):
        """ Create the receiver blueprint """
        raise NotImplementedError('Yunpian do not support incoming SMSes')
