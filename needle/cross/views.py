from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
import pandas as pd


def get_pagination(request, post_list):
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


def index(request):
    kits = Kit.objects.all()
    page_obj = get_pagination(request, kits)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "cross/index.html", context)


def kit_detail(request, slug):
    kit = get_object_or_404(Kit, slug=slug)
    context = {
        "kit": kit,
    }
    return render(request, "cross/kit_detail.html", context)


def kit_list(request):
    kit = Kit.objects.all()
    page_obj = get_pagination(request, kit)
    context = {
        "kit": kit,
        "page_obj": page_obj,
    }
    return render(request, "cross/kit_list.html", context)


def profile(request, username):
    p = list(Progress.objects.select_related())
    p = p[0].kit.total_crosses
    # progress = Progress.objects.select_related("embroiderer")
    # my_kit = Kit.objects.select_related("progress")
    # kit = Progress.objects.filter(id=1).select_related()
    # total = kit.total_crosses
    # print(f'kit is {kit}, total crosses: {total}')
    print(
        "################################################################################################"
    )
    print(p)
    context = {
        "progress": p,
    }
    return render(request, "cross/profile.html", context)
