from django.urls import path
from .views import (
    BookListCreateAPIView, BookDetailAPIView,
    AuthorListCreateAPIView, AuthorDetailAPIView,
    MemberListCreateAPIView, MemberDetailAPIView,
    RegisterView
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    
    path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookDetailAPIView.as_view(), name='book-detail'),

    
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorDetailAPIView.as_view(), name='author-detail'),

    
    path('members/', MemberListCreateAPIView.as_view(), name='member-list-create'),
    path('members/<int:pk>/', MemberDetailAPIView.as_view(), name='member-detail'),

    
    path('auth/register/', RegisterView.as_view(), name='auth-register'),
    path('auth/login/', TokenObtainPairView.as_view(), name='auth-login'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
]

