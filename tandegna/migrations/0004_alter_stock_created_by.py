# Generated by Django 4.1.5 on 2023-04-05 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tandegna', '0003_alter_stock_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='created_by',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
