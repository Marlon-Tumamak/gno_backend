from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import TruckingAccount
import pandas as pd
import re

class TruckingAccountUploadView(APIView):
    """
    POST: Upload Excel file and bulk create trucking accounts with automatic parsing
    """
    def post(self, request):
        try:
            if 'file' not in request.FILES:
                return Response(
                    {'error': 'No file provided'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            file = request.FILES['file']
            
            # Read Excel file
            df = pd.read_excel(file)
            
            # Clean column names
            df.columns = df.columns.str.strip()
            
            # Map Excel columns to model fields
            column_mapping = {
                'AccountNumber': 'account_number',
                'AccountType': 'account_type',
                'TruckType': 'truck_type',
                'PlateNumber': 'plate_number',
                'Description': 'description',
                'Debit': 'debit',
                'Credit': 'credit',
                'FinalTotal': 'final_total',
                'Remarks': 'remarks',
                'ReferenceNumber': 'reference_number',
                'Date': 'date',
                'Quantity': 'quantity',
                'Price': 'price',
                'Driver': 'driver',
                'Route': 'route',
                'Front_Load': 'front_load',
                'Back_Load': 'back_load'
            }
            
            # Rename columns
            df = df.rename(columns=column_mapping)
            
            # Initialize parsing statistics
            parsing_stats = {
                'total_rows': len(df),
                'drivers_extracted': 0,
                'routes_extracted': 0,
                'loads_extracted': 0,
                'valid_rows': 0
            }
            
            # Process each row
            created_count = 0
            errors = []
            
            for index, row in df.iterrows():
                try:
                    # Skip empty rows
                    if row.isnull().all():
                        continue
                    
                    # Count valid data
                    if row.get('driver') and row.get('driver') != '':
                        parsing_stats['drivers_extracted'] += 1
                    if row.get('route') and row.get('route') != '':
                        parsing_stats['routes_extracted'] += 1
                    if row.get('front_load') and row.get('front_load') != '':
                        parsing_stats['loads_extracted'] += 1
                    
                    parsing_stats['valid_rows'] += 1
                    
                    # Create TruckingAccount instance
                    account = TruckingAccount(
                        account_number=row.get('account_number', ''),
                        account_type=row.get('account_type', ''),
                        truck_type=row.get('truck_type', ''),
                        plate_number=row.get('plate_number', '') if row.get('plate_number') != '' else None,
                        description=row.get('description', ''),
                        debit=row.get('debit', 0),
                        credit=row.get('credit', 0),
                        final_total=row.get('final_total', 0),
                        remarks=row.get('remarks', ''),
                        reference_number=row.get('reference_number', '') if row.get('reference_number') != '' else None,
                        date=row.get('date') if not pd.isna(row.get('date')) else None,
                        quantity=row.get('quantity') if not pd.isna(row.get('quantity')) and row.get('quantity') != 0 else None,
                        price=row.get('price') if not pd.isna(row.get('price')) and row.get('price') != 0 else None,
                        driver=row.get('driver', '') if row.get('driver') != '' else None,
                        route=row.get('route', '') if row.get('route') != '' else None,
                        front_load=row.get('front_load', '') if row.get('front_load') != '' else None,
                        back_load=row.get('back_load', '') if row.get('back_load') != '' else None,
                    )
                    
                    account.save()
                    created_count += 1
                    
                except Exception as e:
                    errors.append(f"Row {index + 1}: {str(e)}")
                    continue
            
            return Response({
                'message': f'Successfully created {created_count} trucking accounts',
                'created_count': created_count,
                'parsing_stats': parsing_stats,
                'errors': errors[:10] if errors else []  # Show first 10 errors
            }, status=status.HTTP_201_CREATED)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to process file: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )


class TruckingAccountPreviewView(APIView):
    """
    POST: Preview Excel file data without saving to database - Shows ALL data with proper field extraction
    """
    def post(self, request):
        try:
            if 'file' not in request.FILES:
                return Response(
                    {'error': 'No file provided'},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            file = request.FILES['file']
            
            # Read Excel file
            df = pd.read_excel(file)
            
            # Clean column names
            df.columns = df.columns.str.strip()
            
            # Debug: Print available columns
            print(f"Available columns: {list(df.columns)}")
            
            # Map Excel columns to model fields (handle various column name formats)
            column_mapping = {
                'AccountNumber': 'account_number',
                'Account_Number': 'account_number',
                'ACCOUNT_NUMBER': 'account_number',
                'AccountType': 'account_type',
                'Account_Type': 'account_type',
                'ACCOUNT_TYPE': 'account_type',
                'TruckType': 'truck_type',
                'Truck_Type': 'truck_type',
                'TRUCK_TYPE': 'truck_type',
                'PlateNumber': 'plate_number',
                'Plate_Number': 'plate_number',
                'PLATE_NUMBER': 'plate_number',
                'Description': 'description',
                'DESCRIPTION': 'description',
                'Debit': 'debit',
                'DEBIT': 'debit',
                'Credit': 'credit',
                'CREDIT': 'credit',
                'FinalTotal': 'final_total',
                'Final_Total': 'final_total',
                'FINAL_TOTAL': 'final_total',
                'FINAL_TC': 'final_total',
                'Remarks': 'remarks',
                'REMARKS': 'remarks',
                'ReferenceNumber': 'reference_number',
                'Reference_Number': 'reference_number',
                'REFERENCE_NUMBER': 'reference_number',
                'Date': 'date',
                'DATE': 'date',
                'Quantity': 'quantity',
                'QUANTITY': 'quantity',
                'Price': 'price',
                'PRICE': 'price',
                'Driver': 'driver',
                'DRIVER': 'driver',
                'Route': 'route',
                'ROUTE': 'route',
                'Front_Load': 'front_load',
                'Front Load': 'front_load',
                'FRONT_LOAD': 'front_load',
                'Back_Load': 'back_load',
                'Back Load': 'back_load',
                'BACK_LOAD': 'back_load'
            }
            
            # Rename columns
            df = df.rename(columns=column_mapping)
            
            # Debug: Print mapped columns
            print(f"Mapped columns: {list(df.columns)}")
            
            # Initialize parsing statistics
            parsing_stats = {
                'total_rows': len(df),
                'drivers_extracted': 0,
                'routes_extracted': 0,
                'loads_extracted': 0,
                'valid_rows': 0
            }
            
            # Process each row for preview
            preview_data = []
            errors = []
            
            for index, row in df.iterrows():
                try:
                    # Skip empty rows
                    if row.isnull().all():
                        continue
                    
                    # Count valid data
                    if row.get('driver') and str(row.get('driver')).strip() != '' and str(row.get('driver')).lower() != 'nan':
                        parsing_stats['drivers_extracted'] += 1
                    if row.get('route') and str(row.get('route')).strip() != '' and str(row.get('route')).lower() != 'nan':
                        parsing_stats['routes_extracted'] += 1
                    if row.get('front_load') and str(row.get('front_load')).strip() != '' and str(row.get('front_load')).lower() != 'nan':
                        parsing_stats['loads_extracted'] += 1
                    
                    parsing_stats['valid_rows'] += 1
                    
                    # Prepare preview data (convert to dict for JSON serialization)
                    preview_row = {
                        'account_number': str(row.get('account_number', '')),
                        'account_type': str(row.get('account_type', '')),
                        'truck_type': str(row.get('truck_type', '')),
                        'plate_number': str(row.get('plate_number', '')) if row.get('plate_number') != '' and str(row.get('plate_number')).lower() != 'nan' else None,
                        'description': str(row.get('description', '')),
                        'debit': float(row.get('debit', 0)) if not pd.isna(row.get('debit')) else 0,
                        'credit': float(row.get('credit', 0)) if not pd.isna(row.get('credit')) else 0,
                        'final_total': float(row.get('final_total', 0)) if not pd.isna(row.get('final_total')) else 0,
                        'remarks': str(row.get('remarks', '')),
                        'reference_number': str(row.get('reference_number', '')) if row.get('reference_number') != '' and str(row.get('reference_number')).lower() != 'nan' else None,
                        'date': str(row.get('date')) if not pd.isna(row.get('date')) else None,
                        'quantity': float(row.get('quantity')) if not pd.isna(row.get('quantity')) and row.get('quantity') != 0 else None,
                        'price': float(row.get('price')) if not pd.isna(row.get('price')) and row.get('price') != 0 else None,
                        'driver': str(row.get('driver', '')) if row.get('driver') != '' and str(row.get('driver')).lower() != 'nan' else None,
                        'route': str(row.get('route', '')) if row.get('route') != '' and str(row.get('route')).lower() != 'nan' else None,
                        'front_load': str(row.get('front_load', '')) if row.get('front_load') != '' and str(row.get('front_load')).lower() != 'nan' else None,
                        'back_load': str(row.get('back_load', '')) if row.get('back_load') != '' and str(row.get('back_load')).lower() != 'nan' else None,
                    }
                    
                    preview_data.append(preview_row)
                    
                except Exception as e:
                    errors.append(f"Row {index + 1}: {str(e)}")
                    continue
            
            return Response({
                'message': f'Preview generated for {len(preview_data)} trucking accounts',
                'preview_data': preview_data,  # Show ALL data, not limited to 50 rows
                'parsing_stats': parsing_stats,
                'errors': errors[:10] if errors else []  # Show first 10 errors
            }, status=status.HTTP_200_OK)
            
        except Exception as e:
            return Response(
                {'error': f'Failed to process file: {str(e)}'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
