from ringcentral import SDK
import os
from dotenv import Dotenv
dotenv = Dotenv(".env")
os.environ.update(dotenv)

def get_sdk():
    if os.getenv("ENVIRONMENT_MODE") == "sandbox":
        sdk = SDK(os.getenv("CLIENT_ID_SB"), os.getenv("CLIENT_SECRET_SB"), 'https://platform.devtest.ringcentral.com')
    else:
        sdk = SDK(os.getenv("CLIENT_ID_PROD"), os.getenv("CLIENT_SECRET_PROD"), 'https://platform.ringcentral.com')
    return sdk

def get_platform():
    sdk = get_sdk()
    platform = sdk.platform()
    if os.getenv("ENVIRONMENT_MODE") == "sandbox":
        platform.login(os.getenv("USERNAME_SB"), '', os.getenv("PASSWORD_SB"))
    else:
        platform.login(os.getenv("USERNAME_PROD"), '', os.getenv("PASSWORD_PROD"))
    return platform

def get_phonenumber():
    if os.getenv("ENVIRONMENT_MODE") == "sandbox":
        return os.getenv("USERNAME_SB")
    else:
        return os.getenv("USERNAME_PROD")
