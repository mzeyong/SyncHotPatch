# coding= utf-8
# Author : k2yk

from filesync.file_monitor import file_interface
from auth_center.auth_base import auth_base
from misc_method.client import  client_method
from command_analyz.proto_package import proto
from trans_db import socket_manager
from config import resource,sysconf
from auth_center import base_data
from thread_method.thread_method import thread
from command_analyz.actionDict import ACTION


class control:

    def __init__(self):
        self.f_interface = file_interface()
        self.a_interface = auth_base()
        self.p_interface = proto()
        self.s_interface = socket_manager.sock_manager()
        self.c_interface = client_method()
        self.uid = ''
        self.serverConfig = {
            'mip':sysconf.main_c,
            'mp':sysconf.main_p
        }
        self.clientConfig = base_data.client()


    def init_connect(self,ip = None,port = None):
        self.uid = self.c_interface.get_uuid()
        self.s_interface.newsock(self.uid)
        self.s_interface.connect(self.uid,self.serverConfig['mip'],self.serverConfig['mp'])
        self.a_interface.auth(self.uid,'helloworld')
        self.s_interface.listen()
        self.f_interface.timmer()

    def slovePacket(self,packet):
        result = self.p_interface.analyz(packet)
        thread.startThread(self._sloveCommand,result)
        return True


    def _sloveCommand(self,commandDict):
        keyd = commandDict.keys()




    def start(self):
        pass
