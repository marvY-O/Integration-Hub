from django.urls import path
from . import views

#router = routers.DefaultRouter()
#router.register(r'basicdetails', views.InsertData)

urlpatterns = [
    #path('create_user/', create_user, name = "create_user"),
    #path('read_data/', read_data, name = "read_data"),
    #path('', include(router.urls)),
    path('', views.main, name='home'),
    path('addBank/', views.addBank, name="addBank"),
    path('addBankFunc/', views.addBankFunc, name="addBankFunc")
]
