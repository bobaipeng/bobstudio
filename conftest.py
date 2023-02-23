import pytest
import requests
from _pytest import scope


@pytest.fixture(scope=='session')
def studioHeaders():
    uri = "www.studio195.com"
    body ={"username":"autotest","password":"zsPQQvGXaduTogVTfvDicg==","accountType":"0"}
    res=requests.post(url='https://'+ uri +"/GUNS/mgr/login", verify=False,json=body).json()
    autho_str=res['data']
    headers = {'Authorization': 'Basic '+autho_str}
    print(type(headers))
    return headers