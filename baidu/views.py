from django.shortcuts import render
import json
from rest_framework.views import APIView
from .models import address_info
from .serializers import AddSerializers
from utils import restful


# 加载首页数据
def index(request):
    address_point = address_info.objects.all()
    address_longitude = []
    address_latitude = []
    for i in range(len(address_point)):
        address_longitude.append(address_point[i].longitude)
        address_latitude.append(address_point[i].latitude)

    return render(request, 'index.html',
                  {'address_longitude': json.dumps(address_longitude),
                   'address_latitude': json.dumps(address_latitude)})


# 异步加载数据
def get_title(request):
    id = int(request.GET.get('id'))
    id += 1
    address = address_info.objects.filter(id=int(id))
    serializers = AddSerializers(address, many=True)
    data = serializers.data
    return restful.result(data=data)


# 查询地图
def search_map(request):
    all_address = address_info.objects.all()
    context = {'all_address':all_address}
    return render(request, 'search.html', context=context)


# 添加地图
def add_map(request):
    id = request.GET.get('id','1')
    all_address = address_info.objects.all()

    context = {'all_address':all_address}

    return render(request, 'add.html', context=context)


def video(request):
    return render(request, 'video.html')
