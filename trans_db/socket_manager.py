# coding= utf-8
# Author : k2yk

from misc_method.client import client_method
from sockDB import sockDB
import socksconf
import os
import platform
import socket

class sock_manager:
    db_interface = sockDB()


    def set_keepalive_linux(self,sock, after_idle_sec=1, interval_sec=3, max_fails=5):
        """Set TCP keepalive on an open socket.

        It activates after 1 second (after_idle_sec) of idleness,
        then sends a keepalive ping once every 3 seconds (interval_sec),
        and closes the connection after 5 failed ping (max_fails), or 15 seconds
        """

        if os.name == 'nt':
            sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
        else:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, after_idle_sec)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, interval_sec)
            sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, max_fails)
        return  sock

    def newsock(self,uid):
        try:
            result = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            result =  self.set_keepalive_linux(result)
            self.db_interface.sockdb[uid] = result
            return True
        except :
            return False

    def connect(self,uid,ip,port):
        if ip and port:
            if uid in self.db_interface.sockid:
                soc = self.db_interface.sockdb[uid]
                soc.connect((ip,port))
                return True
        else:
            return  False

    def opensock(self):
        port = socksconf.opport


    def recv(self,uid,lengthd):
        if uid in self.db_interface.sockid:
            soc = self.db_interface.sockdb.get(uid)
            result = soc.recv(lengthd)
            return result
        else:
            return False

    def suspend(self,uid):
        if uid in self.db_interface.sockid:
            pass
    #
    # def stayalive(self,uid):
    #     if uid in self.db_interface.sockid:
    #         pass

    def send(self,uid,data,flag = None):
        if uid in self.db_interface.sockid:
            sock = self.db_interface.sockdb.get(uid)
            sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            if sock:
                if not flag:
                    sock.send(data)
                else:
                    sock.send(data,flag)

    def listen(self,threadnum = 10):
        pass

    def auth(self,uid):
        if uid in self.db_interface.sockid:
            if self.db_interface.sockauth.get(uid):
                return True
        return False

    def initauth(self,uid,authdata):
        if uid in self.db_interface.sockid:
            if not self.db_interface.sockauth.get(uid):
                self.db_interface.sockauth[uid] = client_method.new_uuid()
                return 'Auth'
            else:
                return True
        else:
            return False



    def get_info(self,uid):
        if uid in self.db_interface.sockid:
            dic = {}
            dic['uid'] = self.db_interface.sockid.get(uid)
            dic['auth'] = self.db_interface.sockauth.get(uid)
            dic['connect'] = self.db_interface.sockconnect.get(uid)
            dic['ip'] = self.db_interface.sockip.get(uid)
            dic['mac'] = self.db_interface.sockmac.get(uid)
            dic['time'] = self.db_interface.socktimeout.get(uid)
            dic['pipe'] = self.db_interface.sockdb.get(uid)
            return dic
        return False
