import grequests, requests

res = requests.post("http://dev.hotkidclub.com/api/member/registerOrLogin.ctrl",
                    json={
                        "mobileNumber": 13010000011,
                        "validationCode": "1234",
                        "channel": "MOBILE",
                        "platform": "WEB",
                        "campaign": "MEMBER"
                    })

header = res.cookies.get_dict()
print(header,res)

req_list = [
    grequests.post('https://dev.hotkidclub.com/api/cpn/nationalDay/firstLogin.ctrl',
                   json={
                       "channel": "HKCH5",
                       "platform": "WEB"
                   }, cookies=header) for i in range(5)]


res_list = grequests.map(req_list)  # 并行发送，等最后一个运行完后返回
print(res_list[0].status_code, res_list[0].text)
print(res_list[1].text)
print(res_list[2].text)
print(res_list[3].text)
print(res_list[4].text)

