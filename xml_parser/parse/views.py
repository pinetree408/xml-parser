from django.shortcuts import render
from django.views.generic import TemplateView
import parse
from django.conf import settings


class IndexView(TemplateView):
    template_name = "parse/index.html"

    def get_context_data(self,  **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['result'] = parse.parser(settings.BASE_DIR + "/vasprun.xml")

        return context
