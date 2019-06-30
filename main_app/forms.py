from django import forms
from main_app.models import Group


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_number',
        ]
