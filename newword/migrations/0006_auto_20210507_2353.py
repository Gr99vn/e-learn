# Generated by Django 3.2.2 on 2021-05-07 16:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('newword', '0005_auto_20210507_2209'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='lesson',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='newword.lesson'),
        ),
        migrations.AddField(
            model_name='test',
            name='num_of_quest',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
