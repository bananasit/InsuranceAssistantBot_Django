# Generated by Django 5.1.1 on 2024-10-03 09:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Policy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_number', models.CharField(max_length=50)),
                ('policyholder_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('premium_amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contract_id', models.CharField(max_length=50)),
                ('terms_and_conditions', models.TextField()),
                ('policy_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botapp.policy')),
            ],
        ),
        migrations.CreateModel(
            name='Claim',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claim_id', models.CharField(max_length=50)),
                ('date_of_claim', models.DateField()),
                ('amount_claimed', models.DecimalField(decimal_places=2, max_digits=10)),
                ('policy_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='botapp.policy')),
            ],
        ),
    ]
