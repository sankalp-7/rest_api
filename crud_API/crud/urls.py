from.views import *
from django.urls import path 
app_name='crud'
urlpatterns=[ 
    path('',home),
    path('login/',login,name='login'),
    path('view/',view,name='view'),
    path('update/<int:pk>',Update,name='update'),
    path('delete/<int:pk>',Delete,name='delete'),
    path('api/',api_list),
    path('api/create',api_create),
    path('api/delete/<int:pk>',api_delete),
    path('api/update/<int:pk>',api_update)
]
