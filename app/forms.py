"""
Definition of forms.
"""
import re
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class RegistrationForm(forms.Form):
	username = forms.RegexField(regex=r'^\w+$', widget = forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("UserName"), error_message = { 'invalid': _("This value must contain only letters, numbers and underscores.")} )
	email = forms.EmailField(widget = forms.TextInput(attrs = dict(required=True, max_length=30)), label=_("Email Address"))
	phone = forms.EmailField(widget = forms.TextInput(attrs = dict(required=True, max_length=30)), label=_("Phone Number"))
	password1 = forms.CharField(widget = forms.PasswordInput(attrs = dict(required=True, max_length=30, render_value=False)), label=_("Password"))
	password2 = forms.CharField(widget = forms.PasswordInput(attrs = dict(required=True, max_length=30, render_value=False)), label=_("Password (again)"))

	def clean_username(self):
		try:
			user = User.objects.get(username__iexact=self.cleaned_data['username'])
		except User.DoesNotExist:
			return self.cleaned_data['username']
		raise forms.ValidationError(_("The username already exists. Please try another one "))

	def clean(self):
		if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
			if self.cleaned_data['password1'] != self.cleaned_data['password2']:
				raise forms.ValidationError(_("The two password fields did not match."))
		return self.cleaned_data
