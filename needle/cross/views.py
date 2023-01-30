from django.core.paginator import Paginator
from django.shortcuts import render

from .models import *


def index(request):
    template = "cross/index.html"
    return render(request, template)


def get_pagination(request, post_list):
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    kit_list = Kit.objects.all()
    page_obj = get_pagination(request, kit_list)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "cross/index.html", context)
