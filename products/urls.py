from django.urls import path
from .views import BookView,BookDetailView,Savat,BookUpdateView
app_name = 'products'
urlpatterns=[
    path('', BookView.as_view(), name='bookview'),
    path('detail/<int:pk>', BookDetailView.as_view(), name='detail'),
    path('Savat/<int:pk>', Savat.as_view(), name='savat'),
    path('update/<int:pk>', BookUpdateView.as_view(), name='update'),
  

]


