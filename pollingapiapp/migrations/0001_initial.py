# Generated by Django 4.1.5 on 2023-01-18 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Question', models.CharField(max_length=300, null=True, unique=True)),
                ('Op1', models.CharField(max_length=100, null=True, unique=True)),
                ('Op2', models.CharField(max_length=100, null=True, unique=True)),
                ('Op3', models.CharField(max_length=100, null=True, unique=True)),
                ('Op4', models.CharField(max_length=100, null=True, unique=True)),
                ('Date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Phone', models.SmallIntegerField()),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Result', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D')], default='A', max_length=1)),
                ('User', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='voted_by', to='pollingapiapp.userprofile')),
                ('VQuestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='VQuestionr', to='pollingapiapp.question')),
                ('Votes', models.ManyToManyField(to='pollingapiapp.userprofile')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='QUser',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_by', to='pollingapiapp.userprofile'),
        ),
        migrations.AddField(
            model_name='question',
            name='Votes',
            field=models.ManyToManyField(blank=True, related_name='voted_of', to='pollingapiapp.vote'),
        ),
    ]
