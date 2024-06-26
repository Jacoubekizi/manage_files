# Generated by Django 5.0.6 on 2024-06-15 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_uploadfile_file'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='statusfile',
            options={'ordering': ['created_at']},
        ),
        migrations.AlterField(
            model_name='statusfile',
            name='status',
            field=models.CharField(blank=True, choices=[('1', 'قبول'), ('2', 'رفض'), ('3', 'تعديل')], max_length=25, null=True),
        ),
    ]
