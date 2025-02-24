# Generated by Django 5.1.1 on 2024-12-16 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irohub', '0002_alter_contact_email_alter_registering_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='name',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='password',
        ),
        migrations.AddField(
            model_name='contact',
            name='email1',
            field=models.CharField(default='default', max_length=25),
        ),
        migrations.AddField(
            model_name='contact',
            name='name1',
            field=models.CharField(default='default', max_length=20),
        ),
        migrations.AddField(
            model_name='contact',
            name='password1',
            field=models.CharField(default='default', max_length=20),
        ),
        migrations.AlterField(
            model_name='registering',
            name='password',
            field=models.CharField(max_length=30),
        ),
    ]
