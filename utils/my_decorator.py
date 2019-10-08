from utils.response import HandleResponse


class MyDecorator:
    def __init__(self, func):
        self.func = func

    def is_login(self):
        """是否登录"""
        def wrapper(request, *args, **kwargs):
            print('自定义装饰器被调用了')
            user = request.user
            if not user.is_authenticated:
                # 用户未登录
                return HandleResponse({}, '未登录', 20000).response_json()
            return self.func(request, *args, **kwargs)

        return wrapper
