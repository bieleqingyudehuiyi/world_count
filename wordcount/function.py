#from django.http import HttpResponse
from django.shortcuts import render  # 传递网页给用户


def home(request):
    return render(request, 'home.html')


def count(request):
    user_text = request.GET['text']
    total_count = len(user_text)  # text 为文本名字

    world_dict = {}

    for world in user_text:
        if world not in world_dict:
            world_dict[world] = 1
        else:
            world_dict[world] += 1

    sorted_dict = sorted(world_dict.items(), key=lambda w:w[1], reverse=True)
    #items将(键：值)变成[键，值]，定义一个w[]列表，取w[1],就是列表里面第二个数，即字典里面的值
    return render(request, 'count.html',
    {'count': total_count,'text':user_text,
    'worldict':world_dict,'sorted':sorted_dict})  # 通过字典将total_count 传递给html


def about(request):
    return render(request, 'about.html')