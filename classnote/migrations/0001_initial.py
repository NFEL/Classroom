# Generated by Django 3.1 on 2020-09-01 04:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='classroom',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('classname', models.CharField(max_length=50, null=True)),
                ('code', models.CharField(default='passwd', max_length=6)),
                ('creator', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE,
                                              related_name='creator', to=settings.AUTH_USER_MODEL)),
                ('user_profile', models.ManyToManyField(to='accounts.UserProfile')),
            ],
        ),
    ]
