
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from Atletas.models import Avatar
from Atletas.models import Atleta

class UserRegisterForm(UserCreationForm):
   
   password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
   password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

   class Meta:
       model = User
       fields = ['first_name', 'last_name',  "username", 'email', 'password1', 'password2']



class UserUpdateForm(forms.ModelForm):
    change_password = forms.BooleanField(label='Cambiar contraseña', required=False)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, required=False)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'change_password', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        change_password = cleaned_data.get('change_password')
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if change_password:
            if not password1 or not password2:
                raise forms.ValidationError('Debe ingresar una contraseña')
            if password1 != password2:
                raise forms.ValidationError('Las contraseñas no coinciden')

        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        change_password = self.cleaned_data.get('change_password')
        password = self.cleaned_data.get('password1')

        if change_password and password:
            user.set_password(password)

        if commit:
            user.save()

        return user

"""class AtletaForm(forms.ModelForm):
    class Meta:
        model = Atleta
        fields = ['categoria', 'apodo']"""


"""class AtletaForm(forms.ModelForm):
    grace = forms.CharField(required=False)
    fran = forms.CharField(required=False)
    murph = forms.CharField(required=False)

    class Meta:
        model = Atleta
        fields = ['categoria', 'apodo', 'grace', 'fran', 'murph', 'backsquat_rm', 'clean_rm', 'jerk_rm', 'snatch_rm', 'deadlift_rm']

    def save(self, commit=True, user=None):
        atleta = super().save(commit=False)
        if user:
            atleta.user = user
        if commit:
            atleta.save()
        return atleta
"""
class AtletaForm(forms.ModelForm):
    grace = forms.CharField(required=False)
    fran = forms.CharField(required=False)
    murph = forms.CharField(required=False)

    class Meta:
        model = Atleta
        fields = ['categoria', 'apodo', 'grace', 'fran', 'murph', 'backsquat_rm', 'clean_rm', 'jerk_rm', 'snatch_rm', 'deadlift_rm']
        widgets = {
            'categoria': forms.TextInput(attrs={'class': 'form-control'}),
            'apodo': forms.TextInput(attrs={'class': 'form-control'}),
            'grace': forms.TextInput(attrs={'class': 'form-control'}),
            'fran': forms.TextInput(attrs={'class': 'form-control'}),
            'murph': forms.TextInput(attrs={'class': 'form-control'}),
            'backsquat_rm': forms.NumberInput(attrs={'class': 'form-control'}),
            'clean_rm': forms.NumberInput(attrs={'class': 'form-control'}),
            'jerk_rm': forms.NumberInput(attrs={'class': 'form-control'}),
            'snatch_rm': forms.NumberInput(attrs={'class': 'form-control'}),
            'deadlift_rm': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def save(self, commit=True, user=None):
        atleta = super().save(commit=False)
        if user:
            atleta.user = user
        if commit:
            atleta.save()
        return atleta

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['categoria'].widget.attrs.update({'class': 'form-control'})
        self.fields['apodo'].widget.attrs.update({'class': 'form-control'})
        self.fields['grace'].widget.attrs.update({'class': 'form-control'})
        self.fields['fran'].widget.attrs.update({'class': 'form-control'})
        self.fields['murph'].widget.attrs.update({'class': 'form-control'})
        self.fields['backsquat_rm'].widget.attrs.update({'class': 'form-control'})
        self.fields['clean_rm'].widget.attrs.update({'class': 'form-control'})
        self.fields['jerk_rm'].widget.attrs.update({'class': 'form-control'})
        self.fields['snatch_rm'].widget.attrs.update({'class': 'form-control'})
        self.fields['deadlift_rm'].widget.attrs.update({'class': 'form-control'})


class AtletaUpdateForm(forms.ModelForm):
    categoria = forms.CharField(max_length=20)
    apodo = forms.CharField(max_length=20, required=False)

    class Meta:
        model = Atleta
        fields = ['categoria', 'apodo'
        ]

    def clean(self):
        cleaned_data = super().clean()

        # Agrega cualquier validación adicional que necesites aquí

        return cleaned_data

    def save(self, commit=True):
        atleta = super().save(commit=False)

        # Agrega cualquier otra lógica de guardado que necesites aquí

        if commit:
            atleta.save()

        return atleta




class AvatarFormulario(forms.ModelForm):

   class Meta:
       model = Avatar
       fields = ['imagen']