# Generated by Django 3.0.8 on 2020-07-27 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_assignment_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='submitted_file',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
