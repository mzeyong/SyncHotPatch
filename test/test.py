# coding= utf-8
# Author : k2yk

from  filesync import file_monitor

d = file_monitor.file_interface()


while 1:
    comand = raw_input('COMMAND : ')
    comand = str(comand)
    result = d.api(comand,1,1)
    print result