from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect

from .models import *
from .forms import *
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


def kit_create(request):
    form = KitForm(request.POST or None)
    if form.is_valid():
        kit = form.save(commit=False)
        kit.creator = request.user
        kit.save()
        return redirect("cross:kit_list")
    return render(request, "cross/create_kit.html", {"form": form})


def kit_edit(request, kit_id):
    kit = get_object_or_404(Kit, id=kit_id)
    form = KitForm(request.POST or None, instance=kit)
    if request.user != kit.creator:
        return redirect("cross:kit_detail", kit_id)
    if form.is_valid():
        form.save()
        return redirect("cross:kit_detail", kit_id)
    return render(
        request,
        "posts/create_post.html",
        {
            "form": form,
            "kit_id": kit_id,
        },
    )


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
    embroiderer = get_object_or_404(User, username=username)
    project_list = embroiderer.project.select_related("embroiderer")
    page_obj = get_pagination(request, project_list)

    context = {
        "embroiderer": embroiderer,
        "page_obj": page_obj,
    }
    return render(request, "cross/profile.html", context)
