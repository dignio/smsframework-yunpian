from smsframework import IProvider, exc
from . import error

try: # Py3
    from urllib.request import URLError, HTTPError
except ImportError: # Py2
    from urllib2 import URLError, HTTPError


class YunpianProvider(IProvider):
    """ Yunpian provider """

    def __init__(self, gateway, name, **any_custom_provider_settings):
        """ Configure Yunpian provider
        """
        Custom code to configure provider
        super(YunpianProvider, self).__init__(gateway, name)

    def send(self, message):
        """ Send a message

            :type message: smsframework.data.OutgoingMessage.OutgoingMessage
            :rtype: OutgoingMessage
            """
        
        # Do not forget all possible exceptions
        try:
            message.msgid = Custom code to send SMS
            return message
        except AssertionError as e:
            raise exc.RequestError(str(e))
        except HTTPError as e:
            raise exc.MessageSendError(str(e))
        except URLError as e:
            raise exc.ConnectionError(str(e))
        except CustomErrror as e:
            raise error.YunpianProviderError(str(e))

    def make_receiver_blueprint(self):
        """ Create the receiver blueprint """
        raise NotImplementedError('Yunpian do not support incoming SMSes')
