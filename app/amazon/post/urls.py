
from django.urls import path
from .views import author_list_view, author_update_view, author_delete_view,book_list_view, book_update_view, \
    book_delete_view,home,add_author_view,add_book_view,author_success_view,book_success_view
    
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home),
    path('add-author/', add_author_view, name='add_author'),
    path('add-book/', add_book_view, name='add_book'),
    path('author-success/', author_success_view, name='author_success'),
    path('book-success/', book_success_view, name='book_success'),
    path('authors/', author_list_view, name='author_list'),
    path('author/update/<int:pk>/', author_update_view, name='author_update'),
    path('author/delete/<int:pk>/', author_delete_view, name='author_delete'),
    path('books/', book_list_view, name='book_list'),
    path('book/update/<int:pk>/', book_update_view, name='book_update'),
    path('book/delete/<int:pk>/', book_delete_view, name='book_delete'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
