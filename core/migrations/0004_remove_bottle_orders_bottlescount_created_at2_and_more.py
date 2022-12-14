# Generated by Django 4.1 on 2022-08-25 21:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_bottlescount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bottle',
            name='orders',
        ),
        migrations.AddField(
            model_name='bottlescount',
            name='created_at2',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата и время заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bottlescount',
            name='finished',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='bottlescount',
            name='updated_at2',
            field=models.DateTimeField(auto_now=True, verbose_name='Дата и время изменения заказа'),
        ),
        migrations.AlterField(
            model_name='bottlescount',
            name='bottle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bottle', to='core.bottle'),
        ),
    ]
