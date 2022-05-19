from django.urls import path
from hello_django.calc import views


urlpatterns = [
    path('', views.home_redirect),
    path(
        '<int:a>/<int:b>',
        views.With_Context.as_view(template_name='test.html'),
        name='calc',
    ),
    path('history', views.get_history),
]
