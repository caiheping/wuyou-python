from django.http import JsonResponse


class HandleResponse(object):
    """统一的返回类"""
    def __init__(self, data, message='success', code=0):
        self.data = data    # 数据
        self.message = message  # response的信息
        self.code = code    # 状态码

    def response_json(self):
        obj = {
            'code': self.code,
            'data': self.data,
            'message': self.message
        }
        return JsonResponse(obj)
