from ringcentral import SDK
import os, time
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

builder = rcsdk.create_multipart_builder()
body = {
             'from': {'phoneNumber': os.getenv("RINGCENTRAL_USERNAME")},
             'to': [{'phoneNumber': os.getenv("RECIPIENT_PHONE_NUMBER")}],
             'text': 'This is a test message from Python'
         }
builder.set_body(body)
image = open ('test.jpg', 'rb')
attachment = ('test.jpg', image, 'image/jpeg')
builder.add(attachment)
request = builder.request('/account/~/extension/~/sms')
try:
    response = platform.send_request(request)
    print("Message sent. Delivery status: " + response.json().messageStatus)
    # while response.json().messageStatus == 'Queued':
    #     time.sleep(1)
    #     response = platform.get("/account/~/extension/~/message-store/" + str(response.json().id));
    #     print('Message delivery status: ' + response.json().messageStatus)
except Exception as e:
    print(e)
