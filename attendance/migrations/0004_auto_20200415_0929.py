# Generated by Django 3.0.5 on 2020-04-15 06:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('attendance', '0003_auto_20200414_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('number',),
            },
        ),
        migrations.AlterModelOptions(
            name='employee',
            options={'ordering': ('work_id',)},
        ),
        migrations.AddField(
            model_name='attendance',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='image',
            field=models.ImageField(default='media/avatar.jpg', upload_to='media/image_uploads/'),
        ),
        migrations.AddField(
            model_name='employee',
            name='level',
            field=models.CharField(blank=True, choices=[('intern', 'Intern'), ('junior', 'Junior'), ('senior', 'Senior')], max_length=8),
        ),
        migrations.AddField(
            model_name='employee',
            name='phone',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='work_id',
            field=models.CharField(default=1, max_length=8, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='employee',
            name='head_of_department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Head_of_department',
        ),
    ]
