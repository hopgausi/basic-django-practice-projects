from django import template
from fbv_todo.models import ToDo


register = template.Library()

@register.filter(name='icount')
def items_count(value):
    queryset = ToDo.objects.filter(completed=False)
    value = queryset
    return value.count()

@register.filter(name='ccount')
def items_count(value):
    queryset = ToDo.objects.filter(completed=True)
    value = queryset
    return value.count()



