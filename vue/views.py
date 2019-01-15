from django.shortcuts import render
from django.http import JsonResponse
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BaseAuthentication
from rest_framework.request import Request
from rest_framework import exceptions


def index(request):
    result = {
        'id':1,
        'name':'baidu'
    }
    return JsonResponse(result,status=200)


class TestView(APIView):
    def dispatch(self, request, *args, **kwargs):
        print('dispatch')
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        return Response('get ok')


token_list = [
    'sfsfss123kuf3j123',
    'asijnfowerkkf9812',
]


class TestAuthentication(BaseAuthentication):
    def authenticate(self, request):
        val = request.query_params.get('token')
        if val not in token_list:
            raise exceptions.AuthenticationFailed('用户认证失败.')
        return ('登录用户','用户token')

    def authenticate_header(self, request):
        pass


class TestAuthView(APIView):
    authentication_classes = [TestAuthentication,]
    permission_classes = []

    def get(self,request,*args,**kwargs):
        print('ok')
        return Request('GET ok')