# Generated by Django 2.2 on 2019-08-07 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_ordersummary'),
    ]

    operations = [
        migrations.DeleteModel(
            name='OrderSummary',
        ),
        migrations.CreateModel(
            name='ReviewSummary',
            fields=[
            ],
            options={
                'verbose_name': 'Review Summary',
                'verbose_name_plural': 'Reviews Summary',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('core.review',),
        ),
    ]
