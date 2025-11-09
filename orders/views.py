# # from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets, status
# from rest_framework.decorators import action
# from rest_framework.response import Response
# from .models import Order
# from .serializers import OrderSerializer
# from users.permissions import IsAdminUserRole
# import csv
# from django.http import HttpResponse

# class AdminOrderViewSet(viewsets.ModelViewSet):
#     queryset = Order.objects.all().order_by('-created_at')
#     serializer_class = OrderSerializer
#     permission_classes = [IsAdminUserRole]
#     filterset_fields = ['status','created_at','user__email']
#     search_fields = ['id','user__email']

#     @action(detail=False, methods=['post'])
#     def export(self, request):
#         ids = request.data.get('ids', [])
#         qs = self.queryset.filter(id__in=ids) if ids else self.queryset
#         response = HttpResponse(content_type='text/csv')
#         response['Content-Disposition'] = 'attachment; filename="orders.csv"'
#         writer = csv.writer(response)
#         writer.writerow(['order_id','user_email','total','status','created_at'])
#         for o in qs:
#             writer.writerow([o.id, o.user.email if o.user else '', o.total, o.status, o.created_at])
#         return response


#     @action(detail=True, methods=['put'])
#     def status(self, request, pk=None):
#         order = self.get_object()
#         new_status = request.data.get('status')
#         if new_status not in dict(Order.STATUS_CHOICES):
#             return Response({'error':'invalid status'}, status=400)
#         order.status = new_status
#         order.save()
#         return Response({'success':True, 'order': OrderSerializer(order).data})


from rest_framework import viewsets
from .models import Order
from .serializers import OrderSerializer
from django.http import JsonResponse

def order_list(request):
    return JsonResponse({
        "orders": [
            {"id": 1, "product": "Product A", "quantity": 2},
            {"id": 2, "product": "Product B", "quantity": 1}
        ]
    })

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
