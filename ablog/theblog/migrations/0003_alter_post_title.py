# Generated by Django 3.2.7 on 2021-09-25 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_post_title_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='My Blog', max_length=255),
        ),
    ]