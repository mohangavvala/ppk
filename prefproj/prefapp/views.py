from django.shortcuts import render,redirect,HttpResponseRedirect
from .models import Post

# Create your views here.
def Home(request):
    return render(request,'testapp/home.html')
def Index(request):

    if request.method == 'POST':
        if request.POST.get('name') and request.POST.get('mail'):
            post = Post()
            print(type(post))
            post.name = request.POST.get('name')
            post.mail = request.POST.get('mail')
            post.mnumber = request.POST.get('mnumber')
            post.msg = request.POST.get('msg')
            post.save()
            return  HttpResponseRedirect(request.META.get('HTTP_REFERER'))
            #return render(request,'testapp/index.html')


        else:
            return render(request, 'testapp/index.html')
    return render(request,'testapp/index.html')



def Listview(request):
    post=Post.objects.all()

    return render(request,'testapp/info.html',{"post":post})

def Delete_view(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return redirect('/infolist')