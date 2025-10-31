from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TruckingAccount
from django.db.models import Q

class AccountsDetailView(APIView):
    """
    GET: Get detailed account entries from TruckingAccount model
    """
    def get(self, request):
        try:
            # Define account type mappings
            account_mappings = {
                'repair_maintenance': {
                    'account_type': 'Repairs and Maintenance Expense',
                    'name': 'Repair & Maintenance'
                },
                'insurance': {
                    'account_type': 'Insurance Expense',
                    'name': 'Insurance'
                },
                'fuel': {
                    'account_type': 'Fuel and Oil',
                    'name': 'Fuel & Oil'
                },
                'tax': {
                    'account_type': 'Tax Expense',
                    'name': 'Tax Account'
                },
                'allowance': {
                    'account_type': 'Driver\'s Allowance',
                    'name': 'Allowance Account'
                },
                'income': {
                    'account_type': 'Hauling Income',
                    'name': 'Income Account'
                },
                'salaries_wages': {
                    'account_type': 'Salaries and Wages',
                    'name': 'Salaries and Wages'
                },
                'taxes_permits_licenses': {
                    'account_type': 'Taxes, Permits and Licenses Expense',
                    'name': 'Taxes, Permits and Licenses'
                }
            }
            
            accounts_data = {}
            
            for key, mapping in account_mappings.items():
                # Get all records for this account type
                records = TruckingAccount.objects.filter(account_type=mapping['account_type'])
                
                # Convert to the format expected by frontend
                entries = []
                for record in records:
                    # Handle driver - can be ForeignKey object or None
                    driver_data = None
                    if record.driver:
                        if hasattr(record.driver, 'name'):
                            # It's a Driver model instance
                            driver_data = {
                                'id': record.driver.id,
                                'name': record.driver.name
                            }
                        else:
                            # It's already a string
                            driver_data = record.driver
                    
                    # Handle route - can be ForeignKey object or None
                    route_data = None
                    if record.route:
                        if hasattr(record.route, 'name'):
                            # It's a Route model instance
                            route_data = {
                                'id': record.route.id,
                                'name': record.route.name
                            }
                        else:
                            # It's already a string
                            route_data = record.route
                    
                    entry = {
                        'id': record.id,
                        'account_number': record.account_number or '',
                        'truck_type': record.truck_type or '',
                        'account_type': record.account_type,
                        'plate_number': record.plate_number or '',
                        'debit': float(record.debit or 0),
                        'credit': float(record.credit or 0),
                        'final_total': float(record.final_total or 0),
                        'reference_number': record.reference_number or '',
                        'date': record.date.strftime('%Y-%m-%d') if record.date else '',
                        'description': record.description or '',
                        'remarks': record.remarks or '',
                        'driver': driver_data,
                        'route': route_data,
                        'liters': float(record.quantity or 0) if record.quantity else None,
                        'price': float(record.price or 0) if record.price else None,
                        'front_load': record.front_load or '',
                        'back_load': record.back_load or '',
                        'quantity': float(record.quantity or 0) if record.quantity else None
                    }
                    entries.append(entry)
                
                accounts_data[key] = {
                    'name': mapping['name'],
                    'entries': entries
                }
            
            return Response({
                'accounts': accounts_data
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to fetch accounts detail data: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )