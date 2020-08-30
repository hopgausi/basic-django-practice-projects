from django.urls import path
from . import views

app_name = 'todo'
urlpatterns = [
    path('', views.todo_list_view, name='todo_list'),
    path('items/completed', views.todo_completed_list_view, name='show_completed'),
    path('item/<int:id>/', views.todo_detail_view, name='todo_detail'),
    path('item/<int:id>/delete/', views.todo_delete_view, name='todo_delete'),
    path('item/create/', views.todo_create_view, name='todo_create'),
    path('item/<int:id>/update/', views.todo_update_view, name='todo_update'),
    path('item/<int:id>/complete/', views.todo_mark_as_completed_or_incompleted_view, name='todo_complete'),
]

