# -*- coding: UTF-8 -*-
'''
@Project ：
@File ：createtasks.py
@Author ：baibo.vendor
@Date ：2022/1/20 10:34 
'''
import time
import requests
requests.packages.urllib3.disable_warnings()
import logging
log = logging.getLogger(__name__)


def create_tasks (num):

    with open("D:\ids500.csv", "w", encoding="utf-8") as f:
        
        for i in range(1,num+1):
            f.write("SPS020STDC"+str(i)+"_0,24"+"\n")
def  get_time():
    localtime = time.localtime(time.time())
    sec= time.mktime(localtime)
    print(sec)
if __name__ == '__main__':
    create_tasks(500)
    get_time()
    print('end')