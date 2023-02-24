from django.urls import path
from . import views

urlpatterns = [
path('register/', views.register, name="register"),
path('login/', views.login_2, name="login"),
path('cerrar_sesion', views.cerrar_sesion, name="cerrar_sesion"),
path('dashboard/', views.dashboard, name="dashboard"),
path('', views.dashboard, name="dashboard"),
path('forgotPassword/', views.forgotpassword, name="forgotpassword"),
path('resetpassword_validate/<uidb64>/<token>', views.resetpassword_validate, name="resetpassword_validate"),
path('resetPassword/', views.resetPassword, name="resetPassword"),
path('activate/<uidb64>/<token>', views.activate, name="activate"),
]