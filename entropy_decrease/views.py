from django.shortcuts import render
from entropy_decrease.src import random_num
from django.http import JsonResponse
import random
from . import models  # 导入Item模型
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework import status


@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def my_custom_view(request):
    data = {'message': 'This is my custom API endpoint.'}
    return JsonResponse(data)

@api_view(['PUT'])
def total_score_view(request):
    userid = request.data.get('userid')
    tag = request.data.get('tag','increase')
    score = models.Score.objects.get(owner_id=userid)
    random_number = random.randint(score.min, score.max)
    original_score = score.total_score
    if(tag == 'increase'):
        score.total_score += random_number
    else:
        score.total_score -= random_number
    score.save()
    data = {'random_number': random_number,"original_score":original_score,"total_score":score.total_score,"min":score.min,"max":score.max}
    return JsonResponse(data)

@api_view(['PUT'])
def cost_total_score_view(request):
    userid = request.data.get('userid')
    cost = int(request.data.get('cost'))
    score = models.Score.objects.get(owner_id=userid)
    original_score = score.total_score
    score.total_score -= cost
    score.save()
    data = {'cost': cost,"original_score":original_score,"total_score":score.total_score}
    return JsonResponse(data)

@api_view(['PUT'])
def target_score_view(request):
    userid = request.data.get('userid')
    target_score = request.data.get('target_score')
    score = models.Score.objects.get(owner_id=userid)
    score.target_score = target_score
    return JsonResponse({"target_score":score.target_score})

@api_view(['GET'])
def score_view(request):
    userid = request.data.get('userid')
    print(userid)
    score = models.Score.objects.get(owner_id=userid) 
    return JsonResponse({"total_score":score.total_score,"target_score":score.target_score})

@api_view(['POST'])
def range_view(request):
    userid = request.data.get('userid')
    min = request.data.get('min')
    max = request.data.get('max')
    score = models.Score.objects.get(owner_id=userid) 
    score.min = min
    score.max = max
    score.save()
    return JsonResponse({"min":score.min,"max":score.max})

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
        # from django.contrib.auth.models import User
        # user1 = User.objects.create_user(username=user.username, password=user.password)
        # token, created = Token.objects.get_or_create(user=user1)
        return Response({'message': 'Login successful', 'token': "jwt_token", 'user_id': user.id,"code":0})
    else:
        return Response({'error': 'Invalid username or password',"code":1}, status=status.HTTP_400_BAD_REQUEST)


