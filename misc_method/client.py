# coding= utf-8
# Author : k2yk

import uuid as uid
import os
import socket

class client_method:
    @staticmethod
    def get_uuid():
        with open('../config/uuid','r') as uuid:
            uu = uuid.read()
        if len(uu) <5:
            with open('../config/uuid', 'w') as uuid:
                result = client_method.new_uuid()
                uuid.write(result)
        else:result = uu
        return result

    @staticmethod
    def new_uuid():
        return str(uid.uuid1())

    @staticmethod
    def get_hostname():
        return socket.gethostname()

    @staticmethod
    def get_ip():
        return socket.gethostbyname(client_method.get_hostname())

    @staticmethod
    def get_mac_address():
        node = uid.getnode()
        mac = uid.UUID(int=node).hex[-12:]
        return mac

if __name__ == '__main__':
    d = client_method()
    print d.get_uuid()
    print d.get_ip()
    print d.get_hostname()
    print d.get_mac_address()