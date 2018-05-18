from django.contrib.admin import AdminSite
from django.contrib.auth.forms import AuthenticationForm

class OwnersAdminSite(AdminSite):
    site_header = 'Owners\' admin site'
    login_form = AuthenticationForm

    def has_permission(self, request):
        return request.user.is_active


owners = OwnersAdminSite('owners')
admin = AdminSite()
