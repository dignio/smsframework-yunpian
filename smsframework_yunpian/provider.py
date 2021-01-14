from smsframework import IProvider, exc
from . import error
import re
from yunpian_python_sdk.model import constant as YC
from yunpian_python_sdk.ypclient import YunpianClient

try: # Py3
    from urllib.request import URLError, HTTPError
except ImportError: # Py2
    from urllib2 import URLError, HTTPError


class YunpianProvider(IProvider):
    """ Yunpian provider """

    def __init__(self, gateway, name, apikey, signature=None, auth_sms=None, reminder_sms=None):
        """ Configure Yunpian provider
        """
        self.api_client = YunpianClient(apikey)
        self.signature = signature
        if auth_sms == None:
            auth_sms = '您的验证码是 {code}'
        if reminder_sms == None:
            reminder_sms = '温馨提醒: 请在{time}前查看和遵循患者MD app 用药或测量任务提示'
        self.auth_sms = auth_sms
        self.reminder_sms = reminder_sms
        super(YunpianProvider, self).__init__(gateway, name)

    def send(self, message):
        """ Send a message

            :type message: smsframework.data.OutgoingMessage.OutgoingMessage
            :rtype: OutgoingMessage
            """
        
        # Do not forget all possible exceptions
        try:
            body = message.body
            if self.signature:
                body = self.signature + body
            if message.routing_values and len(message.routing_values) > 1:
                module = message.routing_values[1]
            else:
                module = None
            if module == 'auth.sms':
                body = self._auth_sms(body)
            if module == 'patient task list':
                body = self._reminder_sms(body)
            param = {YC.MOBILE: '+' + message.dst, YC.TEXT: body}
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

    def _auth_sms(self, body):
        reg = re.compile(r'\d+')
        try:
            code = reg.search(body)[0]
        except (IndexError, TypeError):
            code = ''
        return self.auth_sms.format(code=code)

    def _reminder_sms(self, body):
        reg = re.compile(r'(\d|:)+')
        try:
            time = reg.search(body)[0]
        except (IndexError, TypeError):
            time = ''
        return self.reminder_sms.format(time=time)

    def make_receiver_blueprint(self):
        """ Create the receiver blueprint """
        raise NotImplementedError('Yunpian do not support incoming SMSes')
