from django.urls import path
from .views import (AllAdminType, AdminTypeById, CreateAdminType, UpdateAdminType, DeleteAdminType, AllAdminLogin, AdminById, CreateAdmin, UpdateAdmin, DeleteAdmin)

urlpatterns = [
    path('admins/', AllAdminType.as_view(), name='all-admintypes'),
    path('admintypebyid/<int:Id>/', AdminTypeById.as_view(), name='admin-by-id'),
    path('createadmintype/', CreateAdminType.as_view(), name='create-admintype'),
    path('updateadmintype/', UpdateAdminType.as_view(), name='update-admin-type'),
    path('deleteadmintype/<int:Id>/', DeleteAdminType.as_view(), name='delete-admin-type'),
    path('alladmins/', AllAdminLogin.as_view(), name='all-admins'),
    path('adminbyid/<int:Id>/', AdminById.as_view(), name='admin-by-id'),
    path('createadmin/', CreateAdmin.as_view(), name='create-admin'),
    path('updateadmin/', UpdateAdmin.as_view(), name='update-admin-'),
    path('deleteadmin/<int:Id>/', DeleteAdmin.as_view(), name='delete-admin-'),
]