from .services.register import UserService
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            try:
                validated_data = serializer.validated_data
                user = UserService.register_user(
                    username=validated_data.get('username'),
                    email=validated_data.get('email'),
                    password=validated_data.get('password'),
                    birth_date=validated_data.get('birth_date')
                )     
            except Exception as e:
              return Response({"error": str(e)}, status=400)
        
        return Response({"message": "User registered successfully", "user_id": user.id})
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get (self, request):
        user = request.user
        return Response({
            "username": user.username,
            "email": user.email,
            "bio": user.bio,
            "profile_image": user.profile_image.url if user.profile_image else None,
            "location": user.location,
            "birth_date": user.birth_date
        })
        
class PasswordResetRequestView(APIView):
    def post(self, request):
        email = request.data.get("email")      
        UserService.request_password_reset(email)
        return Response({"message":"if email exists, you will be recieving an email with the password reset token"})
    
class PasswordResetConfirmView(APIView):
    def post(self, request):
        uidb64 = request.data.get('uid')
        token = request.data.get('token')
        new_password = request.data.get('new_password')
        
        success = UserService.complete_password_reset(uidb64, token, new_password)
        
        if success:
            return Response({"message": "Password aggiornata con successo."})
        return Response({"error": "Token non valido o scaduto."}, status=400)