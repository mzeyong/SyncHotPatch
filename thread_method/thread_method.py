# coding= utf-8
# Author : k2yk

import threading

class thread :
    def __init__(self):
        pass

    @staticmethod
    def startThread(func,funargs):
        try:
            result = threading.Thread(target=func,args=funargs)
            result.setDaemon(True)
            result.start()
            return  True
        except :
            return False

    @staticmethod
    def killThread(pid):
        pass