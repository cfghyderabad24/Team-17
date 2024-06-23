from django.urls import path
from . import views
urlpatterns=[
    path('',views.signup,name='signup'),
    path('index/',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('addstudent/',views.student_form,name='addstudent'),
    path('add_genre/', views.add_genre, name='add_genre'),
    path('add_book/', views.add_book, name='add_book'),
    path('checkout/', views.checkout_view, name='checkout_view'),
    path('checkin/',views.checkin_view,name='checkin_view'),
    path('get_checkouts_by_genre/', views.get_checkouts_by_genre, name='get_checkouts_by_genre'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('profile/',views.profile,name='profile')
]