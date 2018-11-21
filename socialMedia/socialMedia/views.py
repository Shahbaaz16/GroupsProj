from django.views.generic import TemplateView
from django.urls import reverse
from django.http import HttpResponseRedirect

class Testpage(TemplateView):
    template_name = 'test.html'

class ThanksPage(TemplateView):
    template_name = 'thanks.html'

class Homepage(TemplateView):
    template_name = 'index.html'
