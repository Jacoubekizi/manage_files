# from django import forms
# from .models import Task, Student
# from django.utils.translation import gettext_lazy as _




# class StudentForm(forms.ModelForm):

#     student_code = forms.CharField(label="Code", widget=forms.Textarea(attrs={
#         'rows': 5,
#         'placeholder':'أدخل الكود'
#     }),)
#     student_name = forms.CharField(label="Student name", widget=forms.TextInput(attrs={
#         'placeholder':'أدخل الاسم الثلاثي'
#     }))
#     student_id = forms.IntegerField(label="Studetn id", widget=forms.NumberInput(attrs={
#         'placeholder':'أدخل الرقم الجامعي'
#     }))

#     student_branch_number = forms.IntegerField(label='Student branch number', widget=forms.NumberInput(attrs={
#         'placeholder':'أدخل رقم الفئة'
#     }
#     ))
#     task_file = forms.FileField(label="Task File", widget=forms.FileInput(attrs={
#         'placeholder': 'يحتوي شرح الكود word قم بإدخال ملف',
 
#     }))


#     class Meta:
#         model = Student
#         fields = ['student_name', 'student_id', 'student_branch_number', 'student_code', 'task_file']


# class TaskForm(forms.ModelForm):

#     class Meta:
#         model = Task
#         fields = '__all__'
#         exclude = ['id', ]




from typing import Any
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import authenticate
from .models import *
from django import forms
from django.core.exceptions import ValidationError
        
class CustomUserCreationForm(forms.ModelForm):

    password1= forms.CharField(label='Password', widget=forms.PasswordInput)
    password2= forms.CharField(label='password confirmatio', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('user_type',)

    def clean_password2(self):
        password1=self.cleaned_data.get('password1')
        password2=self.cleaned_data.get('password2')
        
        if password1 and password2 and password1 != password2:
            raise ValidationError("passwords dont match")
        return password2
    
    def save(self, commit: bool = True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('user_type', )


class FormUploadFile(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ('file', 'type_file', 'note',)
        # fields = '__all__'

class FormStatusFile(forms.ModelForm):
    class Meta:
        model = StatusFile
        fields = ('note',)


class FormOrderFile(forms.ModelForm):
    class Meta:
        model = OrderFile
        fields = '__all__'