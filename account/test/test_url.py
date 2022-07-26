from django.test import SimpleTestCase
from django.urls import reverse, resolve
from account import views


class AccountUrlTestCase(SimpleTestCase):
    def test_login(self):
        path = reverse('account:login')
        self.assertEqual(resolve(path).route, 'account/login/')
        self.assertEqual(resolve(path).func.view_class, views.LoginView)
        self.assertNotEqual(resolve(path).func.view_class, views.LogoutView)

    def test_logout(self):
        path = reverse('account:logout')
        self.assertEqual(resolve(path).route, 'account/logout/')
        self.assertEqual(resolve(path).func.view_class, views.LogoutView)
        self.assertNotEqual(resolve(path).func.view_class, views.LoginView)

    def test_register(self):
        path = reverse('account:register')
        self.assertEqual(resolve(path).route, 'account/register/')
        self.assertEqual(resolve(path).func.view_class, views.RegisterView)
        self.assertNotEqual(resolve(path).func.view_class, views.LogoutView)

    def test_register_verify(self):
        path = reverse('account:register_verify')
        self.assertEqual(resolve(path).route, 'account/register/verify/')
        self.assertEqual(resolve(path).func.view_class, views.OtpVerifyRegisterView)
        self.assertNotEqual(resolve(path).func.view_class, views.RegisterView)

    def test_profile(self):
        path = reverse('account:profile')
        self.assertEqual(resolve(path).route, 'account/profile/')
        self.assertEqual(resolve(path).func.view_class, views.ProfileView)
        self.assertNotEqual(resolve(path).func.view_class, views.RegisterView)

    def test_profile_edit(self):
        path = reverse('account:profile_edit', kwargs={'pk': 1})
        self.assertEqual(resolve(path).route, 'account/profile/edit/<pk>/')
        self.assertEqual(resolve(path).func.view_class, views.ProfileEditView)
        self.assertNotEqual(resolve(path).func.view_class, views.LogoutView)

    def test_password_change(self):
        path = reverse('account:password_change')
        self.assertEqual(resolve(path).route, 'account/password_change/')
        self.assertEqual(resolve(path).func.view_class, views.ChangePasswordView)
        self.assertNotEqual(resolve(path).func.view_class, views.ProfileView)

    def test_password_change_done(self):
        path = reverse('account:password_change_done')
        self.assertEqual(resolve(path).route, 'account/password_change/done/')
        self.assertEqual(resolve(path).func.view_class, views.ChangePasswordDoneView)
        self.assertNotEqual(resolve(path).func.view_class, views.ChangePasswordView)

    def test_reset_password(self):
        path = reverse('account:password_reset')
        self.assertEqual(resolve(path).route, 'account/password_reset/')
        self.assertEqual(resolve(path).func.view_class, views.ResetPasswordView)
        self.assertNotEqual(resolve(path).func.view_class, views.ResetPasswordDoneView)

    def test_reset_password_done(self):
        path = reverse('account:password_reset_done')
        self.assertEqual(resolve(path).route, 'account/password_reset/done/')
        self.assertEqual(resolve(path).func.view_class, views.ResetPasswordDoneView)
        self.assertNotEqual(resolve(path).func.view_class, views.ResetPasswordView)

    def test_reset_password_confirm(self):
        path = reverse('account:password_reset_confirm',
                       kwargs={'uidb64': 'Nw', 'token': 'b95q9z-147f50713ce124f5776f2855c62b8500'}
                       )

        self.assertEqual(resolve(path).route, 'account/reset/<uidb64>/<token>/')
        self.assertEqual(resolve(path).func.view_class, views.ResetPasswordConfirmView)
        self.assertNotEqual(resolve(path).func.view_class, views.PasswordResetCompleteView)

    def test_reset_password_complete(self):
        path = reverse('account:password_reset_complete')
        self.assertEqual(resolve(path).route, 'account/reset/done/')
        self.assertEqual(resolve(path).func.view_class, views.ResetPasswordCompleteView)
        self.assertNotEqual(resolve(path).func.view_class, views.PasswordResetDoneView)
