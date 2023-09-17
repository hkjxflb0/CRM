from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.home,name='home'),
    path('product/',views.product,name='product'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('order_form/<str:pk>',views.orderform,name='order_form'),
    path('update/<str:pk>/',views.update,name='update'),
    path('delete/<str:pk>/',views.deleteorder,name='delete_order'),
    path('login/',views.loginpage,name="login"),
    path('register/',views.registration,name="register"),
    path('logout/',views.logoutUser,name="logout"),
    path('user',views.userPage,name="user-page"),
    path('account/',views.accountSettings,name="account"),
    path('reset_password/',auth_views.PasswordResetView.as_view(),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(),name="password_reset_complete"),

] 