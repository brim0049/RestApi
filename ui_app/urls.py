from django.urls import path
from .views import home, utilisateurs, statistiques, addUser,updatePassword,user_delete,validateUpdatePassword

urlpatterns = [
    path('', home, name="home"),
    path('utilisateurs/' , utilisateurs, name="utilisateurs"),
    path('statistiques/', statistiques, name="statistiques"),
    path('addUser/', addUser, name="addUser"),
    path('updatePassword/<str:email>', updatePassword, name="updatePassword"),
    path('validateUpdatePassword/<str:email>', validateUpdatePassword, name="validateUpdatePassword"),
    path(r'^delete/(?P<pk>[0-9]+)/$', user_delete, name='user_delete')    
]
