from django.urls import path
from .import views

urlpatterns = [
    path('addTask/', views.addTask,name='addTask'),
    
    #markas done
    path('mark_as_done/<int:pk>/', views.mark_as_done, name='mark_as_done'),
    
    #mark as undone
    path('mark_as_Undone/<int:pk>/', views.mark_as_Undone, name='mark_as_Undone'),

    #edit Feature
    path('edit_task/<int:pk>',views.edit_task,name='edit_task'),

    #delete Feature
    path('delete_task/<int:pk>',views.delete_task,name='delete_task'),
]
