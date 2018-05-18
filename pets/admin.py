from django.contrib import admin as django_admin
from project.admin import owners, admin
from .models import Pet
from .forms import PetOwnerForm


class PetAdmin(django_admin.ModelAdmin):
    list_display = ['name', 'kind', 'birthday', 'owner']
    list_filters = ['kind']
    search_fields = ['name']

admin.register(Pet, PetAdmin)


class PetOwnerAdmin(PetAdmin):
    list_display = ['name', 'kind', 'birthday']
    form = PetOwnerForm

    def get_queryset(self, request):
        return super().get_queryset(request).filter(owner=request.user)

    def has_module_permission(self, *args, **kwargs):
        return True

    def has_add_permission(self, *args, **kwargs):
        return True

    def has_change_permission(self, *args, **kwargs):
        return True

    def has_delete_permission(self, *args, **kwargs):
        return True

    def save_model(self, request, obj, *args, **kwargs):
        obj.owner = request.user
        super().save_model(request, obj, *args, **kwargs)

owners.register(Pet, PetOwnerAdmin)
