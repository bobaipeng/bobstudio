# -*- coding: UTF-8 -*-
'''
@Project ：sense-foundry-enterprise 
@File ：fire_p1_one_device_one_roi.py
@Author ：baibo.vendor
@Date ：2022/1/20 10:34 
'''
import os

import requests
requests.packages.urllib3.disable_warnings()

import logging
import uuid as uuidtool
log = logging.getLogger(__name__)


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

def upload_create_add(file,uri,headers):
    headers = headers
    files = {'serviceType': (None, 'person'),'image':(open(file,'rb'))}
    res=requests.post(url='https://'+uri+'/UTILITY/files/uploadImage', headers=headers,files=files,verify=False).json()
    # print(res)
    #print(res['data'])
    body ={"birthday":"","cnName":str(uuidtool.uuid1()),"enName":"","idNumber":str(uuidtool.uuid1()),"documentId":"","imageURI":res['data'],"operatePerson":"75","sex":"","personType":"","personTag":"","desc":"","idType":"","idCountry":"","idExpiryDate":"","privilege":"0","expireDate":"","phone":"","externalUid":"","welcomeWords":"","externalInfo":None}
    res=requests.post(url='https://'+uri+'/PERSON/person/create', headers=headers,verify=False,json=body).json()
    # print(res)
    body ={"groupIdList":["8"],"operatePerson":"75","uid":res['data']}
    res=requests.post(url='https://'+uri+'/PERSON/member/addMemberToGroups', headers=headers,verify=False,json=body).json()
    #print(res)
def  getuserids(uri,userid,headers):
    body = {"current":1,"size":5000,"cnName":"","idNumber":"","type":""}
    res = requests.post(url='https://' + uri +"/PERSON/person/pageList",headers=headers, verify=False, json=body).json()
    data_list= res['data']
    ids_ist=[]
    for i in data_list:
        ids_ist.append(i['uid'])
    print(len(ids_ist))
    body={"operatePerson":userid,"groupId":"12","uidList":ids_ist}
    res = requests.post(url='https://' + uri +"/PERSON/member/addGroupMember",headers=headers, verify=False, json=body).json()
    print(res)
    body={"groupId":"12","cnName":"ren","type":"0","inGroupValidHour":"","operatePerson":userid}
    res = requests.post(url='https://' + uri +"/PERSON/personGroup/update",headers=headers, verify=False, json=body).json()
    print(res)
    return ids_ist

def get_file_path(root_path,file_list,dir_list):
    #获取该目录下所有的文件名称和目录名称
    dir_or_files = os.listdir(root_path)
    for dir_file in dir_or_files:
        #获取目录或者文件的路径
        dir_file_path = os.path.join(root_path,dir_file)
        #判断该路径为文件还是路径
        if os.path.isdir(dir_file_path):
            dir_list.append(dir_file_path)
            #递归获取所有文件和目录的路径
            get_file_path(dir_file_path,file_list,dir_list)
        else:
            file_list.append(dir_file_path)
if __name__ == '__main__':
    uri = 'www.studio195.com'
    headers = auth_head(uri)
    userid = get_userid(uri, headers)

    # path = 'D:/studio/person/distractor_8w_hk/distractor_8w_hk/capture'
    # file_list = []
    # dir_list = []
    # get_file_path(path,file_list,dir_list)
    # print(file_list)
    # print(len(file_list))
    # i=5000
    # while(i>=1):
    #         upload_create_add(file_list[i],uri,headers)
    #         print(i)
    #         i=i-1
    getuserids(uri,userid,headers)
    print('end')