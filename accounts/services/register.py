from datetime import date, datetime
from django.contrib.auth import get_user_model
from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from .exceptions import * # Le tue eccezioni personalizzate
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
User = get_user_model()

class UserService:
    @classmethod
    def register_user(cls, username, email, password, birth_date=None):

        cls._validate_user_data(username, email, password, birth_date)
        
        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            birth_date=birth_date
        )
        return user 

    @staticmethod
    def _validate_user_data(username, email, password, birth_date):
        if not username or not email or not password:
            raise MissingRequiredFieldError()
        
        if User.objects.filter(email=email).exists():
            raise EmailAlreadyExistsError()
        
        
        if User.objects.filter(username=username).exists():
            raise UsernameAlreadyExistsError()
        
        try:
            validate_email(email)
        except ValidationError:
            raise InvalidEmailError()
        
        if birth_date:
        
            if isinstance(birth_date, str):
                try:
                    birth_date = datetime.strptime(birth_date, '%Y-%m-%d').date()
                except ValueError:
                    raise InvalidBirthDateError("Formato data non valido. Usa YYYY-MM-DD")

            today = date.today()
            age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
            if age < 13:
                raise AgeRestrictionError("Devi avere almeno 13 anni.")
            
    @staticmethod
    def request_password_reset(email):
        if not email:
            raise MissingRequiredFieldError()
        try:
            validate_email(email)
        except ValidationError:
            raise InvalidEmailError()
        
        user = User.objects.filter(email=email).first()
        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            reset_link = f"http://frontend.com/reset-password/{uid}/{token}/"
            print(f"EMAIL INVIATA A {email}: {reset_link}")
            return True
        else:
             return False                 
    
    
    @staticmethod
    def reset_password(uidb64, token, new_password):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        
            if user and default_token_generator.check_token(user, token):
                user.set_password(new_password)
                user.save()
                return True
        except (TypeError, ValueError, OverflowError, User.DoesNotExist):
            pass
        return False
