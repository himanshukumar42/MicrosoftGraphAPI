import os
from dotenv import load_dotenv

load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

AUTHORITY = f"https://login.microsoftonline.com/{os.getenv('TENANT_ID', 'common')}"

REDIRECT_PATH = "/auth-callback" 
ENDPOINT = 'https://graph.microsoft.com/v1.0'  

SCOPE = [
    "User.ReadBasic.All",
    "Chat.Read",
    "Chat.ReadWrite",
    ]

SESSION_TYPE = "filesystem"
