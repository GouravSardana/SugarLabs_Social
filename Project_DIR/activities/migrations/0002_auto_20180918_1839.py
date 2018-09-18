# Generated by Django 2.0.6 on 2018-09-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activities',
            name='category',
            field=models.CharField(choices=[('Communications and Language', 'Communications and Language'), ('Search & Discovery', 'Search & Discovery'), ('Documents', 'Documents'), ('News', 'News'), ('Chat, mail and talk', 'Chat, mail and talk'), ('Media creation', 'Media creation'), ('Programming', 'Programming'), ('Maths & Science', 'Maths & Science'), ('Maps & Geography', 'Maps & Geography'), ('Media players', 'Media players'), ('Games', 'Games'), ('Teacher tools', 'Teacher tools'), ('Utilities', 'Utilities'), ('Web', 'Web'), ('collections', 'collections'), ('NA', 'NA')], default='NA', max_length=100),
        ),
    ]
