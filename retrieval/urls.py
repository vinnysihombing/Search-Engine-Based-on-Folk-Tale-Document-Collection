from django.urls import path
from retrieval import views
from . import views

app_name = 'retrieval'
urlpatterns = [
    path('', views.import_csv),
    path('cerita/<int:id>', views.cerita_page, name='cerita'),
    path('result/', views.result),
]