from django_filters import FilterSet
from .models import Product



class AuthorFilter(FilterSet):
       class Meta:
        model = Post
        fields = ('Author', 'zagolovok', 'date')