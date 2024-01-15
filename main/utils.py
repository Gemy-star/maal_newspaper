# -*- coding: utf-8 -*-
from django.conf import settings
from django.http import HttpRequest

from main.models import NewsContent


def get_news_letter_news(request: HttpRequest) -> dict:
    ctx = {
        "news": NewsContent.objects.all().order_by("-pk")[:1],
    }
    return ctx
