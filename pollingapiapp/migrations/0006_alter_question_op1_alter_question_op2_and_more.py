# Generated by Django 4.1.5 on 2023-01-18 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pollingapiapp', '0005_remove_question_votes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='Op1',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Op2',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Op3',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='Op4',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
