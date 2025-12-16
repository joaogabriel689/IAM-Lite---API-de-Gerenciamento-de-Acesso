from django.contrib import admin
from django.urls import path, include
from core.api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/acess-requests/', views.AcessRequestListCreateView.as_view(), name='acess-request-list-create'),
    path('api/acess-requests/<int:pk>/', views.AcessRequestListCreateView.as_view(), name='acess-request-detail'),
    path('api/audit-logs/', views.AuditLogListCreateView.as_view(), name='audit-log-list'),
    path('api/users/', views.UserView.as_view(), name='user-create'),
    path('api/users/<int:pk>/', views.UserView.as_view(), name='user-detail'),
]
