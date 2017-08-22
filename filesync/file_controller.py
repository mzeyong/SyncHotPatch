# coding=utf-8
# Author :k2yk

import time
import os
import hashlib
import file_sync_config
from misc_method.directory import d_api
from misc_method.format_out import o_api
from misc_method.hash_lib import h_api


class fileController:
    h_interface = h_api()

    def deleteFile(self,path):
        try:
            os.remove(path)
            return True
        except:
            return False

    def deleteDir(self,path):
        try:
            os.removedirs(path)
            return True
        except:
            return False

    def addFile(self,path,codeByte):
        try:
            t = self.h_interface.hmd5(codeByte)
            with open(path ,'wb') as wf:
                wf.write(codeByte)
                wf.flush()
            with open(path, 'rb') as wf:
                d = self.h_interface.hmd5(wf.read())
                if d == t:
                    return True
            return False
        except:
            return False

    def makeDir(self,path,mode = 644):
        try:
            os.mkdir(path,mode)
            if os.path.isdir(path):
                return True
            else:
                return False
        except:
            return False

    def changeFile(self,path,codeByte):
        temp = ''
        with open(path, 'rb') as wf:
            temp = wf.read()
        try:
            t = self.h_interface.hmd5(codeByte)
            with open(path ,'wb') as wf:
                wf.write(codeByte)
                wf.flush()
            with open(path, 'rb') as wf:
                d = self.h_interface.hmd5(wf.read())
                if d == t:
                    return True
            with open(path, 'wb') as wf:
                wf.write(temp)
                wf.flush()
            return False
        except:
            with open(path, 'wb') as wf:
                wf.write(temp)
                wf.flush()
            return False

    def readF(self,path):
        try:
            temp = ''
            with open(path ,' rb') as rf :
                temp = rf.read()
            return temp
        except:
            return False


if __name__ == '__main__':
    t = fileController()