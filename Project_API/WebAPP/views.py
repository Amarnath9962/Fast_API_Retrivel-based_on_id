# Import necessary modules
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.
class EmployeeList(APIView):

    def get(self, request):
        id = request.query_params.get('id')

        # If ID is provided, retrieve a single employee object
        if id is not None:
            try:
                employee = Employee.objects.get(id=id)
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data)
            except Employee.DoesNotExist:
                return Response({"error": "Employee not found"}, status=404)

        # If ID is not provided, retrieve all employees
        employees = Employee.objects.all()
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data)

    def post(self, request):
        pass
