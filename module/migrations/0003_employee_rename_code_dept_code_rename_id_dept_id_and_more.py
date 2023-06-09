# Generated by Django 4.1.7 on 2023-04-30 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0002_alter_dept_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('ID', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('ECode', models.CharField(max_length=255)),
                ('Name', models.CharField(max_length=255)),
                ('DOB', models.DateField()),
                ('Dept', models.CharField(max_length=255)),
                ('salary', models.BigIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='dept',
            old_name='code',
            new_name='Code',
        ),
        migrations.RenameField(
            model_name='dept',
            old_name='id',
            new_name='ID',
        ),
        migrations.RenameField(
            model_name='dept',
            old_name='name',
            new_name='Name',
        ),
        migrations.AddField(
            model_name='dept',
            name='Create_Date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='dept',
            name='Create_user',
            field=models.TextField(null=True),
        ),
    ]
