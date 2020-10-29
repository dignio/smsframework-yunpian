from smsframework.exc import *


class YunpianProviderError(ProviderError):
    """ Custom Yunpian errors """

    def __init__(self, message=''):
        super(YunpianProviderError, self).__init__(message)
