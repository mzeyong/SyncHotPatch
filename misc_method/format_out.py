
class o_api:

    blank = '    '

    @staticmethod
    def format_dict_string(tempD,num = 1,blank_length = 4):
        f_blank = o_api.blank * num
        res = '{\n'
        for ele in tempD.keys():
            if isinstance(tempD[ele],dict):
                res += f_blank + '"' + str(ele) + '" : ' + o_api.format_dict_string(tempD[ele],num+1) + ' ,\n'
            else:
                res += f_blank + '"' + str(ele) + '" : "' + str(tempD[ele]) + '" ,\n'
        res = res[:-2] + '\n'+ f_blank[:-blank_length] +'}'
        return res

    @staticmethod
    def format_dict_print(tempD):
        result = o_api.format_dict_string(tempD)
        print result