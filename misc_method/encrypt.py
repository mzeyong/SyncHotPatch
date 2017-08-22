# coding= utf-8
# Author : k2yk

from crypt import _rc4
from crypt import _b64

class e_api:

    rc_f = _rc4.rc4()
    b64_f = _b64.b64()

    def rc4(self,data,key = None):
        if key:
            result = self.rc_f.rc4(data,key)
        else:
            result = self.rc_f.rc4(data)
        return result

    def eb64(self,data,chars = None):
        return self.b64_f.encode(data,chars)

    def db64(self,data,chars):
        return self.b64_f.decode(data,chars)