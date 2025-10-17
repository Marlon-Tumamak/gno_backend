from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from collections import defaultdict
import re
from .models import (
    RepairAndMaintenanceAccount, 
    InsuranceAccount, 
    FuelAccount, 
    TaxAccount, 
    AllowanceAccount, 
    IncomeAccount
)


def parse_remarks(remarks):
    """
    Parse remarks to extract driver, route, front_load, and back_load
    Format: "LRO: 140Liters Fuel and Oil NGS-4359 Francis Ariglado:PAG-ILIGAN: Strike/Cement:"
    """
    if not remarks:
        return None, None, None, None
    
    # Known drivers list
    drivers = [
        'Edgardo Agapay', 'Romel Bantilan', 'Reynaldo Rizalda', 'Francis Ariglado',
        'Roque Oling', 'Pablo Hamo', 'Albert Saavedra', 'Jimmy Oclarit', 'Nicanor',
        'Arnel Duhilag', 'Benjamin Aloso', 'Roger', 'Joseph Bahan', 'Doming'
    ]
    
    # Known routes list
    routes = [
        'PAG-CDO', 'PAG-ILIGAN', 'Strike Holcim', 'PAG-ILIGAN STRIKE', 'PAG-CDO (CARGILL)',
        'PAG-CDO STRIKE', 'PAG-BUK', 'PAG-DIPLAHAN', 'PAG-MARANDING', 'PAG-COTABATO',
        'PAG-ZMBGA', 'Pag-COTABATO', 'Pag-AURORA', 'PAG-DIPOLOG', 'PAG-MOLAVE',
        'PAGADIAN', 'PAG-DIMATALING', 'PAG-DINAS', 'PAG-LABANGAN', 'PAG-MIDSALIP',
        'PAGADIAN', 'PAG-OZAMIS', 'PAG-OSMENIA', 'PAG-DUMINGAG', 'PAG-KUMALARANG',
        'PAG-MAHAYAG', 'PAG-TAMBULIG', 'PAG-SURIGAO', 'PAG-BUYOGAN', 'PAG-SAN PABLO',
        'PAGADIAN-OPEX', 'CDO-OPEX', 'PAG-BAYOG', 'PAG-LAKEWOOD', 'PAG-BUUG'
    ]
    
    driver = None
    route = None
    front_load = None
    back_load = None
    
    # Find driver
    for known_driver in drivers:
        if known_driver in remarks:
            driver = known_driver
            break
    
    # Find route
    for known_route in routes:
        if known_route in remarks:
            route = known_route
            break
    
    # Find front_load/back_load pattern (format: "value/value")
    load_pattern = r'([^:]+)/([^:]+):'
    load_match = re.search(load_pattern, remarks)
    if load_match:
        front_load = load_match.group(1).strip()
        back_load = load_match.group(2).strip()
    
    return driver, route, front_load, back_load


