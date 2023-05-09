# import package
import africastalking
from django.conf import settings

username = settings.AFRICATALKING_USERNAME
api_key = settings.AFRICATALKING_API_KEY


def send_sms(smss: str, phone_numbers: list):
    africastalking.initialize(username, api_key)
    sms = africastalking.SMS
    sms.send(smss, phone_numbers)
