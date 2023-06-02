
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


class AtletaForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    fecha_nacimiento = forms.DateField()
    categoria = forms.CharField(max_length=20)
    apodo = forms.CharField(max_length=20, required=False)
    Fran = forms.DurationField(required=False)
    Grace = forms.DurationField(required=False)
    Isabel = forms.DurationField(required=False)
    Murph = forms.DurationField(required=False)
    RM_backsquat = forms.IntegerField(required=False)
    RM_deadlift = forms.IntegerField(required=False)
    RM_bench = forms.IntegerField(required=False)
    RM_snatch = forms.IntegerField(required=False)
    RM_clean = forms.IntegerField(required=False)
    RM_jerk = forms.IntegerField(required=False)
    RM_cleanandjerk = forms.IntegerField(required=False)

class AtletaUpdateForm(forms.ModelForm):
    fecha_nacimiento = forms.DateField()
    categoria = forms.CharField(max_length=20)
    apodo = forms.CharField(max_length=20, required=False)
    Fran = forms.DurationField(required=False)
    Grace = forms.DurationField(required=False)
    Isabel = forms.DurationField(required=False)
    Murph = forms.DurationField(required=False)
    RM_backsquat = forms.IntegerField(required=False)
    RM_deadlift = forms.IntegerField(required=False)
    RM_bench = forms.IntegerField(required=False)
    RM_snatch = forms.IntegerField(required=False)
    RM_clean = forms.IntegerField(required=False)
    RM_jerk = forms.IntegerField(required=False)
    RM_cleanandjerk = forms.IntegerField(required=False)

    class Meta:
        model = Atleta
        fields = ['fecha_nacimiento', 'categoria', 'apodo',
                  'Fran', 'Grace', 'Isabel', 'Murph',
                  'RM_backsquat', 'RM_deadlift', 'RM_bench',
                  'RM_snatch', 'RM_clean', 'RM_jerk', 'RM_cleanandjerk']

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