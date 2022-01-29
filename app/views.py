from django.contrib.auth import login as abc, authenticate, logout as deff
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from chat.views import *
from .models import *
from django.db.models import Q


def chat(request):
    return render(request, 'chat/chat.html')


def search(request):
    query = request.GET.get('q')
    menu_list = menu.objects.filter(sts=True)
    product_list = product.objects.filter(Q(sts=True) & Q(title__icontains=query) | Q(desc__icontains=query))
    context = {'product': product_list, 'menu': menu_list}
    return render(request, 'search.html', context)


def index(request):
    menu_list = menu.objects.filter(sts=True)
    product_list = product.objects.filter(sts=True)

    return render(request, 'index.html', {'product': product_list, 'menu': menu_list})


def login(request):
    menu_list = menu.objects.filter(sts=True)
    if (request.method == 'POST'):
        uname = request.POST['username']
        pwd = request.POST['password']
        auth = authenticate(username=uname, password=pwd)
        if auth is not None:
            abc(request, auth)
            return redirect('/')
    return render(request, 'login.html', {'menu': menu_list})


def register(request):
    menu_list = menu.objects.filter(sts=True)
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        create = User(first_name=first_name, last_name=last_name, email=email, username=username,
                      password=make_password(password))
        create.save()
        if create:
            return redirect('/')
    return render(request, 'register.html', {'menu': menu_list})


def logout(request):
    deff(request)
    return redirect('/')


def product_detail(request, id):
    menu_list = menu.objects.filter(sts=True)
    products = product.objects.get(id=id)
    product_images = productImage.objects.filter(product_id=id)
    viewer = count.objects.filter(product_id=id)
    if not viewer:
        new_viewer = count(product_id=id, viewers=1)
        new_viewer.save()
    for i in viewer:
        total_viewer = i.viewers
        total_viewer += 1
        viewer.update(viewers=total_viewer)
    product_list = product.objects.filter(sts=True).order_by("?")
    return render(request, 'product-detail.html',
                  {'product': products, 'product_list': product_list, 'menu': menu_list,
                   'product_images': product_images})


def products(request, id):
    menu_list = menu.objects.filter(sts=True)
    category_list = category.objects.filter(sts=True)
    product_list = product.objects.filter(sts=True,menu_id=id)
    find = ""
    if request.method == 'POST':
        get_category = request.POST['category']
        get_price = request.POST['price']
        get_price_range = get_price.split(" - ")
        get_min_price = get_price_range[0]
        get_max_price = get_price_range[1]
        find = product.objects.filter(sts=True, category_id=get_category,
                                      price__range=[get_min_price, get_max_price])
        return render(request, 'products.html', {'products': find, 'caty': category_list,'menu': menu_list,})
    return render(request, 'products.html',
                  {'product': product_list, 'menu': menu_list, 'caty': category_list, 'products': find})


def E404(request):
    menu_list = menu.objects.filter(sts=True)
    return render(request, '404.html', {'menu': menu_list})


@login_required(login_url='/login/')
def wishlists(request):
    menu_list = menu.objects.filter(sts=True)
    wishlists_list = wishlist.objects.filter(user=request.user.id)
    return render(request, 'wishlist.html', {'wishlist': wishlists_list, 'menu': menu_list})


@login_required(login_url='/login/')
def addwishlist(request, sid):
    user_idd = request.user.id
    product_ids = sid
    exist = wishlist.objects.filter(user_id=user_idd, product_id=product_ids)
    if exist:
        return redirect('/wishlist/')
    else:
        creates = wishlist(user_id=user_idd, product_id=product_ids)
        creates.save()
        if creates:
            return redirect('/wishlist/')
        else:
            return redirect('/wishlist/')


@login_required(login_url='/login/')
def deletewishlist(request, ssid):
    dele = wishlist.objects.filter(product_id=ssid)
    dele.delete()
    return redirect('/wishlist/')


def entry_not_found(request, exception):
    menu_list = menu.objects.filter(sts=True)
    return render(request, '404.html', {'menu': menu_list})
