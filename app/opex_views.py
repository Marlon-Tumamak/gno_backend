from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Sum
from .models import TruckingAccount


class OPEXView(APIView):
    """
    GET: Get OPEX breakdown by account types with percentages
    """
    
    def get(self, request):
        try:
            # Get OPEX amounts by account types
            opex_data = {}
            
            # Insurance Expense - handle negative values
            insurance_amount = TruckingAccount.objects.filter(account_type='Insurance Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            opex_data['Insurance Expense'] = abs(float(insurance_amount))
            
            # Repairs and Maintenance Expense - handle negative values
            repairs_amount = TruckingAccount.objects.filter(account_type='Repairs and Maintenance Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            opex_data['Repairs and Maintenance Expense'] = abs(float(repairs_amount))
            
            # Taxes, Permits and Licenses Expense - handle negative values
            taxes_permits_amount = TruckingAccount.objects.filter(account_type='Taxes, Permits and Licenses Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            opex_data['Taxes, Permits and Licenses Expense'] = abs(float(taxes_permits_amount))
            
            # Salaries and Wages - handle negative values
            salaries_amount = TruckingAccount.objects.filter(account_type='Salaries and Wages').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            opex_data['Salaries and Wages'] = abs(float(salaries_amount))
            
            # Tax Expense - handle negative values
            tax_amount = TruckingAccount.objects.filter(account_type='Tax Expense').aggregate(
                total=Sum('final_total')
            )['total'] or 0
            opex_data['Tax Expense'] = abs(float(tax_amount))
            
            # Calculate total OPEX
            total_opex = sum(opex_data.values())
            
            # Calculate percentages
            opex_breakdown = []
            for account_type, amount in opex_data.items():
                percentage = (amount / total_opex * 100) if total_opex > 0 else 0
                opex_breakdown.append({
                    'account_type': account_type,
                    'amount': amount,
                    'percentage': round(percentage, 2)
                })
            
            # Sort by amount descending
            opex_breakdown.sort(key=lambda x: x['amount'], reverse=True)
            
            return Response({
                'opex_breakdown': opex_breakdown,
                'total_opex': total_opex,
                'summary': {
                    'total_categories': len(opex_breakdown),
                    'largest_category': opex_breakdown[0] if opex_breakdown else None,
                    'smallest_category': opex_breakdown[-1] if opex_breakdown else None
                }
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to fetch OPEX data: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
