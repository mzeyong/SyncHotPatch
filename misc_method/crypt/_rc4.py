# coding= utf-8
# Author : k2yk


import crypt_config

class rc4:

    @staticmethod
    def rc4(data, key=crypt_config.RC4_CONFIG):

        if (type(data) is type("string")):
            tmpData = data
            data = []
            for tmp in tmpData:
                data.append(ord(tmp))

        if (type(key) is type("string")):
            tmpKey = key
            key = []
            for tmp in tmpKey:
                key.append(ord(tmp))

        x = 0
        box = list(range(256))
        for i in range(256):
            x = (x + box[i] + key[i % len(key)]) % 256
            box[i], box[x] = box[x], box[i]

        x = 0
        y = 0
        out = []
        for c in data:
            x = (x + 1) % 256
            y = (y + box[x]) % 256
            box[x], box[y] = box[y], box[x]
            out.append(c ^ box[(box[x] + box[y]) % 256])

        result = ""
        printable = False

        if (printable == False):
            result = ""
            for tmp in out:
                result += chr(tmp)


        return result