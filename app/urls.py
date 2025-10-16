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
    DriversSummaryView,
)
from .revenue_views import RevenueStreamsView

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
    
    # Drivers Summary URL
    path('drivers/summary/', DriversSummaryView.as_view(), name='drivers-summary'),
    
    # Revenue Streams URL
    path('revenue/streams/', RevenueStreamsView.as_view(), name='revenue-streams'),
]