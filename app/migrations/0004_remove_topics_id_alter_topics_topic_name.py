# Generated by Django 4.2.6 on 2023-12-29 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_rename_topics_name_webpage_topic_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topics',
            name='id',
        ),
        migrations.AlterField(
            model_name='topics',
            name='topic_name',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
