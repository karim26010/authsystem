from rest_framework.exceptions import APIException
from rest_framework import status

class EmailAlreadyExistsError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "A user with this email already exists, if its yours try to login."
    
class UsernameAlreadyExistsError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "A user with this username already exists, please choose another one."
    
class WeakPasswordError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The provided password is too weak, please choose a stronger password."
    
class InvalidEmailError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "The provided email address is not valid."
    
class MissingRequiredFieldError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "One or more required fields are missing."
    
class AgeRestrictionError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = "Users must be at least 13 years old to register."
    
class InvalidBirthDateError(APIException):
    status_code = status.HTTP_400_BAD_REQUEST