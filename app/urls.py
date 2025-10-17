from django.urls import path
from .views import (
    TruckTypeListView,
    TruckTypeDetailView,
    AccountTypeListView,
    AccountTypeDetailView,
    PlateNumberListView,
    PlateNumberDetailView,
    RepairAndMaintenanceAccountListView,
    RepairAndMaintenanceAccountDetailView,
    RepairAndMaintenanceUploadView,
    InsuranceAccountListView,
    InsuranceAccountDetailView,
    InsuranceAccountUploadView,
    FuelAccountListView,
    FuelAccountDetailView,
    FuelAccountUploadView,
    TaxAccountListView,
    TaxAccountDetailView,
    TaxAccountUploadView,
    AllowanceAccountListView,
    AllowanceAccountDetailView,
    AllowanceAccountUploadView,
    IncomeAccountListView,
    IncomeAccountDetailView,
    IncomeAccountUploadView,
    TruckingAccountListView,
    TruckingAccountDetailView,
    TruckingAccountUploadView,
    DriversSummaryView,
)
from .revenue_views import RevenueStreamsView
from .accounts_views import AccountsSummaryView
from .accounts_detail_views import AccountsDetailView
from .trips_views import TripsView
from .trucking_summary_views import (
    TruckingDriversSummaryView,
    TruckingRevenueStreamsView,
    TruckingAccountsSummaryView,
    TruckingTripsSummaryView
)
from .salary_views import SalaryAccountListView, SalaryAccountDetailView
from .salary_upload_view import SalaryAccountUploadView

urlpatterns = [
    # TruckType URLs
    path('truck-types/', TruckTypeListView.as_view(), name='truck-type-list'),
    path('truck-types/<int:pk>/', TruckTypeDetailView.as_view(), name='truck-type-detail'),
    
    # AccountType URLs
    path('account-types/', AccountTypeListView.as_view(), name='account-type-list'),
    path('account-types/<int:pk>/', AccountTypeDetailView.as_view(), name='account-type-detail'),
    
    # PlateNumber URLs
    path('plate-numbers/', PlateNumberListView.as_view(), name='plate-number-list'),
    path('plate-numbers/<int:pk>/', PlateNumberDetailView.as_view(), name='plate-number-detail'),
    
    # Repair and Maintenance Account URLs
    path('repair-maintenance/', RepairAndMaintenanceAccountListView.as_view(), name='repair-maintenance-list'),
    path('repair-maintenance/<int:pk>/', RepairAndMaintenanceAccountDetailView.as_view(), name='repair-maintenance-detail'),
    path('repair-maintenance/upload/', RepairAndMaintenanceUploadView.as_view(), name='repair-maintenance-upload'),
    
    # Insurance Account URLs
    path('insurance/', InsuranceAccountListView.as_view(), name='insurance-list'),
    path('insurance/<int:pk>/', InsuranceAccountDetailView.as_view(), name='insurance-detail'),
    path('insurance/upload/', InsuranceAccountUploadView.as_view(), name='insurance-upload'),
    
    # Fuel Account URLs
    path('fuel/', FuelAccountListView.as_view(), name='fuel-list'),
    path('fuel/<int:pk>/', FuelAccountDetailView.as_view(), name='fuel-detail'),
    path('fuel/upload/', FuelAccountUploadView.as_view(), name='fuel-upload'),
    
    # Tax Account URLs
    path('tax/', TaxAccountListView.as_view(), name='tax-list'),
    path('tax/<int:pk>/', TaxAccountDetailView.as_view(), name='tax-detail'),
    path('tax/upload/', TaxAccountUploadView.as_view(), name='tax-upload'),
    
    # Allowance Account URLs
    path('allowance/', AllowanceAccountListView.as_view(), name='allowance-list'),
    path('allowance/<int:pk>/', AllowanceAccountDetailView.as_view(), name='allowance-detail'),
    path('allowance/upload/', AllowanceAccountUploadView.as_view(), name='allowance-upload'),
    
    # Income Account URLs
    path('income/', IncomeAccountListView.as_view(), name='income-list'),
    path('income/<int:pk>/', IncomeAccountDetailView.as_view(), name='income-detail'),
    path('income/upload/', IncomeAccountUploadView.as_view(), name='income-upload'),
    
    # Trucking Account URLs
    path('trucking/', TruckingAccountListView.as_view(), name='trucking-list'),
    path('trucking/<int:pk>/', TruckingAccountDetailView.as_view(), name='trucking-detail'),
    path('trucking/upload/', TruckingAccountUploadView.as_view(), name='trucking-upload'),
    
    # Salary Account URLs
    path('salary/', SalaryAccountListView.as_view(), name='salary-list'),
    path('salary/<int:pk>/', SalaryAccountDetailView.as_view(), name='salary-detail'),
    path('salary/upload/', SalaryAccountUploadView.as_view(), name='salary-upload'),
    
    # Drivers Summary URL
    path('drivers/summary/', DriversSummaryView.as_view(), name='drivers-summary'),
    
    # Revenue Streams URL
    path('revenue/streams/', RevenueStreamsView.as_view(), name='revenue-streams'),
    
    # Accounts Summary URL
    path('accounts/summary/', AccountsSummaryView.as_view(), name='accounts-summary'),
    
    # Accounts Detail URL
    path('accounts/detail/', AccountsDetailView.as_view(), name='accounts-detail'),
    
    # Trips URL
    path('trips/', TripsView.as_view(), name='trips'),
    
    # Trucking Summary URLs (from trucking data)
    path('trucking/drivers/summary/', TruckingDriversSummaryView.as_view(), name='trucking-drivers-summary'),
    path('trucking/revenue/streams/', TruckingRevenueStreamsView.as_view(), name='trucking-revenue-streams'),
    path('trucking/accounts/summary/', TruckingAccountsSummaryView.as_view(), name='trucking-accounts-summary'),
    path('trucking/trips/summary/', TruckingTripsSummaryView.as_view(), name='trucking-trips-summary'),
]