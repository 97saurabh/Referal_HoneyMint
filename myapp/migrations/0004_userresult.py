# Generated by Django 2.2.1 on 2020-04-16 13:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0003_delete_referal'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('point', models.IntegerField(max_length=200)),
                ('refer_by', models.ForeignKey(on_delete='CASCADE', related_name='result', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
