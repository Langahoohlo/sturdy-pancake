from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
class SignUpView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        data = self.request.data
        
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        password2 = data.get('password2')

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'email already exists'})
            else:
                if len(password) < 6:
                    return Response({'error': 'password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(email=email, name=name, password=password)

                    user.save()
                    return Response({'message': 'user created successfully'})

        else:
            return Response(status=400)
        

        

