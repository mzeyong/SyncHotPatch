# coding=utf-8

import os
import hashlib

class d_api:

    @staticmethod
    def travel_Dict(path,signal = False):
        record = []
        if os.path.isdir(path):
            dT = os.listdir(path)
            record.append(path+'/')
            for ele in dT:
                if os.path.isfile(path+'/'+ele):
                    record.append(path+'/'+ele)
                elif os.path.isdir(path+'/'+ele):
                    record.append(d_api.travel_Dict(path+'/'+ele))
                else:
                    pass
        return record

    @staticmethod
    def fstatus(ldata):
        curDict = {}
        plen = len(ldata)
        ele = 0
        while ele < plen:
            td = ldata[ele]
            if isinstance(ldata[ele], list):
                curDict.update(d_api.fstatus(td))
            else:
                curDict[td] = d_api.getfstatus(td)
            ele += 1
        return curDict

    @staticmethod
    def fstatus1(ldata):
        curDict = {}
        plen = len(ldata)
        ele = 0
        while ele < plen:
            td = ldata[ele]
            if isinstance(ldata[ele], list):
                curDict[td[0]] = d_api.fstatus(td)
            else:
                curDict[td] = d_api.getfstatus(td)
            ele += 1
        return curDict

    @staticmethod
    def try_exec_func(func,funargs):
        pass

    @staticmethod
    def getfstatus(path):
        status = os.stat(path)
        return status