import django_filters.rest_framework
from django.shortcuts import render
from .serializers import DriverSerializer, ClientSerializer, OrderSerializer
from .models import Driver, Client, Order
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.views import APIView


# DRIVER
class DriverList(APIView):
    def get(self, request):
        queryset = Driver.objects.all()
        serializer = DriverSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DriverSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# CLIENT
class ClientList(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ORDER
class OrderList(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            print(serializer.data)
            return Response(serializer.data['id'], status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ORDER UPDATE
class OrderUpdate(APIView):
    def put(self, request, order_id):
        order = Order.objects.get(id=order_id)
        pre_status = order.order_status
        serializer = OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            if serializer.validated_data['order_status'] == 2 and pre_status:
                return Response("Order can't be cancelled")
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# LIST CLIENT'S ORDERS
class ClientOrderList(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get_queryset(self):
        queryset = self.queryset
        from_ = self.request.query_params.get('from')
        to_ = self.request.query_params.get('to')
        if from_ and to_:
            return queryset.filter(client_id=self.kwargs['client_id'], order_start_time__range=[from_, to_])
        return queryset.filter(client_id=self.kwargs['client_id'])









