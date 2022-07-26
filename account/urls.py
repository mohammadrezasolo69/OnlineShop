from django.urls import path, include
from account import views

app_name = 'account'
urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit/<pk>', views.ProfileEditView.as_view(), name='profile_edit'),

    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),

    path('register/', views.RegisterView.as_view(), name='register'),
    path('register/verify/', views.OtpVerifyRegisterView.as_view(), name='register_verify'),

    path('password_reset/', views.ResetPasswordView.as_view(), name='password_reset'),
    path('password_reset/done/', views.ResetPasswordDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.ResetPasswordConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.UserPasswordResetCompleteView.as_view(), name='password_reset_complete'),

    path('password_change/', views.ChangePasswordView.as_view(), name='password_change'),
    path('password_change/done', views.ChangePasswordDoneView.as_view(), name='password_change_done')

]
