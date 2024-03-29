from django.urls import path
from .views import SignUpView, LoginView, ParagraphCreateView, SearchView, RefreshTokenView

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('token/refresh/', RefreshTokenView.as_view(), name='refresh-token'),
    path('paragraphs/', ParagraphCreateView.as_view(), name='paragraphs'),
    path('search/', SearchView.as_view(), name='search'),
]
