# -*- coding: UTF-8 -*-
'''
@Project ：sense-foundry-enterprise 
@File ：fire_p1_one_device_one_roi.py
@Author ：baibo.vendor
@Date ：2022/1/20 10:34 
'''
import cv2
import time
import requests
requests.packages.urllib3.disable_warnings()

import logging
import uuid as uuidtool
import threading
log = logging.getLogger(__name__)
import ffmpeg
import socket
import os


def upload_create_add(file):
    headers = {'Authorization': 'Basic YmFpYm8sMDpneHJ3eHI='}
    files = {'serviceType': (None, 'person'),'image':(open(file,'rb'))}
    res=requests.post(url='https://www.studio218.com/UTILITY/files/uploadImage', headers=headers,files=files,verify=False).json()
    #print(res)
    #print(res['data'])
    body={"birthday":"","cnName":str(uuidtool.uuid1()),"enName":"","idNumber":str(uuidtool.uuid1()),"documentId":"","imageURI":res['data'],"operatePerson":"22","sex":"","personType":"","personTag":"","desc":"","idType":"","idCountry":"","idExpiryDate":"","privilege":"","expireDate":"","phone":""}
    res=requests.post(url='https://www.studio218.com/PERSON/person/create', headers=headers,verify=False,json=body).json()
    #print(res)
    body ={"groupIdList":["8"],"operatePerson":"74","uid":res['data']}
    res=requests.post(url='https://www.studio218.com/PERSON/member/addMemberToGroups', headers=headers,verify=False,json=body).json()
    #print(res)
if __name__ == '__main__':
    path = 'D:/tu/'
    i=1
    j=1
    while(i<=3000):
        for f in os.listdir(path):
            upload_create_add(path+f)
            print(i)
            i=i+1
    print('end')