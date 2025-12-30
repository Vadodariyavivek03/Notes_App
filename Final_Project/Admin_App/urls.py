from django.urls import path
from Admin_App import views

urlpatterns = [
    path('', views.admin_login, name='admin_login'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin_userdata/', views.admin_userdata, name='admin_userdata'),
    path('update_userdata/<int:id>/', views.update_userdata, name='update_userdata'),
    path('delete_userdata/<int:id>/', views.delete_userdata, name='delete_userdata'),
    path('admin_notesdata/', views.admin_notesdata, name='admin_notesdata'),
    path('upload_notes/', views.upload_notes, name='upload_notes'),
    path('update_notes_file/', views.update_notes_file, name='update_notes_file'),
    path('admin_logout/', views.admin_logout, name='admin_logout'),
    path('notes_approve/<int:id>',views.notes_approve,name='notes_approve'),
    path('notes_reject/<int:id>',views.notes_reject,name='notes_reject'),
    path('admin_settings/', views.admin_settings, name='admin_settings'),
    path('admin_inquiry/', views.admin_inquiry, name='admin_inquiry'),
]
