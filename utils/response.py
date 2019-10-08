from django.http import JsonResponse
from django.core import serializers
import json


class HandleResponse(object):
    """统一的返回类"""
    def __init__(self, data, message='success', code=10000):
        self.data = data  # 数据
        self.message = message  # response的信息
        self.code = code  # 状态码

    # 返回json
    def response_json(self):
        if isinstance(self.data, (list, dict, int, float, complex, str, tuple)):
            obj = {
                "code": self.code,
                "data": self.data,
                "message": self.message
            }
            return JsonResponse(obj)
        else:
            # QuerySet 类型
            obj = {
                "code": self.code,
                "data": json.loads(serializers.serialize("json", self.data)),
                "message": self.message
            }
            return JsonResponse(obj, safe=False)
