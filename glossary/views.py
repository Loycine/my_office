from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import Category, Phrase

def add_category(request):
    if(request.method == 'POST'):
        category_name = request.POST['category']
        category = Category.objects.create()
        category.category_text = category_name
        category.save()
    return redirect('index')

def del_category(request):
    if request.method == "GET":
        category_id = request.GET.get('id', None)
        Category.objects.filter(id=category_id).delete()
    return redirect('index')

def modify_category(request):
    pass

def add_phrase(request, category_id):
    if(request.method == 'POST'):
        category = Category.objects.get(id = category_id)

        phrase = Phrase.objects.create(Category_id = category_id)
        phrase.phrase_text = request.POST['phrase_text']
        phrase.explanation = request.POST['explanation']
        phrase.save()

    return redirect('category_detail', category_id)


def del_phrase(request, category_id):
    if(request.method == 'GET'):
        phrase_id = request.GET.get('id', None)
        Phrase.objects.filter(id = phrase_id).delete()

    return redirect('category_detail', category_id)


def category_detail(request, category_id):
    category = Category.objects.get(id = category_id)
    phrase_list = category.phrase.all()
    category_list = Category.objects.all()

    context = {
        'category_list': category_list,
        'phrase_list'  : phrase_list,
        'category_id'  : category_id,
    }

    return render(request, 'glossary/detail.html', context)

def index(request):
    category_list = Category.objects.all()
    context = {
        'category_list': category_list,
    }
    return render(request, 'glossary/index.html', context)