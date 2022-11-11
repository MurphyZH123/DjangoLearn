import json
import os
import sys

sys.path.append("..")


# 使用数据驱动的方式读取json文件
class DDTHandler:
    def __init__(self, file):
        self.file = file

    def open_json(self, encoding='utf8'):
        json_data_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), self.file)
        json_data_value = json.load(open(json_data_path, encoding=encoding))
        test_json_data = []
        for key, value in json_data_value.items():
            test_json_data.append((key, value))
        return test_json_data


if __name__ == '__main__':
    json_data = DDTHandler(file="test_data/test_coupon/test_create_coupon.json")
    data = json_data.open_json()
    print(data)
