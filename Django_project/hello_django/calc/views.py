from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic.base import TemplateView
from hello_django.calc.models import History


class IndexView(View):

    def get(self, request):
        return HttpResponse('calc')


# def index(request, a, b):
#    return HttpResponse(f'{a} + {b} = {a + b}')


def home_redirect(request):
    return redirect(reverse('calc', args=[40, 2]))


class With_Context(TemplateView):

    template_name = "test.html"

    def get_context_data(self, a, b, **kwargs):
        context = super().get_context_data(**kwargs)
        sum_a_b = a + b
        context['a'] = a
        context['b'] = b
        context['c'] = sum_a_b
        History(value=sum_a_b).save()
        return context


def get_history(request):
    value = History.objects.order_by('-timestamp').all()[:10]
    return render(request, 'history.html', context={'Value': value})
