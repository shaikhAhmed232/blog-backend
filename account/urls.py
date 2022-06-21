from django.urls import path
from .views import Signup, TokenBlackListView, UserDetailsView

app_name = 'account'

urlpatterns = [
    path('signup/', Signup.as_view(), name='user_signup'),
    path('<int:pk>/', UserDetailsView.as_view(), name="user_detail"),
    path('logout/blacklist/', TokenBlackListView.as_view(), name='token_blacklist')
]
