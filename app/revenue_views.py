from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from collections import defaultdict
from decimal import Decimal
from .models import TruckingAccount, AllowanceAccount, FuelAccount


class RevenueStreamsView(APIView):
    """
    GET: Get revenue and expense streams data
    """
    
    def get(self, request):
        try:
            # Get hauling income accounts from TruckingAccount
            hauling_accounts = TruckingAccount.objects.filter(account_type='Hauling Income')
            
            # Initialize revenue streams
            front_load_amount = Decimal('0.00')
            back_load_amount = Decimal('0.00')
            
            # Group hauling accounts by route, date, and reference number
            grouped_accounts = defaultdict(list)
            
            for account in hauling_accounts:
                # Skip if no route
                if not account.route or str(account.route).strip() == '' or str(account.route).lower() == 'nan':
                    continue
                
                key = (account.route, account.date, account.reference_number)
                grouped_accounts[key].append(account)
            
            # Process each group according to business rules
            for key, accounts in grouped_accounts.items():
                route, date, reference_number = key
                
                if len(accounts) == 1:
                    # Single entry - apply Strike logic
                    account = accounts[0]
                    amount = abs(float(account.credit)) if float(account.credit) != 0 else abs(float(account.debit))
                    front_load = account.front_load
                    back_load = account.back_load
                    
                    if front_load and 'Strike' in front_load:
                        # If front_load is Strike, amount goes to back_load
                        back_load_amount += Decimal(str(amount))
                    elif back_load and 'Strike' in back_load:
                        # If back_load is Strike, amount goes to front_load
                        front_load_amount += Decimal(str(amount))
                    else:
                        # Check if both loads exist
                        if front_load and back_load:
                            # Split amount between front and back
                            half_amount = Decimal(str(amount)) / 2
                            front_load_amount += half_amount
                            back_load_amount += half_amount
                        elif front_load:
                            front_load_amount += Decimal(str(amount))
                        elif back_load:
                            back_load_amount += Decimal(str(amount))
                else:
                    # Multiple entries - first is front_load, rest are back_load
                    for i, account in enumerate(accounts):
                        amount = abs(float(account.credit)) if float(account.credit) != 0 else abs(float(account.debit))
                        if i == 0:
                            front_load_amount += Decimal(str(amount))
                        else:
                            back_load_amount += Decimal(str(amount))
            
            # Calculate expense streams from TruckingAccount
            # Get allowance amounts (Driver's Allowance)
            allowance_amount = TruckingAccount.objects.filter(account_type='Driver\'s Allowance').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            
            # Get fuel amounts (Fuel and Oil)
            fuel_amount = TruckingAccount.objects.filter(account_type='Fuel and Oil').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            
            # Get OPEX amounts by account types - handle negative values
            insurance_amount = TruckingAccount.objects.filter(account_type='Insurance Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            
            repairs_amount = TruckingAccount.objects.filter(account_type='Repairs and Maintenance Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            
            taxes_permits_amount = TruckingAccount.objects.filter(account_type='Taxes, Permits and Licenses Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            
            salaries_amount = TruckingAccount.objects.filter(account_type='Salaries and Wages').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            
            tax_amount = TruckingAccount.objects.filter(account_type='Tax Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            
            # Calculate total OPEX (excluding Driver's Allowance and Fuel) - use absolute values
            total_opex = abs(float(insurance_amount)) + abs(float(repairs_amount)) + abs(float(taxes_permits_amount)) + abs(float(salaries_amount)) + abs(float(tax_amount))
            
            return Response({
                'revenue_streams': {
                    'front_load_amount': float(front_load_amount),
                    'back_load_amount': float(back_load_amount)
                },
                'expense_streams': {
                    'allowance': float(allowance_amount),
                    'add_allowance': 0,  # Additional allowance if needed
                    'fuel_amount': float(fuel_amount),
                    'add_fuel_amount': 0,  # Additional fuel if needed
                    'total_opex': total_opex
                }
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to fetch revenue streams data: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )



