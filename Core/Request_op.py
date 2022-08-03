import json
import requests



class RequestUnit:
    def send_request(self, method, url, datas, data_type, headers=None, cookies=None, **kwargs):
        """
        :param data_type:
        :param headers:
        :param cookies:
        :param method:
        :param url:
        :param datas:
        :param kwargs:
        :return:
        """
        req_session = requests.session()
        method = str(method).lower()
        res = None
        if method == "get":
            res = req_session.request(method=method, url=url, params=datas, headers=headers, cookies=cookies, **kwargs)
        elif method == "post":
            if data_type == "json":
                res = req_session.request(method=method, url=url, json=datas, headers=headers, cookies=cookies,
                                          **kwargs)
            else:
                res = req_session.request(method=method, url=url, params=datas, headers=headers, cookies=cookies,
                                          **kwargs)
        elif method == "put":
            pass
        elif method == "delete":
            pass
        else:
            pass
        return res

    def expectation_assert(self, expection, data):
        if "=" in expection:
            result = str(expection).split("=")
            assert data[result[0]] == result[1]
        elif "!=" in expection:
            result = str(expection).split("=")
            assert data[result[0]] != result[1]
        elif "in" in expection:
            result = str(expection).split("=")
            assert data[result[0]] in result[1]
        else:
            pass


# if __name__ == '__main__':
#     res = RequestUnit().send_request("post", "http://127.0.0.1:5000/test_post", {"num1": 1, "num2": 2},
#                                      data_type="not json")
#     # req_session = requests.session()
#     # res = req_session.request("post","http://127.0.0.1:5000/test_post",params={"num1":1,"num2":2})
#     # res = RequestUnit().send_request("get", "http://127.0.0.1:5000/test_get", {"num1": 1, "num2": 2})
#     print(res.text)
