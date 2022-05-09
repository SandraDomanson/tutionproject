# Generated by Django 4.0.4 on 2022-04-23 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('studentname', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phn', models.CharField(blank=True, max_length=255, null=True)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('cpassword', models.CharField(max_length=255)),
                ('classs', models.CharField(max_length=255)),
                ('subjects', models.CharField(max_length=255)),
                ('fathersname', models.CharField(max_length=255)),
                ('mothersname', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('pincode', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subname', models.CharField(max_length=255)),
                ('classs', models.CharField(max_length=255)),
                ('fees', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('tid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('phn', models.CharField(blank=True, max_length=255, null=True)),
                ('sub', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('cpassword', models.CharField(max_length=255)),
                ('res', models.FileField(upload_to='static/resume')),
            ],
        ),
    ]
