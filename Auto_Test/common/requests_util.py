import requests


class RequestUtil:
    session = requests.Session()

    def send_request(self,method,url,data,**kwargs):
        method = str(method).lower()#变成小写
        res = ""
        if method == 'get':
            res = RequestUtil.session.request(method,url,params=data,**kwargs)
        elif method == 'post':
            res = RequestUtil.session.request(method,url,json=data,**kwargs)
        return res
