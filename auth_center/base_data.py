# coding= utf-8
# Author : k2yk

import random
import time

from misc_method.client import client_method


class client:
    def __init__(self):
        self.ids = client_method.get_uuid()
        self.ips = client_method.get_ip()
        self.mac = client_method.get_mac_address()
        self.host = client_method.get_hostname()




