# Generated by Django 4.2.7 on 2024-02-04 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MainForum', '0006_tagghost_alter_ghost_category_ghost_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ghost',
            name='img_url',
        ),
    ]
