import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def GetRequest(url):
    r = requests.get(url,
                     headers=_headers,
                     auth=(_user_name, _password),
                     verify=False)
    print(json.dumps(json.loads(r.text), indent=1))


if __name__ == "__main__":
    """
    AWX Basic認証
    """
    _host = "127.0.0.1"
    _user_name = "user"
    _password = "password"

    _headers = {"Content-Type": "application/json"}
    #_url = "http://%s/api/v2/job_templates/" % _host

    _url = "http://%s/api/v2/workflow_job_template_nodes/" % _host
    print(_url)
    GetRequest(_url)

    #_url = "http://%s/api/v2/workflow_job_nodes/" % _host
    # print(_url)
    # GetRequest(_url)

    #_url = "http://%s/api/v2/workflow_job_nodes/%s/always_nodes/" % (_host, 1)
    # print(_url)
    # GetRequest(_url)

    #_url = "http://%s/api/v2/workflow_job_nodes/%s/" % (_host, 1)
    # print(_url)
    # GetRequest(_url)

    _url = "http://%s/api/v2/workflow_job_templates/%s/workflow_nodes/" % (
        _host, 21)
    print(_url)
    GetRequest(_url)
    # 成功ノード(success_nodes)と失敗ノード(failer_nodes)の2つに分岐することはわかった
