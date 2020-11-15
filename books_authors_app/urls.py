from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('books/create', views.create_book),
    path('book/<int:book_id>', views.display_book),
    path('book/<int:book_id>/update', views.update_book),
    path('authors', views.author_index),
    path('author/create', views.create_author),
    path('author/<int:author_id>', views.display_author),
    path('author/<int:author_id>/update', views.update_author),
    path('book/<int:book_id>/delete', views.delete_book),
    path('author/<int:author_id>/delete', views.delete_author),
]

