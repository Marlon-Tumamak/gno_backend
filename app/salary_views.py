from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import SalaryAccount
from .serializers import SalaryAccountSerializer


# SalaryAccount Views
class SalaryAccountListView(ListCreateAPIView):
    """
    GET: List all salary accounts
    POST: Create a new salary account
    """
    queryset = SalaryAccount.objects.all()
    serializer_class = SalaryAccountSerializer


class SalaryAccountDetailView(RetrieveUpdateDestroyAPIView):
    """
    GET: Retrieve a specific salary account
    PUT: Update a specific salary account
    PATCH: Partially update a specific salary account
    DELETE: Delete a specific salary account
    """
    queryset = SalaryAccount.objects.all()
    serializer_class = SalaryAccountSerializer

