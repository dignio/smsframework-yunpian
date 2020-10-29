|Build Status|

SMSframework Yunpian Provider
===============================================

Yunpian Provider for
[smsframework](https://pypi.python.org/pypi/smsframework/).

You need an account with "SMS Server" service set up. You'll need the
following configuration: apikey.

Also you should know, that not any SMS can be sent. But only SMS that match the template or have [Youcompany] signature.

Template can be set here - https://www.yunpian.com/console/#/admin

Example template is "[MyCompany] You secret code: #code#", where `#code#` is a variable.

Installation
============

Install from pypi:

    $ pip install smsframework_yunpian


Initialization
==============

    from smsframework import Gateway
    from smsframework_yunpian import YunpianProvider

    gateway = Gateway()
    gateway.add_provider('yunpian', YunpianProvider,
        apikey='secret_api_key'
    )

Config
------

Source: /smsframework_yunpian/provider.py

-  ``apikey``: Api key
-  ``signature``: Optional signature, if set it will be prepended to all SMS. Example: `"[MyCompany]"`

Sending Parameters
==================

Provider-specific sending params: None

Additional Information
======================

OutgoingMessage.meta
--------------------

Provider-specific sending params

IncomingMessage.meta
--------------------

Provider-specific income message fields.

MessageStatus.meta
------------------

Provider-specific message status fields.
