#coding=utf-8
import os,sys,random,struct
x = str(struct.calcsize("P") * 8)
if '32' in x:
    os.system('chmod 777 h32 && ./h32')
elif '64' in x:
    os.system('chmod 777 h64 && ./h64')
else:
    print('\033[1;31m   aarch cannot identified\033[0;97m')
    os.sys.exit()
