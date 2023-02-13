# Generated by Django 4.0.4 on 2022-06-02 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_user_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Name of project')),
                ('link_to_git', models.URLField(max_length=256, verbose_name='Link to Git')),
                ('owners', models.ManyToManyField(to='users.user')),
            ],
        ),
        migrations.CreateModel(
            name='ToDo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Text of notes')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Time of creating')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Time of updating')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='todoproject.project')),
            ],
        ),
    ]
