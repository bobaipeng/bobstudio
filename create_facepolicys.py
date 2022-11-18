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
requests.packages.urllib3.disable_warnings()
log = logging.getLogger(__name__)


def create_device(uri, headers, num, userid):
    headers["Content-Type"] = "application/json"
    list_temp = []
    # 添加设备
    for i in range(1, num+1):
        body = {"deviceSerial": "face_"+str(i), "deviceCnName": "face_"+str(i), "deviceEnName": "", "deviceSecret": "", "deviceIP": "101", "devicePort": "", "desc": "", "productType": "12", "deviceType": "2", "deviceVersion": "101", "deviceTag": "", "externalDid": "", "deviceUri": "rtsp://10.151.5.160:8554/yangling/face_1", "deviceConnType": "", "deviceProtocol": "",
                "matchingThreshold": "", "streamWidth": 1920, "streamHeight": 1080, "faceAttribute": "0", "livenessCheck": "0", "ingressQCThreshold": "", "frameRate": "", "boundingBoxSizeThreshold": "", "bkImageStorage": "0", "targetGroup": "", "validRegionDefinition": [], "privilege": "", "operatePerson": str(userid), "ingressAngleThreshold": ""}
        res = requests.post(url='https://' + uri + '/DEVICE/device/create',
                            headers=headers, verify=False, json=body).json()
        print(str(i)+"创建设备---------------->:"+str(res))
        list_temp.append(res['data'])
    return list_temp


def create_policy(uri, headers, list_ids, userid):
    for _id in list_ids:
        body = {"desc": "facepo_"+_id, "deviceScope": "", "eventType": "", "monitorPeriodEnd": "", "monitorPeriodStart": "", "operatePerson": str(userid), "policyActions": [{"actionContent": "111", "actionTarget": "11111111111", "actionType": "3"}], "policyDevices": [{"deviceId": _id, "deviceSerial": "", "deviceType": "2"}], "policyId": "", "policyName": "facepo_"+_id, "policyTargets": [
            {"targetValue": "8", "operator": "2", "classId": "0", "targetId": "0"}], "policyType": "0", "rollingCount": "", "rollingWindow": "", "consecutiveWindow": "", "consecutiveCount": "", "targetScope": "", "validPeriodEnd": "", "validPeriodStart": "", "monitorPeriodWeekday": ""}
        res = requests.post(url='https://' + uri + '/POLICYMONITOR/faceMonitoringPolicy/create',
                            headers=headers, verify=False, json=body).json()
        print("创建策略---------------->:"+str(res))

#陌生人 "targetValue": "-99"  人员组 填组id


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


if __name__ == '__main__':
    uri = "www.studio79.com"
    headers = auth_head(uri)
    userid = get_userid(uri, headers)
    list_ids = create_device(uri, headers, 1, userid)
    create_policy(uri, headers, list_ids, userid)
    # time.sleep(60)
    #time.sleep(30*60)
    # print(uri)
    # headers = auth_head(uri)
    # userid = get_userid(uri, headers)
    # delete_devices(uri, headers, "face", userid)
    # delete_policys(uri, headers, "face", userid)
    print('end')
