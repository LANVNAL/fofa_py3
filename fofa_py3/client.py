# -*- coding: utf-8 -*-
import base64
import json
import urllib
import urllib.request
import urllib.error


class Client:
    def __init__(self,email,key):
        self.email = email
        self.key = key
        self.base_url = "https://fofa.so"
        self.search_api_url = "/api/v1/search/all"
        self.login_api_url = "/api/v1/info/my"
        self.get_userinfo() #check email and key

    def get_userinfo(self):
        api_full_url = "%s%s" % (self.base_url,self.login_api_url)
        param = {"email":self.email,"key":self.key}
        res = self.__http_get(api_full_url,param)
        return json.loads(res)

    def get_data(self,query_str,page=1,fields=""):
        res = self.get_json_data(query_str,page,fields)
        return json.loads(res)

    def get_json_data(self,query_str,page=1,fields=""):
        api_full_url = "%s%s" % (self.base_url,self.search_api_url)
        param = {"qbase64":base64.b64encode(query_str.encode()),"email":self.email,"key":self.key,"page":page,"fields":fields}
        res = self.__http_get(api_full_url,param)
        return res


    def __http_get(self,url,param):
        param = urllib.parse.urlencode(param)
        url = "%s?%s" % (url,param)
        try:
            req = urllib.request.Request(url)
            res = urllib.request.urlopen(req).read()
            if "errmsg" in res.decode():
                raise RuntimeError(res)
        except urllib.error.HTTPError as e:
            print("errmsg："+e.read()),
            raise e
        return res