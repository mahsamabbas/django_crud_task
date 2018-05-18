from django import forms


class PetOwnerForm(forms.ModelForm):
    class Meta:
        fields = ['kind', 'name', 'birthday']
