# -*- coding: utf-8 -*-
import settings

PAYMENT_DONE = "PAYMENT_DONE"
CANCELED = "CANCELED"
TIMEOUTED = "TIMEOUTED"
WAITING = "WAITING"
FAILED = "FAILED"
CALL_COMPLETED = "CALL_COMPLETED"
UNKNOWN = "UNKNOWN"

PAYMENT_COMMAND = {
    'successURL': 'http://tolary.cz',
    'failedURL': 'http://tolary.cz',
    'productName': 'test',
    'eshopGoId': settings.ESHOP_GOID,
    'variableSymbol': '235',
    'totalPrice': 100,
    }