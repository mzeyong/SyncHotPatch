# coding= utf-8
# Author : k2yk

import socket

soc = socket.socket()

class sock:
    def __init__(self):
        pass

    def get_peer_ip(self,soc):
        return soc.getpeername()[0]

    def get_peer_port(self,soc):
        return soc.getpeername()[1]

    def get_peer_host(self,soc):
        return soc.getpeername