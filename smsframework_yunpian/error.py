from smsframework.exc import *


class YunpianProviderError(ProviderError):
    """ Custom Yunpian errors """

    def __init__(self, message=''):
        Implement some custom errors or delete this stuff
        super(YunpianProviderError, self).__init__(message)
