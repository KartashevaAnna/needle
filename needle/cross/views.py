from django.shortcuts import render

# Create your views here.


def index(request):
    template = "cross/index.html"
    return render(request, template)


from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.cache import cache_page
from django.db.models import Q

from .forms import KitForm, ProjectForm, ProgressForm
from .models import User, Progress, Kit


def get_pagination(request, post_list):
    paginator = Paginator(post_list, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return page_obj


# @cache_page(20, key_prefix='index_page')
def index(request):
    kit_list = Kit.objects.all()
    page_obj = get_pagination(request, kit_list)
    context = {
        "page_obj": page_obj,
    }
    return render(request, "cross/index.html", context)
