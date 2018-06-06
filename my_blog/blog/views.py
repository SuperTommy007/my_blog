from django.shortcuts import render
from django.http import HttpResponse
from blog.models import BlogPost
from django.core.paginator import Paginator
import markdown
# Create your views here.

def blog_index(request):
    print(request.META['REMOTE_ADDR'])
    return render(request,'blog/index.html')

def blog_list(request):
    blog_list = BlogPost.objects.all()
    paginator = Paginator(blog_list,3)

    # print(paginator.page(1)[0])
    # print(paginator.num_pages)
    return render(request, 'blog/bloglist.html', {'blog_list': paginator.page(paginator.num_pages)})

def pre(request,pk):
    blog_list = BlogPost.objects.all()
    paginator = Paginator(blog_list, 3)
    # print(dir(request.GET))
    # print(pk)
    return render(request, 'blog/bloglist.html', {'blog_list': paginator.page(pk)})

def next(request,pk):
    blog_list = BlogPost.objects.all()
    paginator = Paginator(blog_list, 3)
    # print(pk)
    return render(request, 'blog/bloglist.html', {'blog_list': paginator.page(pk)})

def blog_details(request,pk):
    print(pk)
    blogdetail = BlogPost.objects.get(pk = pk)
    blogdetail.body = markdown.markdown(blogdetail.body,
                                  extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
    return render(request, 'blog/blogdetails.html', {'c':blogdetail})
    # return HttpResponse(blogdetail.title)

def categry(request,pk):
    print(pk)
    blog_list = BlogPost.objects.filter(category_id=pk)
    print(len(blog_list))
    # paginator = Paginator(blog_list, 2)
    return render(request, 'blog/bloglist.html', {'blog_list': blog_list})


def search(request):
    return render(request,'blog/create.html')