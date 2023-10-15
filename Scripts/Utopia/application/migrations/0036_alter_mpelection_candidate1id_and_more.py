# Generated by Django 4.2.5 on 2023-10-11 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0035_ministerprimarydetails_ministernumberid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mpelection',
            name='Candidate1ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Candidate1ID', to='application.usersprimarydetails'),
        ),
        migrations.AlterField(
            model_name='mpelection',
            name='Candidate2ID',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Candidate2ID', to='application.usersprimarydetails'),
        ),
    ]