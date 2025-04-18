from .views import home, new_search,index,register,login,log
from django.urls import path

urlpatterns=[
	path('',index,name='index'),
	path('home/',home,name='home'),
	path('register/',register,name='register'),
	path('login/',login,name='login'),
    path('log/',log,name='log'),
	path('new_search',new_search,name='new_search')
]