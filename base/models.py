from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

Type_User = (
    ('مساعد','مساعد'),
    ('مدقق','مدقق'),
    ('مشرف','مشرف'),
    ('مدير','مدير'),
)

Status = (
    ('1','طلب مراجعة مشرف'),
    ('2','طلب تعديل من مساعد'),
    ('3','رفض'),
    ('4','طلب مراجعة مدير'),
    ('5','تم التحقق'),
    ('6', 'طلب مراجعة مدقق')
)

Type_File = (
    ('word','word'),
    ('pdf','pdf'),
    ('exel','exel'),
)

class User(AbstractUser):
    user_type = models.CharField(max_length=25, choices=Type_User)

    def __str__(self) -> str:
        return self.username
    
class UploadFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='files')
    note = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    type_file = models.CharField(max_length=25, choices=Type_File)

    def __str__(self) -> str:
        return f'{self.user.username}ملف من قبل'



class StatusFile(models.Model):
    file = models.ForeignKey(UploadFile, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    status = models.CharField(max_length=25, choices=Status, blank=True, null=True)
    note = models.TextField(max_length=1000, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_proccessed = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.status}ملف-'
    
    class Meta:
        ordering = ['created_at']


class OrderFile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.CharField(max_length=25)
    description = models.TextField(max_length=1000)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.user.username} طلب ملف من المدقق'
    
    class Meta:
        ordering = ['created_at']