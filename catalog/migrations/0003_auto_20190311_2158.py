# Generated by Django 2.1.7 on 2019-03-11 19:58

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20190311_2144'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('salary_amount', models.DecimalField(decimal_places=2, default=0, max_digits=15)),
                ('foto_employee', models.ImageField(default='', upload_to='static/images/')),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=120)),
            ],
            options={
                'verbose_name': 'Должность сотрудника',
                'verbose_name_plural': 'Должности сотрудников',
            },
        ),
        migrations.RemoveField(
            model_name='genre',
            name='parent',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
        migrations.AddField(
            model_name='employee',
            name='employee_position',
            field=models.ForeignKey(blank=True, null=True, on_delete=True, to='catalog.Position'),
        ),
        migrations.AddField(
            model_name='employee',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='catalog.Employee'),
        ),
    ]