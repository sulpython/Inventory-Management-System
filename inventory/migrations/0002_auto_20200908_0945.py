# Generated by Django 3.1.1 on 2020-09-08 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='desktop',
            name='location',
            field=models.CharField(default='LOCATION', max_length=10),
        ),
        migrations.AlterField(
            model_name='desktop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('OUT OF ORDER', 'Item is not working properly'), ('IN-USE', 'Item is being used by employee')], default='AVAILABLE', max_length=15),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='location',
            field=models.CharField(default='LOCATION', max_length=10),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('OUT OF ORDER', 'Item is not working properly'), ('IN-USE', 'Item is being used by employee')], default='AVAILABLE', max_length=15),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='location',
            field=models.CharField(default='LOCATION', max_length=10),
        ),
        migrations.AlterField(
            model_name='laptop',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('OUT OF ORDER', 'Item is not working properly'), ('IN-USE', 'Item is being used by employee')], default='AVAILABLE', max_length=15),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='location',
            field=models.CharField(default='LOCATION', max_length=10),
        ),
        migrations.AlterField(
            model_name='mobile',
            name='status',
            field=models.CharField(choices=[('AVAILABLE', 'Item ready to be purchased'), ('OUT OF ORDER', 'Item is not working properly'), ('IN-USE', 'Item is being used by employee')], default='AVAILABLE', max_length=15),
        ),
    ]
