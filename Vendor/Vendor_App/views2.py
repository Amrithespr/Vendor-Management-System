

# # Create your views here.

# from django.shortcuts import render
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import *
# from .models import *
# from .serializers import *
# from rest_framework.response import Response
# from django.utils import timezone
# from django.db.models import Avg
# from rest_framework.authentication import TokenAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework import generics, status

# class VendorListCreateView(generics.ListCreateAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

# class VendorRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

# class PurchaseOrderListCreateView(generics.ListCreateAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer

# class PurchaseOrderRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer

# class VendorPerformanceView(generics.RetrieveAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     queryset = Vendor.objects.all()
#     serializer_class = VendorSerializer

#     def retrieve(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response({'on_time_delivery_rate': serializer.data['on_time_delivery_rate'],
#                  'quality_rating_avg': serializer.data['quality_rating_avg'],
#                  'average_response_time': serializer.data['average_response_time'],
#                  'fulfillment_rate': serializer.data['fulfillment_rate']})
#         # return Response(serializer.data['on_time_delivery_rate', 'quality_rating_avg', 'average_response_time', 'fulfillment_rate'])

# # class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
# #     # authentication_classes = [TokenAuthentication]
# #     # permission_classes = [IsAuthenticated]
# #     queryset = PurchaseOrder.objects.all()
# #     serializer_class = PurchaseOrderSerializer

# #     def create(self, request, *args, **kwargs):
# #         instance = self.get_object()
# #         instance.acknowledgment_date = request.data.get('acknowledgment_date')    #timezone.now()
# #         instance.save()
# #         response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
# #         average_response_time = sum(abs((ack_date - issue_date).total_seconds()) for ack_date, issue_date in response_times) #/ len(response_times)
# #         if response_times:
# #             average_response_time = total_seconds / len(response_times)
# #         else:
# #             average_response_time = 0  # Avoid division by zero if there are no response times
# #         instance.vendor.average_response_time = average_response_time
# #         instance.vendor.save()
# #         return Response({'acknowledgment_date': instance.acknowledgment_date})


# class AcknowledgePurchaseOrderView(generics.UpdateAPIView):
#     # authentication_classes = [TokenAuthentication]
#     # permission_classes = [IsAuthenticated]
#     queryset = PurchaseOrder.objects.all()
#     serializer_class = PurchaseOrderSerializer

#     @receiver(post_save, sender=PurchaseOrder)
#     def update_vendor_performance(sender, instance, **kwargs):
#         if instance.status == 'completed' and instance.delivered_data is None:
#             instance.delivered_data = timezone.now()
#             instance.save()

#     # Update On-Time Delivery Rate
#         completed_orders = PurchaseOrder.objects.filter(vendor=instance.vendor, status='completed')
#         completed_orders_count = completed_orders.count()

#         if completed_orders_count > 0:
#             on_time_deliveries = completed_orders.filter(delivery_date__gte=F('delivered_data'))
#             on_time_delivery_rate = on_time_deliveries.count() / completed_orders_count
#         else:
#             on_time_delivery_rate = 0

#         instance.vendor.on_time_delivery_rate = on_time_delivery_rate

#         # Update Quality Rating Average
#         completed_orders_with_rating = completed_orders.exclude(quality_rating__isnull=True)
#         completed_orders_with_rating_count = completed_orders_with_rating.count()

#         if completed_orders_with_rating_count > 0:
#             quality_rating_avg = completed_orders_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
#         else:
#             quality_rating_avg = 0

#         instance.vendor.quality_rating_avg = quality_rating_avg

#         # Update Average Response Time
#         response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
#         response_times_count = len(response_times)

#         if response_times_count > 0:
#             total_seconds = sum(abs((ack_date - issue_date).total_seconds()) for ack_date, issue_date in response_times)
#             average_response_time = total_seconds / response_times_count
#         else:
#             average_response_time = 0

#         instance.vendor.average_response_time = average_response_time

#         # Save the updated vendor performance metrics
#         instance.vendor.save()


    

# # new from chatgpt

#     #     # Update On-Time Delivery Rate
#     # completed_orders_count = completed_orders.count()
#     # if completed_orders_count > 0:
#     #     on_time_delivery_rate = on_time_deliveries.count() / completed_orders_count
#     # else:
#     #     on_time_delivery_rate = 0
#     # instance.vendor.on_time_delivery_rate = on_time_delivery_rate

#     # # Update Quality Rating Average
#     # completed_orders_with_rating_count = completed_orders_with_rating.count()
#     # if completed_orders_with_rating_count > 0:
#     #     quality_rating_avg = completed_orders_with_rating.aggregate(Avg('quality_rating'))['quality_rating__avg'] or 0
#     # else:
#     #     quality_rating_avg = 0
#     # instance.vendor.quality_rating_avg = quality_rating_avg

#     # # Update Average Response Time
#     # response_times = PurchaseOrder.objects.filter(vendor=instance.vendor, acknowledgment_date__isnull=False).values_list('acknowledgment_date', 'issue_date')
#     # response_times_count = len(response_times)
#     # if response_times_count > 0:
#     #     total_seconds = sum(abs((ack_date - issue_date).total_seconds()) for ack_date, issue_date in response_times)
#     #     average_response_time = total_seconds / response_times_count
#     # else:
#     #     average_response_time = 0
#     # instance.vendor.average_response_time = average_response_time

