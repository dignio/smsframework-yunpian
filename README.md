|Build Status|

SMSframework Yunpian Provider
===============================================

Yunpian Provider for
[smsframework](https://pypi.python.org/pypi/smsframework/).

You need an account with "SMS Server" service set up. You'll need the
following configuration: username, password.

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
