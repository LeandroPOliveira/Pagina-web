from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class LoginForms(forms.Form):
    nome_login = forms.CharField(label="Nome de Login",
                                 required=True,
                                 max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', "placeholder": 'Ex. José da Silva'}))
    senha = forms.CharField(label="Senha",
                            required=True,
                            max_length=70,
                            widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Digite a senha'}))


class CadastroForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(CadastroForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'

# class CadastroForms(forms.Form):
#     nome_cadastro = forms.CharField(label="Nome de Cadastro",
#                                  required=True,
#                                  max_length=100,
#                                  widget=forms.TextInput(
#                                      attrs={'class': 'form-control', "placeholder": 'Ex. José da Silva'}))
#
#     email = forms.CharField(label="Email",
#                                  required=True,
#                                  max_length=100,
#                                  widget=forms.EmailInput(
#                                      attrs={'class': 'form-control', "placeholder": 'Ex. jose@mail.com'}))
#
#     senha_1 = forms.CharField(label="Senha",
#                             required=True,
#                             max_length=70,
#                             widget=forms.PasswordInput(
#                                 attrs={'class': 'form-control', "placeholder": 'Digite sua senha'}))
#
#     senha_2 = forms.CharField(label="Confirme sua senha",
#                                 required=True,
#                                 max_length=70,
#                                 widget=forms.PasswordInput(
#                                     attrs={'class': 'form-control', "placeholder": 'Confirme sua senha'}))
#
#     def clean_nome_cadastro(self):
#         nome = self.cleaned_data.get('nome_cadastro')
#         if nome:
#             nome = nome.strip()
#             if " " in nome:
#                 raise forms.ValidationError('Espaços não são permitidos neste campo')
#             else:
#                 return nome
#
#     def clean_senha_2(self):
#         senha_1 = self.cleaned_data.get('senha_1')
#         senha_2 = self.cleaned_data.get('senha_2')
#         if senha_1 and senha_2:
#             if senha_1 != senha_2:
#                 raise forms.ValidationError('Senhas não são iguais')
#             else:
#                 return senha_2
#


class PerfilForm(UserChangeForm):
    # Hide Password stuff
    password = None
    # Get other fields
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(PerfilForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'


class UserInfoForm(forms.ModelForm):
    telefone = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone'}), required=False)
    endereco = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address 1'}), required=False)
    cidade = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'City'}), required=False)
    cep = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Zipcode'}), required=False)

    class Meta:
        model = Profile
        fields = ('telefone', 'endereco', 'cidade', 'cep')


class NovaSenhaForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']
    
    def __init__(self, *args, **kwargs):
        super(NovaSenhaForm, self).__init__(*args, **kwargs)
    
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password1'].label = ''
        self.fields['new_password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'
    
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['new_password2'].label = ''
        self.fields['new_password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'
    
    
