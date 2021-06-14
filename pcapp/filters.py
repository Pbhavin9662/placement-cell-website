import django_filters
from .models import *


class studentlistfilters(django_filters.FilterSet):
    class Meta:
        model = Selected_Students
        fields = '__all__'


