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

uri = "www.studio195.com"

def test_delete_persons(studioHeaders):
    userid = get_userid(uri, studioHeaders)
    body = {"sts":"0","current":1,"size":20000,"cnName":"1","idNumber":"","documentId":"","lastModTsEnd":"","lastModTsStart":""}
    res = requests.post(url='https://'+ uri +'/PERSON/person/pageList', headers=studioHeaders,verify=False,json=body).json()
    
    #删除person
    for _person in res['data']:
        body = {"uidList":[ _person['uid'] ],"operatePerson":str(userid)}
        res = requests.post(url='https://'+ uri +'/PERSON/person/deactivate', headers=studioHeaders,verify=False,json=body).json()
        print("删除人员---------------->:"+_person['uid'])
def auth_head(uri):
    body ={"username":"autotest","password":"zsPQQvGXaduTogVTfvDicg==","accountType":"0"}
    res=requests.post(url='https://'+ uri +"/GUNS/mgr/login", verify=False,json=body).json()
    autho_str=res['data']
    headers = {'Authorization': 'Basic '+autho_str}
    print(type(headers))
    return headers

def get_userid(uri, headers):
    res = requests.get(url='https://' + uri + "/GUNS/mgr/isLogin",
                       headers=headers, verify=False).json()
    return res['data']['user']['id']