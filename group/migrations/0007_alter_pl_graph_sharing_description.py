# Generated by Django 3.2.9 on 2024-06-19 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0006_alter_pl_graph_sharing_chart_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pl_graph_sharing',
            name='description',
            field=models.CharField(max_length=1500),
        ),
    ]