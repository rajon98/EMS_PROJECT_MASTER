# Generated by Django 4.2.2 on 2023-07-06 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_attendee_dob_alter_attendee_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventcategory',
            name='priority',
        ),
    ]
