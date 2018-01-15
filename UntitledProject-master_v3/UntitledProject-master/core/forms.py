from django import forms
from django.contrib.auth.models import User

class RegisterUserForm(forms.Form):
  email = forms.EmailField(required=True)
  password = forms.CharField(required=True)
  name = forms.CharField(required=True)
  username = forms.CharField(required=True)

  def is_valid(self):
    valid = True

    if not super(RegisterUserForm, self).is_valid():
      valid = False

    user_exists = User.objects.filter(username=self.data['email']).exists()
    if user_exists:
      valid = False

    return valid

class NewProjectForm(forms.Form):
  name = forms.CharField(required=True)
  description = forms.CharField(required=True)
  start_date = forms.CharField(required=True)
  end_date = forms.CharField(required=True)

  def is_valid(self):
    valid = True

    if not super(NewProjectForm, self).is_valid():
      valid = False

    return valid

class NewPersonForm(forms.Form):
  name = forms.CharField(required=True)
  salary = forms.IntegerField()
  function = forms.CharField(required=True)

  def is_valid(self):
    valid = True

    if not super(NewPersonForm, self).is_valid():
      valid = False

    return valid

class NewTaskForm(forms.Form):
  name = forms.CharField(required=True)
  responsable_id = forms.IntegerField(required=True)
  project_id = forms.IntegerField(required=True)

  def is_valid(self):
    valid = True

    if not super(NewTaskForm, self).is_valid():
      valid = False

    return valid

class NewResourceForm(forms.Form):
  name = forms.CharField(required=True)
  value = forms.FloatField(required=True)
  project_id = forms.IntegerField(required=True)

  def is_valid(self):
    valid = True

    if not super(NewResourceForm, self).is_valid():
      valid = False

    return valid