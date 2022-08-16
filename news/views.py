from multiprocessing import context
import re
from unicodedata import category
from django.shortcuts import render
from .models import *
def index(request):
    categories = Category.objects.all()
    context = {
        'categories':categories
    }
    return render(request=request, template_name='news/index.html', context=context)
    