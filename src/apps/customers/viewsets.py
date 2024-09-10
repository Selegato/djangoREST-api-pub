from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializers import CustomerSerializer, BenefitSerializer
from .models import CustomerModel, BenefitModel
from mongodb_connection import get_unidata_qa
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class CustomerViewSet(viewsets.ViewSet):

    #get_All
    def list(self, request):
        db = get_unidata_qa()
        customer_model = CustomerModel(db)
        customers = customer_model.get_all_customers()
        if not customers:
            return Response({'message': 'No customers found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #get_One
    def retrieve(self, request, pk=None):
        db = get_unidata_qa()
        customer_model = CustomerModel(db)
        customer = customer_model.find_customer(pk)
        if not customer:
            return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    #add_one
    def create(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            db = get_unidata_qa()
            customer_model = CustomerModel(db)
            customer = customer_model.find_customer(validated_data['document'])
            if customer:
                return Response({'message': 'Customer already exists'}, status=status.HTTP_400_BAD_REQUEST)
            if 'birthDate' in validated_data:
              validated_data['birthDate'] = validated_data['birthDate'].strftime('%Y-%m-%d')
            validated_data['registerDate'] = datetime.now().isoformat()
            validated_data['updateDate'] = datetime.now().isoformat()
            customer_model.insert_customer(validated_data)
            return Response({'message': 'Success'},status=status.HTTP_201_CREATED)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    #update sem CPF
    def update(self, request, pk=None):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            validated_data = serializer.validated_data
            db = get_unidata_qa()
            customer_model = CustomerModel(db)
            customer = customer_model.find_customer(validated_data['document'])
            if not customer:
                return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
            if 'birthDate' in validated_data:
                validated_data['birthDate'] = validated_data['birthDate'].strftime('%Y-%m-%d')
            validated_data['updateDate'] = datetime.now().isoformat()
            if 'document' in validated_data:
                del validated_data['document']
            customer_model.update_customer(pk, validated_data)
            return Response({'message': 'Success'},status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #delete
    def destroy(self, request, pk=None):
        db = get_unidata_qa()
        customer_model = CustomerModel(db)
        customer = customer_model.find_customer(pk)
        if not customer:
            return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        customer_model.delete_customer(pk)
        return Response({'message': 'Success'},status=status.HTTP_200_OK)
    

class BenefitViewSet(viewsets.ModelViewSet):
    queryset = BenefitModel.objects.all()
    serializer_class = BenefitSerializer


class CustomerBenefitViewSet(viewsets.ViewSet):
    def list(self, request):
        cpf = request.query_params.get('cpf')
        if not cpf:
            return Response({'message': 'CPF is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        db = get_unidata_qa()
        customer_model = CustomerModel(db)
        customer = customer_model.find_customer(cpf)
        if not customer:
            return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        benefits = BenefitModel.objects.filter(nrCpf=cpf)
        if not benefits:
            return Response({'message': 'No benefits found'}, status=status.HTTP_404_NOT_FOUND)
        
        customer_serializer = CustomerSerializer(customer)
        benefit_serializer = BenefitSerializer(benefits, many=True)

        combined_data = {
            'customer': customer_serializer.data,
            'benefits': benefit_serializer.data
        }

        return Response(combined_data, status=status.HTTP_200_OK)


    def retrieve(self, request, pk=None):
        db = get_unidata_qa()

        #consulta MongoDB
        customer_model = CustomerModel(db)
        customer = customer_model.find_customer(pk)
        if not customer:
            return Response({'message': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)
        
        #Consulta SQL
        benefit = BenefitModel.objects.get(pk=pk)
        if not benefit:
            return Response({'message': 'No benefits found'}, status=status.HTTP_404_NOT_FOUND)
        
        customer_serializer = CustomerSerializer(customer)
        benefit_serializer = BenefitSerializer(benefit)

        combined_data = {
        'customer': customer_serializer.data,
        'benefit': benefit_serializer.data
        }

        return Response(combined_data, status=status.HTTP_200_OK)