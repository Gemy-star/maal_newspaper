from django.shortcuts import render
from django.views.generic import TemplateView
from .models import NewsContent
from typing import Any


# Create your views here.
class HomePageView(TemplateView):
    template_name = "pages/home.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["last_news"] = NewsContent.objects.all().order_by("-pk")[:5]
        context["hot_new"] = NewsContent.objects.all().order_by("-pk").first()
        return context
