from django.shortcuts import render,HttpResponse
from app01.models import aigroup
from django.core import serializers
import json
from django.http import JsonResponse

# from app01.models import DKT
# Create your views here.
def index(request):
    data_list=aigroup.objects.all()
    data_list1=aigroup.objects.filter(kind='数与代数')
    data_list2 = aigroup.objects.filter(kind='图形与几何')
    data_list3 = aigroup.objects.filter(kind='统计与概率')
    data_list4 = aigroup.objects.filter(kind='量与计算')
    data_list5 = aigroup.objects.filter(kind='逻辑与思维训练')
    data_list6 = aigroup.objects.filter(kind='综合与实践')
    return render(request,"index.html",{"data_list":data_list,"data_list1":data_list1,"data_list2":data_list2,"data_list3":data_list3,"data_list4":data_list4,"data_list5":data_list5,"data_list6":data_list6})

def update_aigroup_percent(request):
    if request.method == 'POST':
        # 更新kind为"语法"的记录的percent为0.28
        updated_count = aigroup.objects.filter(kind='语法').update(percent=0.28)
        aigroup.objects.filter(kind='数据结构').update(percent=0.08)
        if updated_count > 0:
            return JsonResponse({'status': 'success', 'message': '更新成功'})
        else:
            return JsonResponse({'status': 'error', 'message': '未找到符合条件的记录'}, status=404)
    return JsonResponse({'status': 'error', 'message': '仅支持POST请求'}, status=405)

def user_list(request):
    # 去app目录下的templates目录中找user_list.html(根据app的注册顺序，逐一去他们的templates目录中找）
    return render(request,"user_list.html")

def user_add(request):
    return HttpResponse("添加用户")

def tpl(request):
    name="wzd"
    list=["cyt","wzd"]
    return render(request,'tpl.html',{"n1":name,"list":list})

def test(request):
    print(request.GET)
    return HttpResponse("终于成功啦！")

def login(request):
    if request.method == "GET":
        return render(request,"login.html")
    else:
        data_list=aigroup.objects.all()
        data_list1=aigroup.objects.filter(kind='数与代数')
        data_list2 = aigroup.objects.filter(kind='图形与几何')
        data_list3 = aigroup.objects.filter(kind='统计与概率')
        data_list4 = aigroup.objects.filter(kind='量与计算')
        data_list5 = aigroup.objects.filter(kind='逻辑与思维训练')
        data_list6 = aigroup.objects.filter(kind='综合与实践')
        return render(request,"index.html",{"data_list":data_list,"data_list1":data_list1,"data_list2":data_list2,"data_list3":data_list3,"data_list4":data_list4,"data_list5":data_list5,"data_list6":data_list6})


def challenge_detail(request, item_id):
    item = aigroup.objects.get(id=item_id)
    # 将 item 模型实例转换为字典（提取需要的字段）
    item_dict = {
        'id': item.id,
        'name': item.name,
        'kind':item.kind,
        'content': item.content,
        'analysis': item.analysis,
        # 其他需要的字段（如 answer）
        'answer': item.answer  # 假设模型有 answer 字段
    }
    # 序列化为 JSON 字符串
    item_json = json.dumps(item_dict)
    # 同时确保 data_json 正确序列化（之前的逻辑）
    data_list = list(aigroup.objects.all().values('id', 'name', 'content', 'analysis', 'answer'))
    data_json = json.dumps(data_list)
    return render(request, 'challenge_detail.html', {
        'item_json': item_json,  # 传递 JSON 字符串
        'data_json': data_json
    })
    

# ... existing code ...
# from .models import DKT
# import torch
#
#
# def dkt_prediction(request):
#     # 初始化模型参数（与原代码一致，模型支持任意batch_size）
#     concept_num = 100  # 知识点总数
#     hidden_dim = 200  # 隐藏层维度
#     feature_dim = 2  # 输入特征维度(正确/错误二分类)
#     output_dim = 100  # 输出维度(知识点数量)
#     dropout = 0.5  # Dropout概率
#     bias = True  # 是否使用偏置
#
#     # 创建模型实例（参数无需修改，模型支持动态batch_size）
#     model = DKT(
#         feature_dim=feature_dim,
#         hidden_dim=hidden_dim,
#         output_dim=output_dim,
#         dropout=dropout,
#         bias=bias
#     )
#
#     # 准备输入数据（调整为单个学生）
#     # 1. xt - 当前回答结果(0=错误,1=正确)，单个学生的1个时间步数据
#     values = [0,1]  # 单个学生当前问题回答错误（长度1）
#     xt = torch.tensor(values, dtype=torch.long).unsqueeze(0)  # 形状 [1, 1]（batch_size=1，时间步=1）
#
#     # 2. qt - 当前问题对应的知识点编号，单个学生的1个时间步数据
#     values2 = [5,12]  # 单个学生当前回答的是第5个知识点的问题（长度1）
#     qt = torch.tensor(values2, dtype=torch.long).unsqueeze(0)  # 形状 [1, 1]（batch_size=1，时间步=1）
#
#     # 进行预测（输出形状会根据时间步调整）
#     with torch.no_grad():
#         pred_res = model(xt, qt)  # 若时间步=1，输出形状为 [1, 0]（无预测结果）；建议时间步≥2以生成有效预测
#
#     # 返回响应（示例调整为时间步=2的情况）
#     # 若需有效预测，可将xt/qt调整为时间步=2（例如xt=[0,1], qt=[5,12]），输出形状为 [1, 1]
#     return HttpResponse(f"Prediction result shape: {pred_res.shape}, values: {pred_res.tolist()}")

# ... existing code ...