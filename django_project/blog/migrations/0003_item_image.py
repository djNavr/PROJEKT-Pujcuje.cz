# Generated by Django 5.0.3 on 2024-05-22 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_category_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='item_pics'),
        ),
    ]
