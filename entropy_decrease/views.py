from django.shortcuts import render
from entropy_decrease.src import random_num
from django.http import JsonResponse
from . import models  # 导入Item模型
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from django.contrib.auth import authenticate

@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_custom_view(request):
    data = {'message': 'This is my custom API endpoint.'}
    return JsonResponse(data)

def random_number_view(request):
    generator = random_num.RandomNumberGenerator()
    random_number = generator.generate_random_number()

    score = models.Score.objects.get(owner_id=1)
    original_score = score.total_score
    score.total_score += random_number
    score.save()

    data = {'random_number': random_number,"original_score":original_score,"total_score":score.total_score}
    return JsonResponse(data)

def test_db_view(request):

    # 创建新的Item记录
    new_item = models.Item(name='Example Item', description='This is an example item', price=19.99)
    new_item.save()

    score = models.Score(total_score=1,owner_id=1)
    score.save()

    # 查询数据库中的Item记录
    items = models.Item.objects.all()  # 获取所有Item记录
    filtered_items = models.Item.objects.filter(price__gte=10)  # 获取价格大于等于10的Item记录

    # 更新Item记录
    item_to_update = models.Item.objects.get(id=1)  # 假设要更新ID为1的记录
    item_to_update.name = 'Updated Item Name'
    item_to_update.save()

    # 删除Item记录
    # item_to_delete = models.Item.objects.get(id=2)  # 假设要删除ID为2的记录
    # item_to_delete.delete()
    data = {'message': "okay"}
    return JsonResponse(data)



@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username,password)
    try:
        user = models.User.objects.get(username=username,password=password)
    except models.User.DoesNotExist:
        user = None

    if user is not None:
        from django.contrib.auth.models import User
        user = User.objects.create_user(username="test2", password="test2")
        token, created = Token.objects.get_or_create(user=user)
        return Response({'message': 'Login successful', 'token': token.key, 'user_id': user.id})
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)


