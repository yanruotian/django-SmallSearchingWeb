from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Articles
import random
 

def GBK2312():
    head = random.randint(0xb0, 0xf7)
    body = random.randint(0xa1, 0xfe)
    val = f'{head:x}{body:x}'
    return bytes.fromhex(val).decode('gbk')


def Unicode():
    val = random.randint(0x4e00, 0x9fbf)
    return chr(val)


def random_article(min:int, max:int):
    str = ""
    for _ in range(random.randint(min, max)):
        str += Unicode()
    return str

# Create your views here.

def index(request):
    init_articles(500)
    '''
    for article in Articles.objects.all()[:6]:
        print(article.id, article)
    '''
    if request.method=='GET':
        print('GET...')
        return render(request, 'index.html', {'placeholder':''})
    elif request.method=='POST':
        print('POST...')
        # print(request.POST)
        user = request.user
        print('user:', user)
        if not user in User.objects.all():
            return render(request, 'index.html', {'placeholder':'请先点击左上角用户头像进行登录或注册！'})
        search_string = request.POST['search_string']
        if search_string=='':
            return redirect(reverse('home:home'), permanent=True)
        content = []
        count = 0
        for article in Articles.objects.all():
            if search_string in article.content:
                count += 1
                content.append({'id':article.id, 'content':article.show(150)})
                if count >= 4:
                    break
        return render(
            request,
            'SearchPage.html', 
            {'placeholder': '直接回车可以回到主界面哦', 'value': search_string, 'content': content}
        )


def login(request):
    if request.method=='GET':
        print(request.user)
        if request.user in User.objects.all():
            return render(request, 'Login.html', {'placeholder':'', 'login':request.user})
        return render(request, 'Login.html', {'placeholder':'', 'login':False})
    elif request.method=='POST':
        name = request.POST['logname']
        passwd = request.POST['logpasswd']
        print('login:')
        print('name:', name, ', password:', passwd)
        try:
            user = User(username=name)
            user.set_password(passwd)
            user.save()
            auth.login(request, user)
            return redirect(reverse('home:home'))
        except:
            try:
                user = auth.authenticate(username=name, password=passwd)
                auth.login(request, user)
                return redirect(reverse('home:home'))
            except:
                return render(request, 'Login.html', {'placeholder':'用户名已存在，且密码不符', 'login':False})


@login_required
def logout(request):
    auth.logout(request)
    return redirect(reverse('home:home'))


def delete_articles():
    while Articles.objects.all():
        Articles.objects.all().delete()


def init_articles(num:int):
    num_before = len(Articles.objects.all())
    if num_before >= num:
        return
    for _ in range(num - num_before):
        Articles.objects.create(
            content=random_article(5, 1000)
        )


@login_required
def show_by_id(request, id):
    print(id, type(id), request.method)
    try:
        id = int(id)
    except:
        return redirect(reverse('home:home'), permanent=False)
    if request.method=='GET':
        try:
            content = Articles.objects.get(id=id).content
        except:
            return redirect(reverse('home:home'), permanent=False)
        return render(request, 'Details.html', {'content':content, 'value':request.GET['search_string'], 'placeholder':'直接回车可以回到主界面哦'})
    elif request.method=='POST':
        return redirect(reverse('home:home'), permanent=False)
