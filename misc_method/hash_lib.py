# coding=utf-8
# Author :k2yk

import hashlib

class h_api:

    md5 = hashlib.md5
    sha1 = hashlib.sha1
    sha256 = hashlib.sha256

    @staticmethod
    def hmd5(cbyte):
        if isinstance(cbyte,int):
            cbyte = str(cbyte)
        return h_api.md5(cbyte).hexdigest()

    @staticmethod
    def bmd5(cbyte):
        return h_api.md5(cbyte).digest()

    @staticmethod
    def hsha1(cbyte):
        return h_api.sha1(cbyte).hexdigest()

    @staticmethod
    def bsha1(cbyte):
        return h_api.sha1(cbyte).digest()

    @staticmethod
    def hsha256(cbyte):
        return h_api.sha256(cbyte).hexdigest()

    @staticmethod
    def bsha256(cbyte):
        return h_api.sha256(cbyte).digest()

    # @staticmethod
    # def hexdigest(binBytes):
    #     return

if __name__ == '__main__':
    print h_api.bmd5('12345')