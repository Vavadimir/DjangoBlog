from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from .models import Posts, Comments


def index(request):
    q = Posts.objects.all()
    try:
        title = request.POST['title']
        text = request.POST['post_text']
    except:
        if request.user.is_authenticated():
            return render(request, 'blog/index.html', {'posts': q, "logged": 1})
        else:
            return render(request, 'blog/index.html', {'posts': q})
    else:
        print('yes')
        post = Posts(pub_date=timezone.now(), post_text=text, post_title=title)
        Posts.save(post)
        if request.user.is_authenticated():
            return render(request, 'blog/index.html', {'posts': q, "logged": 1})
        else:
            return render(request, 'blog/index.html', {'posts': q})
    # else:
    #     return redirect('login')

def login(request):
    try:
        name = request.POST['name']
        passw = request.POST['passw']
    except:
        if request.user.is_authenticated():
            return redirect('index')
        else:
            return render(request, 'blog/login.html')
    else:
        user = authenticate(username=name, password=passw)
        if user is not None:
            auth_login(request, user)
            return redirect('index')
        else:
            if name in User.objects.all().values_list('username', flat=True):
                return render(request, 'blog/login.html', {"error_message": "Bad password"})
            else:
                user = User.objects.create_user(username=name, password=passw)
                user = authenticate(username=name, password=passw)
                auth_login(request, user)
                return redirect('index')

def postpage(request, post_id):
    q = Posts.objects.all()
    #itel = None
    for el in q:
        if int(el.post_id) == int(post_id):
            break
    cms = el.comments_set.all()
    if request.user.is_authenticated():
        return render(request, 'blog/postpage.html', {'post': el, 'comment': cms, "logged": 1})
    else:
        return render(request, 'blog/postpage.html', {'post': el, 'comment': cms})

def postproc(request):
    if request.POST:
        print(request.POST["comm"])
        print(request.POST["path"])
        cmnt = request.POST["comm"]
        nmb = request.POST["path"]
        posts = Posts.objects.all()
        for el in posts:
            if int(el.post_id) == int(nmb):
                break
        cmt = Comments(author=request.user, post=el, pub_date=timezone.now(), comment=cmnt)
        Comments.save(cmt)
        return HttpResponse("gg")


def comments(request):
    if request.POST:
        post_id = request.POST["path"]
        q = Posts.objects.all()
        for el in q:
            if int(el.post_id) == int(post_id):
                break
        cms = el.comments_set.all()
        return render(request, 'blog/comments.html', {'comment': cms})


def logout_us(request):
    logout(request)
    return redirect('index')