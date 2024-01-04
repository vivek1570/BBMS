# Generated by Django 4.2.7 on 2023-12-03 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='p_add',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_age',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_b_group',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='p_phone',
            field=models.CharField(max_length=15),
        ),
    ]