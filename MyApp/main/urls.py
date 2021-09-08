from django.urls import path
from django.conf.urls import url
from . import views
from .views import *

urlpatterns = [
    path('', views.home, name= 'home'),
    path('register/', views.register, name= 'register'),
    path('login/', views.loginPage, name= 'login'),
    path('logout/', views.logoutUser, name= 'logout'),
    path('student_dashboard/', views.student_dashboard, name= 'student_dashboard'),
    path('student_portal/', views.student_portal, name='student_portal'),
    path('s_attendance/', views.s_attendance, name='s_attendance'),
    path('student_view/', views.student_view, name='student_view'),
    path('main/', views.main, name='main'),
    path('profile/', views.profile, name='profile'),
    path('leave_attendance/', views.leave_attendance, name='leave_attendance'),
    path('admin_login/', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_attendance_view/', views.admin_attendance_view, name='admin_attendance_view'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('admin_mar_atten/', views.admin_mark_atten, name='admin_mark_atten'),
    path('from_to/', views.from_to, name='from_to'),
    path('admin_grade/', views.admin_grade, name='admin_grade'),
    path('admin_base/', views.admin_base, name='admin_base'),
    path('base/', views.base, name='base'),
    #path('edit_base/', views.edit_base, name='edit_base'),
    path('base_test/', views.base_test, name='base_test'),

]
