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


def create_device (uri,headers,num,userid):
    headers["Content-Type"]="application/json"
    list_temp=[]
    #添加设备
    for i in range(1,num+1):
        body = {"deviceSerial":"shildface_"+str(i),"deviceCnName":"shildface_"+str(i),"deviceEnName":"","deviceSecret":"","deviceIP":"111","devicePort":"","desc":"","productType":"12","deviceType":"22","deviceVersion":"111","deviceTag":"","externalDid":"","deviceUri":"rtsp://10.151.174.31:8554/performance/shielding","deviceConnType":"","deviceProtocol":"","matchingThreshold":"","streamWidth":"","streamHeight":"","faceAttribute":"1","livenessCheck":"1","ingressQCThreshold":"","frameRate":"","boundingBoxSizeThreshold":"","bkImageStorage":"1","targetGroup":"","validRegionDefinition":None,"privilege":"0","operatePerson":str(userid),"ingressAngleThreshold":""}
        res = requests.post(url='https://'+ uri +'/DEVICE/device/create', headers=headers,verify=False,json=body).json()
        print(str(i)+"创建设备---------------->:"+str(res))
        list_temp.append(res['data'])
    return list_temp
def create_policy(uri,headers,list_ids,userid):
     for _id in list_ids:
        body={"consecutiveCount":"","consecutiveWindow":"","desc":"","deviceScope":"","monitorPeriodEnd":"","monitorPeriodStart":"","monitorPeriodWeekday":"","monitoringRoi":[{"monitoringPolicyUuid":"","operatePerson":"73","did":str(_id),"regionPicUrl":"/images/cognitivesvc/fetchFrame/20221018/09/515d287554c14ab7bad76727da977b5c.jpg","roi":[{"appliedModels":[{"modelID":"1571170032370475010","modelName":"shieldFace","modelFrequency":"3","modelFrequencyType":"2","keyFrameDetection":"1","modelParameter":"{\"threshold\":\"0.5\",\"minSize\":\"60\",\"bufferSize\":\"\",\"bufferExpire\":\"\",\"scale\":\"\"}"}],"regionId":"","roiIdentifier":str(_id),"regionType":"0","regionName":"e","regionDirection":"","regionDef":"[{\"x\":144,\"y\":57.375},{\"x\":90,\"y\":1977.375},{\"x\":3720,\"y\":2061.375},{\"x\":3672,\"y\":93.375},{\"x\":3672,\"y\":93.375}]"}]}],"operatePerson":str(userid),"policyActions":[{"actionContent":"11","actionTarget":"11","actionType":"3"}],"policyDevices":[{"deviceId":str(_id),"deviceSerial":"","deviceType":""}],"policyId":"","policyName":"shildfacef_"+str(userid),"policyTargets":[{"targetId":"27","targetValue":"3","operator":"2","classId":"0","matchingThreshold":"0.2"}],"policyType":"6","rollingCount":"","rollingWindow":"","targetScope":"","validPeriodEnd":"","validPeriodStart":""}
        res = requests.post(url='https://'+ uri +'/POLICYMONITOR/roiMonitoringPolicy/create', headers=headers,verify=False,json=body).json()
        print("创建策略---------------->:"+str(res))
def delete_devices(uri,headers,keyword,userid):
        body = {"current":1,"size":100,"productType":[],"deviceType":[],"deviceCnName":"","deviceSerial":keyword,"deviceTag":"","sts":""}
        res = requests.post(url='https://'+ uri +'/DEVICE/device/list', headers=headers,verify=False,json=body).json()
        list_temp = res['data']
        for _device in list_temp:
            body = {"did":_device['did'],"operatePerson":str(userid)}
            res = requests.post(url='https://'+ uri +'/DEVICE/device/deactivate', headers=headers,verify=False,json=body).json()
            print("删除设备---------------->:"+str(res))
def delete_policys(uri,headers,keyword,userid):
        body = {"current":1,"size":20,"policyName":str(keyword),"policyType":"","deviceId":[]}
        res = requests.post(url='https://'+ uri +'/POLICYMONITOR/monitoringPolicy/list', headers=headers,verify=False,json=body).json()
        list_temp = res['data']
        for _policy in list_temp:
            body = {"policyIds":[_policy['policyId']],"operatePerson":str(userid)}
            res = requests.post(url='https://'+ uri +'/POLICYMONITOR/monitoringPolicy/deactivate', headers=headers,verify=False,json=body).json()
            print("删除策略---------------->:"+str(res))

def auth_head(uri):
    body = {"username":"admin","password":"zsPQQvGXaduTogVTfvDicg==","accountType":"0"}
    res=requests.post(url='https://'+ uri +"/GUNS/mgr/login", verify=False,json=body).json()
    autho_str=res['data']
    headers = {'Authorization': 'Basic '+autho_str}
    print(type(headers))
    return headers
def get_userid(uri,headers):
     res=requests.get(url='https://'+ uri +"/GUNS/mgr/isLogin", headers=headers,verify=False).json()
     return res['data']['user']['id']
if __name__ == '__main__':
    uri = "www.studio218.com"
    headers = auth_head(uri)
    userid = get_userid(uri,headers)
    list_ids=create_device(uri,headers,10,userid)
    create_policy(uri,headers,list_ids,userid)
    # time.sleep(5)
    # time.sleep(60*60)
    # delete_devices(uri,headers,"face",userid)
    # delete_policys(uri,headers,"face",userid)
    print('end')