from django.shortcuts import render,redirect
from .models import postIt
# Create your views here.
def blog(request):
    post_list = postIt.objects.all()
    if request.method=='POST':
        id = request.POST.get('id')
        postIt.objects.get(id=id).delete()

    return render(request, 'blog.html', {'post_list': post_list})

def post(request):
    if request.method =='POST':
        title =request.POST.get('title')
        content = request.POST.get('content')
        postIt.objects.create(title=title,content=content)
        return redirect('/blog')#回去上一頁
    return render(request,'post.html')

def edit(request):
    id = request.GET.get('q')
    editPost = postIt.objects.get(id=id)
    if request.method=='POST':
        editPost.title= request.POST.get('title')
        editPost.content = request.POST.get('content')
        editPost.save()
        return redirect('/blog')
    return render(request, 'edit.html', {'post': editPost})