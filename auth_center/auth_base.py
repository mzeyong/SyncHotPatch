# coding= utf-8
# Author : k2yk



class auth_base:


    def __init__(self):
        self.key = 'helloworld'
        self.auth_key_uuid = []

    def auth(self,uu,key = 'helloworld'):
        if uu not in self.auth_key_uuid:
            if key == self.firstKey:
                self.auth_key_uuid.append(uu)
                return True
            else:
                return False
        else:
            return True

    def check(self,uu):
        if uu in self.auth_key_uuid:
            return True
        return False