class TripsView(APIView):
    """
    GET: Get consolidated trips data grouped by plate number and date
    """
    
    def get(self, request):
        try:
            # Dictionary to store trips grouped by (plate_number, date)
            trips = defaultdict(lambda: {
                'account_number': '',
                'plate_number': '',
                'date': '',
                'trip_route': '',
                'driver': '',
                'allowance': 0,
                'reference_number': '',
                'fuel_liters': 0,
                'fuel_price': 0,
                'front_load': '',
                'front_load_reference_number': '',
                'front_load_amount': 0,
                'back_load_reference_number': '',
                'back_load_amount': 0,
                'front_and_back_load_amount': 0,
                'remarks': '',
                'insurance_expense': 0,
                'repairs_maintenance_expense': 0,
                'taxes_permits_licenses_expense': 0,
                'salaries_allowance': 0
            })
            
            # Process Income Accounts for front_load and back_load
            income_accounts = IncomeAccount.objects.select_related('plate_number').all()
            
            # Group income by plate, date, and reference number
            income_grouped = defaultdict(list)
            for account in income_accounts:
                key = (account.plate_number.number, account.date, account.reference_number)
                income_grouped[key].append(account)
            
            # Process each income group
            for (plate_num, date, ref_num), accounts in income_grouped.items():
                trip_key = (plate_num, date)
                
                if len(accounts) == 1:
                    # Single entry - check if front_load has value
                    account = accounts[0]
                    front_load_value = str(account.front_load).strip().lower()
                    back_load_value = str(account.back_load).strip().lower()
                    
                    trips[trip_key]['account_number'] = account.account_number
                    trips[trip_key]['plate_number'] = plate_num
                    trips[trip_key]['date'] = date.strftime('%Y-%m-%d')
                    trips[trip_key]['trip_route'] = account.route
                    trips[trip_key]['driver'] = account.driver
                    trips[trip_key]['reference_number'] = ref_num
                    trips[trip_key]['front_load'] = account.front_load
                    trips[trip_key]['remarks'] = account.remarks
                    
                    # Check if front_load has a meaningful value (not empty, 'n', 'nan', etc.)
                    if (front_load_value and front_load_value != '' and 
                        front_load_value not in ['n', 'nan', 'none', '0'] and
                        back_load_value and back_load_value != '' and 
                        back_load_value not in ['nan', 'none', '0']):
                        # Both front_load and back_load have meaningful values - divide by 2
                        half_amount = float(account.final_total) / 2
                        trips[trip_key]['front_load_amount'] += half_amount
                        trips[trip_key]['back_load_amount'] += half_amount
                        trips[trip_key]['front_load_reference_number'] = ref_num
                        trips[trip_key]['back_load_reference_number'] = ref_num
                    elif (back_load_value and back_load_value != '' and 
                          back_load_value not in ['nan', 'none', '0']):
                        # Only back_load has value - all goes to back_load, front_load = 0
                        trips[trip_key]['front_load_amount'] = 0  # Explicitly set to 0
                        trips[trip_key]['back_load_amount'] += float(account.final_total)
                        trips[trip_key]['back_load_reference_number'] = ref_num
                    elif (front_load_value and front_load_value != '' and 
                          front_load_value not in ['n', 'nan', 'none', '0']):
                        # Only front_load has value - all goes to front_load, back_load = 0
                        trips[trip_key]['front_load_amount'] += float(account.final_total)
                        trips[trip_key]['back_load_amount'] = 0  # Explicitly set to 0
                        trips[trip_key]['front_load_reference_number'] = ref_num
                    else:
                        # Neither has meaningful value - skip this entry
                        continue
                else:
                    # Multiple entries - first is front_load, rest are back_load
                    for i, account in enumerate(accounts):
                        trips[trip_key]['account_number'] = account.account_number
                        trips[trip_key]['plate_number'] = plate_num
                        trips[trip_key]['date'] = date.strftime('%Y-%m-%d')
                        trips[trip_key]['trip_route'] = account.route
                        trips[trip_key]['driver'] = account.driver
                        trips[trip_key]['front_load'] = account.front_load
                        trips[trip_key]['remarks'] = account.remarks
                        
                        if i == 0:
                            # First entry is front_load
                            trips[trip_key]['front_load_amount'] += float(account.final_total)
                            trips[trip_key]['front_load_reference_number'] = ref_num
                        else:
                            # Subsequent entries are back_load
                            trips[trip_key]['back_load_amount'] += float(account.final_total)
                            trips[trip_key]['back_load_reference_number'] = ref_num
            
            # Process Fuel Accounts
            fuel_accounts = FuelAccount.objects.select_related('plate_number').all()
            for account in fuel_accounts:
                trip_key = (account.plate_number.number, account.date)
                if trip_key in trips or not trips[trip_key]['plate_number']:
                    trips[trip_key]['plate_number'] = account.plate_number.number
                    trips[trip_key]['date'] = account.date.strftime('%Y-%m-%d')
                    trips[trip_key]['fuel_liters'] += float(account.liters or 0)
                    trips[trip_key]['fuel_price'] = float(account.price or 0)
                    if not trips[trip_key]['driver']:
                        trips[trip_key]['driver'] = account.driver
                    if not trips[trip_key]['trip_route']:
                        trips[trip_key]['trip_route'] = account.route
            
            # Process Allowance Accounts
            allowance_accounts = AllowanceAccount.objects.select_related('plate_number').all()
            for account in allowance_accounts:
                trip_key = (account.plate_number.number, account.date)
                if trip_key in trips or not trips[trip_key]['plate_number']:
                    trips[trip_key]['plate_number'] = account.plate_number.number
                    trips[trip_key]['date'] = account.date.strftime('%Y-%m-%d')
                    trips[trip_key]['allowance'] += float(account.final_total)
                    trips[trip_key]['salaries_allowance'] += float(account.final_total)
            
            # Process Insurance Accounts
            insurance_accounts = InsuranceAccount.objects.select_related('plate_number').all()
            for account in insurance_accounts:
                trip_key = (account.plate_number.number, account.date)
                if trip_key in trips or not trips[trip_key]['plate_number']:
                    trips[trip_key]['plate_number'] = account.plate_number.number
                    trips[trip_key]['date'] = account.date.strftime('%Y-%m-%d')
                    trips[trip_key]['insurance_expense'] += float(account.final_total)
            
            # Process Repair and Maintenance Accounts
            repair_accounts = RepairAndMaintenanceAccount.objects.select_related('plate_number').all()
            for account in repair_accounts:
                trip_key = (account.plate_number.number, account.date)
                if trip_key in trips or not trips[trip_key]['plate_number']:
                    trips[trip_key]['plate_number'] = account.plate_number.number
                    trips[trip_key]['date'] = account.date.strftime('%Y-%m-%d')
                    trips[trip_key]['repairs_maintenance_expense'] += float(account.final_total)
            
            # Process Tax Accounts
            tax_accounts = TaxAccount.objects.select_related('plate_number').all()
            for account in tax_accounts:
                trip_key = (account.plate_number.number, account.date)
                if trip_key in trips or not trips[trip_key]['plate_number']:
                    trips[trip_key]['plate_number'] = account.plate_number.number
                    trips[trip_key]['date'] = account.date.strftime('%Y-%m-%d')
                    trips[trip_key]['taxes_permits_licenses_expense'] += float(account.final_total)
            
            # Calculate front_and_back_load_amount for each trip
            # Only include trips that have a route
            trips_list = []
            for trip_data in trips.values():
                # Skip trips without a route or with 'nan' as route
                route = str(trip_data['trip_route']).strip().lower()
                if not trip_data['trip_route'] or route == '' or route == 'nan':
                    continue
                    
                trip_data['front_and_back_load_amount'] = (
                    trip_data['front_load_amount'] + trip_data['back_load_amount']
                )
                trips_list.append(trip_data)
            
            # Sort by date and plate number
            trips_list.sort(key=lambda x: (x['date'], x['plate_number']))
            
            return Response({
                'trips': trips_list,
                'total_trips': len(trips_list)
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to fetch trips data: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
