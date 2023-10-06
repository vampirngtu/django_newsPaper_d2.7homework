from django.urls import path
from .views import IndexView

app_name = 'accounts'
urlpatterns = [
    path('', IndexView.as_view(template_name='accounts/base.html', name='accounts'),
    ]