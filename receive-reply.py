from multiprocessing import Process
from time import sleep
from ringcentral.subscription import Events
from ringcentral import SDK
from dotenv import Dotenv
import os
dotenv = Dotenv(os.path.join(os.path.dirname(__file__), ".env"))
os.environ.update(dotenv)

rcsdk = SDK( os.getenv("RINGCENTRAL_CLIENT_ID"),
           os.getenv("RINGCENTRAL_CLIENT_SECRET"),
           os.getenv("RINGCENTRAL_SERVER_URL") )

platform = rcsdk.platform()
platform.login( os.getenv("RINGCENTRAL_USERNAME"),
                os.getenv("RINGCENTRAL_EXTENSION"),
                os.getenv("RINGCENTRAL_PASSWORD") )

def pubnub():
    try:
        eventFilters = [
            '/account/~/extension/~/message-store/instant?type=SMS',
            '/account/~/extension/~/voicemail'
        ]
        subscription = rcsdk.create_subscription()
        subscription.add_events(eventFilters)
        subscription.on(Events.notification, on_message)
        res = subscription.register()
        print("Wait for notifications ...")
        while True:
            sleep(1)

    except KeyboardInterrupt:
        print("Failed to subscribe for notifications.")

def on_message(msg):
    if "/message-store/instant" in msg['event']:
        senderNumber = msg['body']['from']['phoneNumber']
        print ("Received a voicemail from: " + senderNumber)
        response = platform.post('/account/~/extension/~/sms', {
            'from': {'phoneNumber': os.getenv("RINGCENTRAL_USERNAME")},
            'to': [{'phoneNumber': senderNumber}],
            'text' : 'This is an automatic reply. Thank you for your message!'
        })
        print('Replied message sent. Message delivery status: ' + response.json().messageStatus)
    elif "/voicemail" in msg['event']:
        if "phoneNumber" in msg['body']['from']:
            senderNumber = msg['body']['from']['phoneNumber']
            print ("Received a voicemail from: " + senderNumber)
            response = platform.post('/account/~/extension/~/sms', {
                'from': {'phoneNumber': os.getenv("RINGCENTRAL_USERNAME")},
                'to': [{'phoneNumber': senderNumber}],
                'text' : 'This is an automatic reply. Thank you for your voice message! I will get back to you asap.'
            })
            print("Replied message sent. Message delivery status: " + response.json().messageStatus)
    else:
        print ("Not an event we are waiting for.")

p = Process(target=pubnub)

try:
    p.start()
except KeyboardInterrupt:
    p.terminate()
