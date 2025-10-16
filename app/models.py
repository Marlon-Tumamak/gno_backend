from django.db import models

# Create your models here.

class TruckType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class AccountType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PlateNumber(models.Model):
    number = models.CharField(max_length=255)

    def __str__(self):
        return self.number
    
class RepairAndMaintenanceAccount(models.Model):
    account_number = models.CharField(max_length=255)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    plate_number = models.ForeignKey(PlateNumber, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    final_total = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=255)
    date = models.DateField()
    description = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)

    def __str__(self):
        return self.account_number

class InsuranceAccount(models.Model):
    account_number = models.CharField(max_length=255)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    plate_number = models.ForeignKey(PlateNumber, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    final_total = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=255)
    date = models.DateField()
    description = models.CharField(max_length=255)
    remarks = models.CharField(max_length=255)

    def __str__(self):
        return self.account_number

class FuelAccount(models.Model):
    account_number = models.CharField(max_length=255)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    plate_number = models.ForeignKey(PlateNumber, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    final_total = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=255)
    date = models.DateField()
    driver = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    liters = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    route = models.CharField(max_length=255)
    description = models.TextField()
    remarks = models.CharField(max_length=255)
    front_load = models.CharField(max_length=255)
    back_load = models.CharField(max_length=255)

    def __str__(self):
        return self.account_number

class TaxAccount(models.Model):
    account_number = models.CharField(max_length=255)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    plate_number = models.ForeignKey(PlateNumber, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    final_total = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    remarks = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return self.account_number

class AllowanceAccount(models.Model):
    account_number = models.CharField(max_length=255)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    plate_number = models.ForeignKey(PlateNumber, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    final_total = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField()
    remarks = models.CharField(max_length=255)

    def __str__(self):
        return self.account_number

class IncomeAccount(models.Model):
    account_number = models.CharField(max_length=255)
    truck_type = models.ForeignKey(TruckType, on_delete=models.CASCADE)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    plate_number = models.ForeignKey(PlateNumber, on_delete=models.CASCADE)
    debit = models.DecimalField(max_digits=10, decimal_places=2)
    credit = models.DecimalField(max_digits=10, decimal_places=2)
    final_total = models.DecimalField(max_digits=10, decimal_places=2)
    reference_number = models.CharField(max_length=255)
    date = models.DateField()
    driver = models.CharField(max_length=255)
    route = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    route = models.CharField(max_length=255)
    description = models.TextField()
    remarks = models.CharField(max_length=255)
    front_load = models.CharField(max_length=255)
    back_load = models.CharField(max_length=255)

    def __str__(self):
        return self.account_number
