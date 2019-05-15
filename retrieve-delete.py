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
    'readStatus' : "Read"
}
response = platform.get('/account/~/extension/~/message-store', params)
records = response.json().records
count = len(records)
print ("We get a list of %d messages" % (count))
for record in records:
    messageId = record.id
    platform.delete("/account/~/extension/~/message-store/%d" % (messageId))
    print("Message %d has been deleted" % (messageId))
    break
