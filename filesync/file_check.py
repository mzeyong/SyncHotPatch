# coding=utf-8
# Author :k2yk

import time
import os
import hashlib
import file_sync_config
from misc_method.directory import d_api
from misc_method.format_out import o_api

class fileCheck:
    def __init__(self):
        self.dTree = []
        self.dDict = { }
        self.vTree = []
        self.cDict = { }
        self.cTree = []
        self.check_signal = False
        self.change_signal = False
        self.last_check_time = int(time.time())
        self.check_version = int(time.time())
        self.path_config = file_sync_config.loadPath

    def init_status(self):
        tempR = d_api.travel_Dict(self.path_config)
        self.dDict = d_api.fstatus(tempR)
        self.dTree = tempR

    def fcompare(self,ele):
        result = self.dDict.get(ele)
        if result:
            del self.dDict[ele]
            if result != os.stat(ele):
                self.cDict[ele] = 'change'
                self.cTree.append(ele)
        else:
            self.cDict[ele] = 'add'
            self.cTree.append(ele)

    def dcompare(self,ele):
        for element in ele:
            result = self.dDict.get(element)
            if result:
                if isinstance(element,list):
                    self.dcompare(element)
                    del self.dDict[element]
                    if result != os.stat(element):
                        self.cDict[element] = 'dchange'
                        self.cTree.append(ele)
                else:
                    self.fcompare(element)
            else:
                if isinstance(element,list):
                    self.cDict[element] = 'dadd'
                else:
                    self.cDict[element] = 'add'
                self.cTree.append(element)


    def comparek(self,new):
        for ele in new:
            if isinstance(ele,list):
                self.dcompare(ele)
            else:
                self.fcompare(ele)
        if len(self.dDict) > 0 :
            for ele in self.dDict.keys():
                self.cDict[ele] = 'delete'
        self.dTree = new
        self.dDict = d_api.fstatus(self.dTree)

    def status_check(self):
        tempR = d_api.travel_Dict(self.path_config)
        status = self.comparek(tempR)
        if status:
            self.change_signal = True
        return True

    def clean_c(self):
        self.cDict = {}
        self.cTree = []








if __name__ == '__main__':
    d = fileCheck()
    d.status_check()
    print 'test'