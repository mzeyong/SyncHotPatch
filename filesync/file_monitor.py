# coding= utf-8
# Author : k2yk

import os
from file_check import fileCheck
from file_controller import fileController
from misc_method import encrypt
import file_sync_config
import time
import threading
import logging


class file_interface:

    def __init__(self):
        self.c_signal = False
        self.w_signal = False
        self.r_signal = True
        self.version = int(time.time())
        self.c_api = fileCheck()
        self.c_api.init_status()
        self.e_api = encrypt.e_api()
        self.w_api = fileController()
        self.action_Dict = {
            'CHECK':self.check_change,
            'TRANS':self.transport,
            'INIT':self.init_file,
            'VERSION':self.get_version,
            'FINISH':self.cleanup,
        }
        self.time_span = 20
        self.threadPool = []
        self.thread = threading.Thread(target=self.timmer)
        self.thread.start()
        self.threadPool.append(self.thread)

    def cleanup(self,p):
        self.c_api.clean_c()
        self.c_signal = False

    def timmer(self):
        while self.r_signal:
            time.sleep(self.time_span)
            if self.c_signal == False:
                self.check_change('localCheck')
            else:
                pass
            timeArray = time.localtime(time.time())
            otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
            log = 'INFO '+ str(otherStyleTime) + ' running local check file change \n'
            print log


    def get_version(self,p):
        return self.version

    def check_change(self,p):
        result = self.c_api.status_check()
        if len(self.c_api.cDict) > 0 :
            self.c_signal = True
            print 'Change'

        return self.c_api.cDict

    def init_file(self,p):
        result = self.c_api.dTree
        return result

    def transport(self,path):
        if file_sync_config.E_FLAGS:
            result = self.w_api.readF(path)
            result = self.e_api.rc4(result)
        else:
            result = self.w_api.readF(path)
        return (path , result)

    def api(self, status , ids ,p, version = None):
        try:
            if not version or  not status:
                result = (500,False)
                # return result
            elif status in self.action_Dict:
                pass
            else:
                status = 'VERSION'
            action = self.action_Dict.get(status)
            try:
                result = (200,action(p))
            except:
                result = (500,False)
            if not ids:
                result = (500,False)
            return result
        except:
            return False
        pass


if __name__ == '__main__':
    d = file_interface()
    print 1
    time.sleep(23)
    print 2
