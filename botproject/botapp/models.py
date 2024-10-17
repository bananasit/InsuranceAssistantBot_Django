from django.db import models

# Create your models here.

class Policy(models.Model):
    policy_number = models.CharField(max_length=50)
    policyholder_name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    premium_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Claim(models.Model):
    claim_id = models.CharField(max_length=50)
    policy_number = models.ForeignKey(Policy, on_delete=models.CASCADE)
    date_of_claim = models.DateField()
    amount_claimed = models.DecimalField(max_digits=10, decimal_places=2)

class Contract(models.Model):
    contract_id = models.CharField(max_length=50)
    policy_number = models.ForeignKey(Policy, on_delete=models.CASCADE)
    terms_and_conditions = models.TextField()

