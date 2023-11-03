from time import sleep
from django.http import JsonResponse
from .models import Intern
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework import status
from .task import send_mail
from django.forms.models import model_to_dict

class InternAPI(APIView):
    def get(self, request):
        intern = Intern.objects.all().values()
        return Response(intern, status=status.HTTP_200_OK)


class AddNewIntern(APIView):
    def post(self, request):
        data = request.data
        print(data)
        Intern.objects.create(
            emp_id=data.get('emp_id'),
            name=data.get('name'),
            age=data.get('age'),
            passing_year=data.get('passing_year'),
            address=data.get('address'),
            phone_number=data.get('phone_number'),
            finishing_date=data.get('finishing_date')
        )
        return Response(request.data)


class DeleteIntern(APIView):
    def post(self, request, id):
        Intern.objects.get(emp_id=id).delete()
        return Response({'status': 'OK'})


class UpdateInternDetails(APIView):
    def post(self, request, id):
        intern = Intern.objects.get(emp_id=id)
        intern.name = request.data.get("name")
        intern.save()
        return Response({'status': 'OK'})


class GetInternFromId(APIView):
    def get(self, request, id):
        data = Intern.objects.get(emp_id=id)
        return Response(model_to_dict(data))
        # return Response({
        #     "emp_id": data.emp_id,
        #     "name": data.name,
        #     "age": data.age,
        #     "passing_year": data.passing_year,
        #     "address": data.address,
        #     "phone_number": data.phone_number,
        #     "finishing_date": data.finishing_date
        # })


class SendMail(APIView):
    def get(self, request):
        send_mail.delay()
        return Response({"status": 'ok'})

# @api_view(['GET', 'POST'])
# def intern_list(request):

#     if request.method == 'GET':
#         intern = Intern.objects.all().values()
#         # serializer = InternSerializer(intern, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         # return JsonResponse({'interns': serializer.data})
#         return Response(intern)
#     elif request.method == 'POST':
#         data = request.data
#         print(data)
#         # serializer = InternSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     serializer.save()
#         #     return Response(serializer.data, status=status.HTTP_201_CREATED)
#         Intern.objects.create(
#             emp_id=data.get('emp_id'),
#             name=data.get('name'),
#             clg_name=data.get('clg_name'),
#             age=data.get('age'),
#             passing_year=data.get('passing_year'),
#             address=data.get('address'),
#             phone_number=data.get('phone_number'),
#             finishing_date=data.get('finishing_date')
#         )
#         return Response(request.data)


# @api_view(['GET', 'PUT', 'DELETE'])
# def intern_details(request, emp_id):
#     try:
#         intern = Intern.objects.get(emp_id=emp_id)
#         if request.method == 'GET':
#             serializer = InternSerializer(intern)
#             return Response(serializer.data)
#         elif request.method == 'PUT':
#             serializer = InternSerializer(intern, data=request.data)
#             if serializer.is_valid():
#                 serializer.save()
#                 return Response(serializer.data, status=status.HTTP_201_CREATED)
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         elif request.method == 'DELETE':
#             intern.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#     except Intern.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
