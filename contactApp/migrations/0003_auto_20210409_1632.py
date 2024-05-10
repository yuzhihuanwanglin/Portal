# Generated by Django 3.1.7 on 2021-04-09 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contactApp', '0002_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='status',
            field=models.IntegerField(choices=[(1, '未审'), (2, '通过'), (3, '未通过')], default=1, max_length=5, verbose_name='面试成绩'),
        ),
    ]