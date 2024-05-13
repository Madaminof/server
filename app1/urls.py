from django.urls import path
from .views import Registratsiya, Login, LogOut



app_name = 'app1'
urlpatterns = [
    path('register/', Registratsiya.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/',LogOut.as_view(), name='logout') ,

    

]