# coding= utf-8
# Author : k2yk

from misc_method.client import *
from misc_method.crypt._b64 import b64


class proto:
    __doc__ = 'hpf_frame'

    p_split = '|{}|'

    p_status_dict = {
        'done':200,
        'error':500,
        'not found':400,
        'author':100,
    }
    @staticmethod
    def analyz(datastream):
        dataDict = datastream.split(proto.p_split)
        result = {}
        for element in range(len(dataDict)):
            if len(dataDict[element]) < 1:
                pass
            elif element >0 and element<len(dataDict):
                temp = dataDict[element].split(' ')
                result[temp[0]] = b64.decode(temp[1])
            elif element == 0:
                temp = dataDict[element].split(' ')
                result['status'] = temp[0]
                result['status_code'] = temp[1]
        print dataDict
        return result

    @staticmethod
    def pack(**kwargs):
        s_ips = kwargs.get('ips')
        s_author = kwargs.get('author')
        s_host = kwargs.get('hosts')
        s_mac = kwargs.get('mac')
        s_uuid = kwargs.get('uuid')
        s_datastream = kwargs.get('datastream')
        s_status = kwargs.get('status')
        if not s_ips:
            s_ips = client_method.get_ip()

        if not s_author:
            result = 'AUTHOR 100'
            return result

        if not s_host :
            s_host = client_method.get_hostname()
        if not s_mac:
            s_mac = client_method.get_mac_address()

        if not s_uuid:
            s_uuid = client_method.get_uuid()

        if not s_datastream:
            return False

        if not s_status:
            return False

        s_info = str(s_ips)+str(s_uuid)+str(s_mac)+str(s_host)

        s_datastream = str(s_datastream)


        result = ''

        result += str(s_status) + ' 200'
        result += proto.p_split
        result += 'sinfo ' + b64.encode(s_info) + ''
        result += proto.p_split
        result += 'data '+ b64.encode(s_datastream)
        result += proto.p_split

        return result

if __name__ == '__main__':
    d = proto()
    uuidd = '3535c640-7c1a-11e7-b0a4-00249b05ea27'
    author = 1234
    ips = '1.1.1.1'
    data = 'helloworld'
    status = 'CHECK'
    result = d.pack(ips = ips,author=author,hosts = 'fuck',mac = None ,uuid = uuidd,datastream=data,status=status)
    print result
    print d.analyz(result)

