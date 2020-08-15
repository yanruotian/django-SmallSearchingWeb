from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def hello(request):
    content={'hello': 'Hello World!'}
    return render(request, 'HelloWorld.html', content)

'''
def the_first_page(request):
    return HttpResponse("<h1><center>First Page</center></h1>")
'''

def the_first_page(request):
    return render(request, 'TheFirstPage.html', {})


def echo(request, string):
    return HttpResponse('<p><center>'+string+'</center></p>')

'''
def echo_introduce(request):
    content='<h1><center>Echo Introduce</center></h1>\
        <p><center>To use echo, turn to echo/your_html_string</center></p>'
    return HttpResponse(content)
'''

def echo_introduce(request):
    return render(request, 'Echo.html', {})


def echo_test(request):
    print(request.GET['echo_string'])
    return redirect('/test/echo')


def search_test(request):
    return render(request, 'Search.html', {})


def searching_test(request):
    print('用户要搜索 '+request.GET['search_string'])
    return redirect('/test/search')


def post_test(request):
    changer={}
    if request.method=='POST':
        changer['search_result']=request.POST['search_string']
    return render(request, 'PostSearch.html', changer)


def a():
    pass
