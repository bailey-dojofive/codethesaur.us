# Generated by Django 3.2.6 on 2021-08-23 18:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteVisit',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('url', models.URLField(max_length=300)),
                ('user_agent', models.CharField(max_length=300)),
                ('referer', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='LookupData',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('language1', models.CharField(max_length=50)),
                ('language2', models.CharField(max_length=50)),
                ('structure', models.CharField(max_length=50)),
                ('site_visit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.sitevisit')),
            ],
        ),
    ]