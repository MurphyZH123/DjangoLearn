"""
封装请求，当前只封装了get和post请求
"""
import requests
import json


class HandleRequests:
    """
    封装requests类
    """

    def __init__(self) -> object:
        """
        定义一个session的参数
        """
        self.session = requests.Session()

    def visit(self, url, method="post", data=None, is_json=False, headers=None, files=None, **kwargs) -> object:
        """
        向服务器发起请求
        :rtype: object
        :param headers:请求头信息
        :param url: 请求的地址
        :param method: 请求的方式
        :param data: 请求的参数
        :param is_json: 是否为json字符串格式
        :return res:返回响应内容
        """
        # 如果数据为str格式的字符串，则转换为json
        if isinstance(data, str):
            try:
                data = json.load(data)
            except Exception:
                data = eval(data)

        # 请求方式为全部小写字母
        method = method.lower()

        # 处理请求方式为get的情况
        if method == "get":
            res = self.session.get(url, params=data, headers=headers, files=files)
        # 处理请求方式为post的情况
        elif method == "post":
            # 如果is_json为True，那么以json形式传参
            if is_json:
                res = self.session.post(url, json=data, headers=headers, files=files)
            # 如果is_json为False，那么以www-from表单形式传参
            else:
                res = self.session.post(url, data=data, headers=headers, files=files)
        else:
            print("不支持除了【{}】以外的请求方式".format(method))

        return res

    def close(self):
        """
        关闭请求链接
        :return:
        """
        self.session.close()


if __name__ == "__main__":
    req = HandleRequests()
    payload = {
        "employeeId": "00326431",
        "plaintext": "cruley@5"
    }
    header = {"content-type": "application/json"}
    res = req.visit("http://dev.hotkidclub.com/api-admin/member_backend/login.ctrl", "post", data=payload, is_json=True,
                    headers=header)
    print(res.json())
