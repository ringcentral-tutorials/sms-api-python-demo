# SMS Application Walk-through

Welcome to the SMS Application Walk-through and tour of a fully functional SMS application powered by RingCentral. In this walk through you will learn:

- How to send an SMS message
- How to send an MMS message
- How to track delivery status of messages
- How to modify the message's read status.
- How to delete a message.
- How to receive and reply to SMS messages

### Clone - Setup - Run the project
```
$ git clone https://github.com/ringcentral-tutorials/sms-api-python-demo
$ cd sms-api-python-demo
$ cp .env-sampledotenv .env
$ python setup.py install
```
Specify your app client id and client secret as well as account login credentials to the .env file.

#### How to send SMS
```
$ python send-sms.py
```
#### How to send MMS
```
$ python send-mms.py
```
#### How to retrieve and modify message status
```
$ python retrieve-modify.py
```
#### How to delete a message
```
$ python retrieve-delete.py
```
#### How to receive and reply to SMS messages
```
$ python receive-reply.py
```

## RingCentral Python SDK
The SDK is available at https://github.com/ringcentral/ringcentral-python
