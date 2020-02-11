#coding=utf-8
from django.utils.deprecation import MiddlewareMixin


class Row1(MiddlewareMixin):
    def process_request(self, request):
        print("中间件R1")

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        # view_func 对应 views函数，view_func_args、kwargs 对应 views里的参数、
        print("中间件V1view")

    def process_response(self, request, response):
        print("中间件1返回")
        return response


# 参数里的 response ：就是views里面返回的值，所以要继续返回一下，否则客户端收不到数据

class Row2(MiddlewareMixin):
    def process_request(self, request):
        print("中间件R2")

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        # view_func 对应 views函数，view_func_args、kwargs 对应 views里的参数、
        print("中间件V2view")

    def process_response(self, request, response):
        print("中间件2返回")
        return response


class Row3(MiddlewareMixin):
    def process_request(self, request):
        print("中间件R3")

    def process_view(self, request, view_func, view_func_args, view_func_kwargs):
        # view_func 对应 views函数，view_func_args、kwargs 对应 views里的参数、
        print("中间件V3view")

    def process_response(self, request, response):
        print("中间件3返回")
        return response