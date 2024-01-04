from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('base/',views.baser,name='baser'),
    path('login/', views.login_user, name ='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_password/', views.change_password, name='change_password'),
    path('base/account/',views.account,name='account'),
    path('base/person/',views.add_person,name='person'),
    path('base/donor/',views.add_donor,name='donor'),
    path('base/stock/',views.stock_show,name='stock'),
    path('base/request/',views.request_blood,name='receive'),
    path('base/search/',views.search_blood,name='search'),
    path('base/person_info/',views.person_info,name='person_info'),
    path('base/donor_info/',views.donor_info,name='donor_info'),
    path('base/camp/',views.camp_info,name='camp'),
]

