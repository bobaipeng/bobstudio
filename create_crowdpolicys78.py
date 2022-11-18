# -*- coding: UTF-8 -*-
'''
@Project ：
@File ：createtasks.py
@Author ：baibo.vendor
@Date ：2022/1/20 10:34 
'''
import logging
import time
import requests

import random
import string
requests.packages.urllib3.disable_warnings()
log = logging.getLogger(__name__)


def create_device(uri, headers, num, userid):
    headers["Content-Type"] = "application/json"
    list_temp = []
    # 添加设备
    for i in range(1, num+1):
        body = {"deviceSerial": "roibianaho_"+str(i), "deviceCnName": "roi_"+str(i), "deviceEnName": "", "deviceSecret": "", "deviceIP": "113", "devicePort": "", "desc": "", "productType": "12", "deviceType": "21", "deviceVersion": "113", "deviceTag": "", "externalDid": "", "deviceUri": "rtsp://10.151.5.160:8554/xing/crowd2p1080", "deviceConnType": "", "deviceProtocol": "",
                "matchingThreshold": "", "streamWidth": 1920, "streamHeight": 1080, "faceAttribute": "0", "livenessCheck": "1", "ingressQCThreshold": "", "frameRate": "", "boundingBoxSizeThreshold": "", "bkImageStorage": "0", "targetGroup": "", "validRegionDefinition": [], "privilege": "0", "operatePerson": str(userid), "ingressAngleThreshold": ""}
        res = requests.post(url='https://' + uri + '/DEVICE/device/create',
                            headers=headers, verify=False, json=body).json()
        print(str(i)+"创建设备---------------->:"+str(res))
        list_temp.append(res['data'])
    return list_temp


def create_policy(uri, headers, list_ids, userid):
    for _id in list_ids:
        ident_id = random_str(19)
        body = {"consecutiveCount": "", "consecutiveWindow": "", "desc": "name", "deviceScope": "", "monitorPeriodEnd": "", "monitorPeriodStart": "", "monitorPeriodWeekday": "", "monitoringRoi": [{"monitoringPolicyUuid": "", "operatePerson": str(userid), "did": _id, "regionPicUrl": "/images/cognitivesvc/fetchFrame/20221103/16/17aa8ffec959423983eb1cbb9abd34e3.jpg", "roi": [{"regionId": "", "roiIdentifier":  str(ident_id), "regionType": "0", "regionName": str(ident_id), "crossDirection": "", "regionDirection": "0.1", "regionDef": "[{\"x\":71.93144363876071,\"y\":53.015625},{\"x\":53.93100417490662,\"y\":1019.015625},{\"x\":1844.9747308283895,\"y\":1034.015625},{\"x\":1862.9751702922435,\"y\":38.015625},{\"x\":1862.9751702922435,\"y\":38.015625}]", "appliedModels": [
            {"modelID": "1587280470787256321", "modelName": "coloCrowdCount", "modelFrequency": "1", "modelFrequencyType": "0", "keyFrameDetection": "1", "modelParameter": "{\"minSize\":\"22\",\"threshold\":\"0.5\",\"bufferExpire\":\"\",\"bufferSize\":\"\",\"scale\":\"\"}"}]}], "distanceBetweenLines": ""}], "operatePerson": str(userid), "policyActions": [{"actionContent": "1", "actionTarget": "1", "actionType": "3"}], "policyDevices": [{"deviceId": _id, "deviceSerial": "", "deviceType": ""}], "policyId": "", "policyName": "ce_"+_id, "policyTargets": [{"targetId": "54", "targetValue": "1", "operator": "0", "classId": "0", "matchingThreshold": "0.1"}], "policyType": "7", "rollingCount": "", "rollingWindow": "", "targetScope": "", "validPeriodEnd": "", "validPeriodStart": "", "eventTrackTime": "", "eventTrackFreq": ""}
        res = requests.post(url='https://' + uri + '/POLICYMONITOR/roiMonitoringPolicy/create',
                            headers=headers, verify=False, json=body).json()
        print("创建策略---------------->:"+str(res))


def delete_devices(uri, headers, keyword, userid):
    body = {"current": 1, "size": 100, "productType": [], "deviceType": [],
            "deviceCnName": "", "deviceSerial": keyword, "deviceTag": "", "sts": ""}
    res = requests.post(url='https://' + uri + '/DEVICE/device/list',
                        headers=headers, verify=False, json=body).json()
    list_temp = res['data']
    for _device in list_temp:
        body = {"did": _device['did'], "operatePerson": str(userid)}
        res = requests.post(url='https://' + uri + '/DEVICE/device/deactivate',
                            headers=headers, verify=False, json=body).json()
        print("删除设备---------------->:"+str(res))


def delete_policys(uri, headers, keyword, userid):
    body = {"current": 1, "size": 20, "policyName": str(
        keyword), "policyType": "", "deviceId": []}
    res = requests.post(url='https://' + uri + '/POLICYMONITOR/monitoringPolicy/list',
                        headers=headers, verify=False, json=body).json()
    list_temp = res['data']
    for _policy in list_temp:
        body = {"policyIds": [_policy['policyId']],
                "operatePerson": str(userid)}
        res = requests.post(url='https://' + uri + '/POLICYMONITOR/monitoringPolicy/deactivate',
                            headers=headers, verify=False, json=body).json()
        print("删除策略---------------->:"+str(res))


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


def random_str(n):
    """ 生成指定 n 长度的随机字符串
    """
    s = '01234567890123456789'
    return ''.join(random.sample(s, n))


if __name__ == '__main__':
    uri = "www.studio218.com"
    headers = auth_head(uri)
    userid = get_userid(uri, headers)
    list_ids = create_device(uri, headers, 10, userid)
    create_policy(uri, headers, list_ids, userid)
    time.sleep(5)
    time.sleep(30*60)
    print(uri)
    headers = auth_head(uri)
    userid = get_userid(uri, headers)
    delete_devices(uri, headers, "roibianaho", userid)
    delete_policys(uri, headers, "ce_", userid)
    print('end')
