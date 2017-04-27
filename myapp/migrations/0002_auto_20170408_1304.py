# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-08 13:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='Ladder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Game')),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
            ],
        ),
        migrations.CreateModel(
            name='PlatformGame',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Game')),
                ('platform', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Platform')),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('date_of_birth', models.DateField(verbose_name='Date of Birth')),
                ('email', models.EmailField(max_length=254)),
                ('xp', models.IntegerField()),
                ('gender', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('X', 'Not specified')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='PlayerTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Player')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=18)),
                ('tag', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='TeamMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ladder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Ladder')),
                ('match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Match')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Team')),
            ],
        ),
        migrations.DeleteModel(
            name='Animal',
        ),
        migrations.AddField(
            model_name='playerteam',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.Team'),
        ),
    ]