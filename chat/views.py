from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from app.models import *
from chat.models import *
from django.http import HttpResponse


# Create your views here.
def chatre(request, id):
    product_detail = ""
    vl = ""
    p_id = request.GET.get('p_id')
    # value = request.COOKIES['product_id']
    usr = request.user.id
    uid = usr
    nam = ""
    if p_id:
        product_detail = product.objects.get(id=p_id)
    else:
        vl = request.COOKIES['product_id']
        product_detail = product.objects.get(id=vl)
    nm = User.objects.filter(id=id)
    for q in nm:
        nam = q.username
    res = chat.objects.filter(doc=id, pa=usr)
    ob = User.objects.filter(is_staff=True)
    response = render(request, 'chatr/chat_app.html',
                      {'re': ob, 'res': res, 'nm': nam, 'sn': usr, 'reo': id, 'product_detail': product_detail,'pro_id':p_id})
    response.set_cookie('product_id', p_id, max_age=300000)
    return response


def receive_data(request, pid, uid):
    print('uid={} pid={}'.format(uid, pid))
    a = chat.objects.filter(doc=uid, pa=pid, to=1).last()
    if not a:
        data = {'chat': "", 'id': 1, 'tm': ""}
    else:

        chat.objects.filter(doc=pid, pa=uid).update(sts=True)
        data = {'chat': a.sub, 'id': a.id, 'tm': a.create_at}
    return JsonResponse(data)


def com(request):
    receiver = request.POST.get('receiver')
    print('sssssssssssss{}'.format(receiver))
    sndd = request.POST.get('sendr')
    chatt = request.POST.get('msg')
    product_id = request.POST.get('p_id')
    chat.objects.create(doc_id=receiver, pa_id=sndd, sub=chatt, to=0, product_id=product_id)
    return JsonResponse('hit', safe=False)


def chatrea(request, id):
    usr = request.user.id
    uid = id
    nm = User.objects.filter(id=id)
    for q in nm:
        nam = q.username
    res = chat.objects.filter(doc=usr, pa=uid)
    product_d = chat.objects.filter(doc=usr, pa=uid, to=0).last()
    ob = User.objects.filter(is_staff=False)
    return render(request, 'chat/chata.html', {'re': ob, 'res': res, 'nm': nam, 'sn': usr, 'reo': uid, 'pd': product_d})


def receive_dataa(request, pid, uid):
    print('uid={} pid={}'.format(uid, pid))
    a = chat.objects.filter(doc=pid, pa=uid, to=0).last()
    if not a:
        data = {'chat': "", 'id': 1, 'tm': ""}
    else:

        chat.objects.filter(doc=pid, pa=uid).update(sts=True)
        data = {'chat': a.sub, 'id': a.id, 'tm': a.create_at}
    return JsonResponse(data)


def coma(request):
    print("hid docntorfffffffffffffffff")
    receiver = request.POST.get('receiver')
    print('sssssssssssss{}'.format(receiver))
    sndd = request.POST.get('sendr')
    chatt = request.POST.get('msg')
    chat.objects.create(doc_id=sndd, pa_id=receiver, sub=chatt, to=1)

    return JsonResponse('hit', safe=False)


def send_emails(request):
    subject = f'hello Admin some new messages from {request.user.username}.'
    message = f'Hi {request.user.username}, thank you for registering in geeksforgeeks.'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['saadashraf721@gmail.com']
    send_mail(subject, message, email_from, recipient_list)
