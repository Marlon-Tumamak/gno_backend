from rest_framework import serializers
from .models import RepairAndMaintenanceAccount, InsuranceAccount, FuelAccount, TaxAccount, AllowanceAccount, IncomeAccount, TruckType, AccountType, PlateNumber


class TruckTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TruckType
        fields = ['id', 'name']
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']

class AccountTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = ['id', 'name']
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']

class PlateNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlateNumber
        fields = ['id', 'number']
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']

class RepairAndMaintenanceAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = RepairAndMaintenanceAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'description',
            'remarks',
        ]
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']

class InsuranceAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = InsuranceAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'description',
            'remarks',
        ]
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']

class FuelAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = FuelAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'liters',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']

class TaxAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = TaxAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'description',
            'remarks',
            'price',
            'quantity',
        ]
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']

class AllowanceAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = AllowanceAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'description',
            'remarks',
        ]
        read_only_fields = ['id']


class IncomeAccountSerializer(serializers.ModelSerializer):
    truck_type_name = serializers.CharField(source='truck_type.name', read_only=True)
    account_type_name = serializers.CharField(source='account_type.name', read_only=True)
    plate_number_display = serializers.CharField(source='plate_number.number', read_only=True)
    
    class Meta:
        model = IncomeAccount
        fields = [
            'id',
            'account_number',
            'truck_type',
            'truck_type_name',
            'account_type',
            'account_type_name',
            'plate_number',
            'plate_number_display',
            'debit',
            'credit',
            'final_total',
            'reference_number',
            'date',
            'driver',
            'route',
            'quantity',
            'price',
            'description',
            'remarks',
            'front_load',
            'back_load',
        ]
        read_only_fields = ['id']
