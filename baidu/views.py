from django.shortcuts import render
import json
from .models import address_info
from .serializers import AddSerializers
from utils import restful


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
def title(request):
    id = request.GET.get('id')
    address = address_info.objects.get(id=id)
    serializers = AddSerializers(address, many=True)
    data = serializers.data
    return restful.result(data=data)
