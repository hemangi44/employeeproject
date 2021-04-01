
from django.contrib import admin
from django.urls import path
from empapp.views import home,showdept, adddept, deletedept, showinfo, addinfo, deleteinfo, search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('showdept/',showdept,name='showdept'),
    path('adddept/',adddept,name='adddept'),
    path('deletedept/<int:id>',deletedept,name='deletedept'),
    path('showinfo/',showinfo,name='showinfo'),
    path('addinfo/',addinfo,name='addinfo'),
    path('deleteinfo/<int:id>',deleteinfo,name='deleteinfo'),
    path('search/',search,name='search'),
]
