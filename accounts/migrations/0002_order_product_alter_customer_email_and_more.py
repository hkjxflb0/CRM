# Generated by Django 4.1.7 on 2023-03-29 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Pending', 'Pending'), ('Out for delivery', 'Out for delivery'), ('Delivered', 'Delivered')], max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('price', models.FloatField(null=True)),
                ('category', models.CharField(choices=[('iNDOOR', 'INDOOR'), ('Out Door', 'Out Door')], max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('data', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
