from django.urls import path
from . import views

urlpatterns = [
    path('', views.word_list, name='word_list'),  # Home page to list words
    path('edit/<int:pk>/', views.edit_word, name='edit_word'),  # Edit page
]
