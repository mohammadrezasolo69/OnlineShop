from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from account.forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('email',"id", 'full_name', 'phone_number', 'is_staff', 'is_superuser')
    list_editable = ('is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email', 'phone_number', 'full_name')
    ordering = ('email',)

    fieldsets = (
        (('Personal info'), {'fields': ('full_name', 'beo', 'avatar', 'email', 'password')}),

        (('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser'),
        }),

        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('full_name', 'phone_number', 'email', 'password1', 'password2'),
        }),
    )
