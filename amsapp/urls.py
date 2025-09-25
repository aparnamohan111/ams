from django.urls import path,include
from . import views
urlpatterns = [
   path('',views.login,name="login"),
   path('reg',views.reg,name="reg"),
   path('base',views.base,name="base"),
   path('admin_dashboard',views.admin_dashboard,name="admin_dashboard"),
   path('manage_slots',views.manage_slots,name="manage_slots"),
   path('manage_bookings',views.manage_bookings,name="manage_bookings"),
   path('manage_slots',views.manage_slots,name="manage_slots"),
   path('base_user',views.base_user,name="base_user"),
   path('user_dashboard',views.user_dashboard,name="user_dashboard"),
   path('available_slots',views.available_slots,name="available_slots"),
   path('book-slot/<int:slot_id>/', views.book_slot, name='book_slot'),
   path('my_bookings/', views.my_bookings, name='my_bookings'),
   path('cancel-booking/<int:booking_id>/', views.cancel_booking, name='cancel_booking'),
   path('admin/cancel-booking/<int:booking_id>/', views.admin_cancel_booking, name='admin_cancel_booking'),
   path('logout/', views.logout_view, name='logout'),

]
