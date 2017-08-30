from django.contrib.auth.models import User
from django import forms
from .models import Program, Cycle, Step, MotorSetting

#creating a class to bootstrap program form on frontend
class ProgramFormClass(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ProgramFormClass, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg'
        })

    class Meta:
        model = Program
        fields = ['program_name', 'program_description', 'cycles']


#creating a class to bootstrap cycle form on frontend
class CycleFormClass(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CycleFormClass, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg'
        })

    class Meta:
        model = Cycle
        fields = ['cycle_name', 'cycle_description', 'steps']


#creating a class to bootstrap step form on frontend
class StepFormClass(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StepFormClass, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control form-control-lg'
        })

    class Meta:
        model = Step
        fields = '__all__'

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
