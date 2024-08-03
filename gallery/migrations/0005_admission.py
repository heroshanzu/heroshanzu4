# Generated by Django 5.0.2 on 2024-08-02 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_subscriber_submitted_at'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nemis', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('middle_name', models.CharField(max_length=40)),
                ('surname', models.CharField(max_length=40)),
                ('date_of_birth', models.DateField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('grade_level', models.CharField(choices=[('pp1', 'Pre Primary 1'), ('pp2', 'Pre Primary 2'), ('grade1', 'Grade 1'), ('grade2', 'Grade 2'), ('grade3', 'Grade 3'), ('grade4', 'Grade 4'), ('grade5', 'Grade 5'), ('grade6', 'Grade 6'), ('grade7', 'Grade 7'), ('grade8', 'Grade 8'), ('grade9', 'Grade 9')], max_length=40)),
                ('current_school', models.CharField(blank=True, max_length=200)),
                ('about_us', models.TextField(max_length=200)),
                ('parent_name', models.CharField(max_length=100)),
                ('parent_email', models.EmailField(max_length=254)),
                ('parent_phone', models.CharField(max_length=15)),
                ('parent_relation', models.CharField(choices=[('parent', 'Parent'), ('guardianr', 'Guardian'), ('other', 'Other')], max_length=20)),
                ('parent_residence', models.CharField(max_length=40)),
            ],
        ),
    ]
