from django.db import models
from django.utils.translation import ugettext as _
from django.urls import reverse
from django.contrib.auth.models import User


class Pet(models.Model):
    kind = models.CharField(_('animal type'), max_length=8, choices=[
        ('cat', 'Cat'),
        ('dog', 'Dog'),
    ])  # 'type' is reserved in python, so better use 'kind' as field name
    name = models.CharField(_('name'), max_length=32)
    birthday = models.DateField(_('birthday'))
    owner = models.ForeignKey(User, on_delete=models.CASCADE)  # assume any User may be an owner

    class Meta:
        ordering = ['owner', 'birthday', 'name', 'pk']
        verbose_name = _('pet')
        verbose_name_plural = _('pets')

    def __str__(self):
        return '{kind} {name} ({birthday})'.format(
            kind=self.kind,
            name=self.name,
            birthday=self.birthday,
        )
