# Generated by Django 4.1 on 2022-08-20 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_donor_form_delete_form_edonator'),
    ]

    operations = [
        migrations.CreateModel(
            name='extendeduser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('aadhaar_no', models.CharField(max_length=20, null=True)),
                ('email', models.CharField(max_length=12, null=True)),
                ('password', models.CharField(max_length=20, null=True)),
                ('username', models.CharField(max_length=20, null=True)),
            ],
        ),
        migrations.RenameField(
            model_name='donor_form',
            old_name='Contact_no',
            new_name='contact_no',
        ),
    ]
