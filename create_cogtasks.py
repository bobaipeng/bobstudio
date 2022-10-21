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


def create_tasks (uri,headers,num):
    headers["Content-Type"]="application/json"
    # #添加配置
    # for i in range(1,num+1):
    #     body = {"taskId":"roiIntrusion"+str(i),"processor":"roiIntrusion","type":2,"rtspHeight":1080,"rtspWidth":1920,"interval":3,"threshold":0.5,"minSize":22}
    #     res = requests.post(url='https://'+ uri +'/APIPKG/apipkg/async/video/addTask', headers=headers,verify=False,json=body).json()
    #     print(str(i)+"添加配置---------------->:"+str(res))
    
    #执行视频
    for i in range(1,num+1):
        time.sleep(3)
        body = {"taskId":"roiIntrusion"+str(i),"processor":"roiIntrusion","video":"/images/4h7minroi_1h_"+str(num)+".mp4","type": 2,"rtspHeight": 1080,"rtspWidth": 1920,"interval": 3,"threshold": 0.5,"minSize": 22}
        res = requests.post(url='https://'+ uri +'/APIPKG/apipkg/async/video/analysis', headers=headers,verify=False,json=body).json()
        print(str(i)+"执行视频---------------->:"+str(res))
def delete_tasks(uri,headers,num):
    #删除配置
    for i in range(1,num+1):
        data = {"taskId":"roiIntrusion"+str(i)}
        res = requests.post(url='https://'+ uri +'/APIPKG/apipkg/analysis/task/delete', headers=headers,verify=False,data=data).json()
        print(str(i)+"删除配置---------------->:"+str(res))
def auth_head(uri):
    body = {"username":"Almighty","password":"06919a6df17b4959b4dd5e94552b408a","accountType":"2"}
    res=requests.post(url='https://'+ uri +"/GUNS/mgr/login", verify=False,json=body).json()
    autho_str=res['data']
    headers = {'Authorization': 'Basic '+autho_str}
    print(type(headers))
    return headers
if __name__ == '__main__':
    uri = "www.studio217.com"
    headers = auth_head(uri)
    create_tasks(uri,headers,16)
    #delete_tasks(uri,headers,17)
    print('end')