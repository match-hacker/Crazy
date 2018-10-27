# Generated by Django 2.1.2 on 2018-10-20 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_task_tasklogdetail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='task_Type',
            new_name='task_type',
        ),
        migrations.AddField(
            model_name='tasklogdetail',
            name='status',
            field=models.SmallIntegerField(choices=[(0, 'initialized'), (1, 'success'), (2, 'failed'), (3, 'timeout')], default=0),
        ),
    ]