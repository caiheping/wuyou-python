from django.http import JsonResponse
from django.core import serializers
import json

from utils.status_type import statusType


class HttpResponseJson(object):
    """统一的返回类"""
    def __init__(self, data=None, status=200, code=20000):
        self.data = data  # 数据
        self.status = status  # response的信息
        self.code = code  # 状态码

    # 返回json
    def json(self):
        if self.status == 200:
            if self.data is None:
                obj = {
                    "code": self.code,
                    "data": statusType[self.status][self.code],
                    "status": self.status
                }
                return JsonResponse(obj)
            elif isinstance(self.data, (list, dict, int, float, complex, str, tuple)):
                obj = {
                    "code": self.code,
                    "data": self.data,
                    "status": self.status
                }
                return JsonResponse(obj)
            else:
                # QuerySet 类型
                obj = {
                    "code": self.code,
                    "data": json.loads(serializers.serialize("json", self.data)),
                    "status": self.status
                }
                return JsonResponse(obj, safe=False)
        else:
            obj = {
                "code": self.code,
                "data": statusType[self.status][self.code]
            }
            data = JsonResponse(obj)
            data.status_code = self.status
            return data
