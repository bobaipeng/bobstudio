# -*- coding: UTF-8 -*-
'''
@Project ：sense-foundry-enterprise 
@File ：fire_p1_one_device_one_roi.py
@Author ：baibo.vendor
@Date ：2022/1/20 10:34 
'''
import cv2
import time
import datetime
import requests
requests.packages.urllib3.disable_warnings()

import logging
import uuid as uuidtool
import threading
log = logging.getLogger(__name__)
import ffmpeg
import socket
import os

def auth_head(uri):
    body = {"username": "autotest",
            "password": "zsPQQvGXaduTogVTfvDicg==", "accountType": "0"}
    res = requests.post(url='https://' + uri +
                        "/GUNS/mgr/login", verify=False, json=body).json()
    autho_str = res['data']
    headers = {'Authorization': 'Basic '+autho_str}
    print(type(headers))
    return headers


def get_userid(uri, headers):
    res = requests.get(url='https://' + uri + "/GUNS/mgr/isLogin",
                       headers=headers, verify=False).json()
    return res['data']['user']['id']

def upload_create_add(file,uri,headers,j):
    headers = headers
    # files = {'serviceType': (None, 'person'),'image':(open(file,'rb'))}
    # res=requests.post(url='https://'+uri+'/UTILITY/files/uploadImage', headers=headers,files=files,verify=False).json()
    # # print(res)
    # print(res['data'])
    body ={"birthday":"","cnName":str(uuidtool.uuid1()),"enName":"","idNumber":str(uuidtool.uuid1()),"documentId":"","imageURI":"/images/person/20221108/164/74b1929bafe3442299f8d65041affdb9.jpg","operatePerson":"75","sex":"","personType":"","personTag":"","desc":"","idType":"","idCountry":"","idExpiryDate":"","privilege":"0","expireDate":"","phone":"","externalUid":"","welcomeWords":"","externalInfo":None}
    res=requests.post(url='https://'+uri+'/PERSON/person/create', headers=headers,verify=False,json=body).json()
    #print(res)
    body ={"groupIdList":[str(j)],"operatePerson":"75","uid":res['data']}
    res=requests.post(url='https://'+uri+'/PERSON/member/addMemberToGroups', headers=headers,verify=False,json=body).json()
    #print(res)
if __name__ == '__main__':
    uri = 'www.studio79.com'
    headers = auth_head(uri)
    userid = get_userid(uri, headers)
    path = 'D:/tu/1.jpg'
    j=12
    while(j<=98):
        i=10000
        headers = auth_head(uri)
        print( datetime.datetime.now()      )
        print(j )
        while(i>=1):
                upload_create_add(path,uri,headers,j)
                i=i-1                    
        j=j+1 
    print('end')