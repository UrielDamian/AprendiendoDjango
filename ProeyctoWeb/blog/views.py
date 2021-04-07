from django.shortcuts import render
from blog.models import Post,Categoria

# Create your views here.
def blog(request):
    post = Post.objects.all()    
    return render(request,"blog/blog.html", {'Posts':post})

def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    post = Post.objects.filter(categorias = categoria)  
    return render(request,"blog/categorias.html",{"categoria":categoria,'Posts':post})
    