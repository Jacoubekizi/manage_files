# Generated by Django 5.0.6 on 2024-06-18 08:08

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_statusfile_user_alter_statusfile_status_orderfile'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orderfile',
            options={'ordering': ['created_at']},
        ),
        migrations.AddField(
            model_name='orderfile',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='statusfile',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'طلب مراجعة مشرف'), ('2', 'طلب تعديل من مساعد'), ('3', 'رفض'), ('4', 'طلب مراجعة مدير'), ('5', 'تم التحقق'), ('6', 'طلب مراجعة مدقق')], max_length=25, null=True),
        ),
    ]