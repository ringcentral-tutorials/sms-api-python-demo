from ringcentral import SDK
import os
from dotenv import Dotenv
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env"))
os.environ.update(dotenv)

rcsdk = SDK( os.getenv("RINGCENTRAL_CLIENT_ID"),
           os.getenv("RINGCENTRAL_CLIENT_SECRET"),
           os.getenv("RINGCENTRAL_SERVER_URL") )

platform = rcsdk.platform()
platform.login( os.getenv("RINGCENTRAL_USERNAME"),
                os.getenv("RINGCENTRAL_EXTENSION"),
                os.getenv("RINGCENTRAL_PASSWORD") )

params = {
             'from': {'phoneNumber': os.getenv("RINGCENTRAL_USERNAME")},
             'to': [{'phoneNumber': os.getenv("RECIPIENT_PHONE_NUMBER")}],
             'text': 'This is a test message from Python'
         }
try:
    response = platform.post('/account/~/extension/~/sms', params)
    print("Message sent. Delivery status: " + str(response.json().messageStatus))
except Exception as e:
    print(e)
