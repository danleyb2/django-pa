# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-12-31 07:14
from __future__ import unicode_literals

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                    regex='^\\+?1?\\d{9,15}$')])),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(default='images/services/None/no-img.jpg', upload_to='images/icons')),
                ('css', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=9)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('p_url', models.URLField(blank=True, verbose_name='project_url')),
                ('s_url', models.URLField(blank=True, verbose_name='source_url')),
                ('screenshot',
                 models.ImageField(default='images/projects/None/no-img.jpg', upload_to='images/projects')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('url', models.URLField(blank=True, verbose_name='service_link')),
                ('username', models.CharField(blank=True, max_length=20)),
                ('icon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pa.Icon')),
            ],
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('experience', models.PositiveIntegerField(default=1)),
                ('knower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='technologies',
                                             to='pa.SiteInfo')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(blank=True, verbose_name='Website')),
                ('profile_image',
                 models.ImageField(default='images/profile/None/no-img.jpg', upload_to='images/profile')),
                ('company', models.CharField(blank=True, max_length=50)),
                ('intro', models.TextField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='user_profile',
                                              to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='siteinfo',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pa.UserProfile'),
        ),
        migrations.AddField(
            model_name='service',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services',
                                    to='pa.SiteInfo'),
        ),
        migrations.AddField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects',
                                    to='pa.SiteInfo'),
        ),
        migrations.AddField(
            model_name='project',
            name='technologies',
            field=models.ManyToManyField(to='pa.Technology'),
        ),
        migrations.AddField(
            model_name='location',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location',
                                       to='pa.UserProfile'),
        ),
        migrations.AddField(
            model_name='contact',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pa.UserProfile'),
        ),
    ]
