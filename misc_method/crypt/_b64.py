# coding= utf-8
# Author : k2yk

import base64

class b64:
    @staticmethod
    def encode(data,chars = None):
        if chars:
            result = base64.b64encode(data,chars)
        else:
            result = base64.b64encode(data)
        return result

    @staticmethod
    def decode(data,chars = None):
        if chars:
            result = base64.b64decode(data,chars)
        else:
            result = base64.b64decode(data)
        return result