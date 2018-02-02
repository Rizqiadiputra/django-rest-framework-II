"""
Request objects
REST framework introduces a Request object that extends the regular HttpRequest, and provides more flexible request parsing. The core functionality of the Request object is the request.data attribute, which is similar to request.POST, but more useful for working with Web APIs.

request.POST  # Only handles form data.  Only works for 'POST' method.
request.data  # Handles arbitrary data.  Works for 'POST', 'PUT' and 'PATCH' methods.

-
Response objects
REST framework also introduces a Response object, which is a type of TemplateResponse that takes unrendered content and uses content negotiation to determine the correct content type to return to the client.

return Response(data)  # Renders to content type as requested by the client.

-
Status codes
Using numeric HTTP status codes in your views doesn't always make for obvious reading, and it's easy to not notice if you get an error code wrong. REST framework provides more explicit identifiers for each status code, such as HTTP_400_BAD_REQUEST in the status module. It's a good idea to use these throughout rather than using numeric identifiers.

-

Wrapping API views
REST framework provides two wrappers you can use to write API views.

The @api_view decorator for working with function based views.
The APIView class for working with class-based views.
These wrappers provide a few bits of functionality such as making sure you receive Request instances in your view, and adding context to Response objects so that content negotiation can be performed.

The wrappers also provide behaviour such as returning 405 Method Not Allowed responses when appropriate, and handling any ParseError exception that occurs when accessing request.data with malformed input.

"""

"""
Cara kedua
"""
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer


"""
wrapping API views
The @api_view decorator for working with function based views.
"""

@api_view(['GET', 'POST'])
def student_list(request, format=None):
    """
       List all code students, or create a new student.
       """
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_detail(request, pk, format=None):
    """
        Retrieve, update or delete a code student.
        """
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""Cara satu"""
# from django.shortcuts import render
# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from .models import Student
# from .serializers import StudentSerializer

# Create your views here.

# @csrf_exempt
# def student_list(request):
#     """
#     List all code students, or create a new student.
#     """
#     if request.method == 'GET':
#         students = Student.objects.all()
#         serializer = StudentSerializer(students, many=True)
#         return JsonResponse(serializer.data, safe=False)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def student_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         student = Student.objects.get(pk=pk)
#     except Student.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = StudentSerializer(student)
#         return JsonResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = StudentSerializer(student, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         student.delete()
#         return HttpResponse(status=204)