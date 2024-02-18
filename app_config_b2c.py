import os

b2c_tenant = os.getenv('TENANT_NAME')
signupsignin_user_flow = os.getenv('SIGNUPSIGNIN_USER_FLOW')
editprofile_user_flow = os.getenv('EDITPROFILE_USER_FLOW')

resetpassword_user_flow = os.getenv('RESETPASSWORD_USER_FLOW')

authority_template = "https://{tenant}.b2clogin.com/{tenant}.onmicrosoft.com/{user_flow}"

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

AUTHORITY = authority_template.format(tenant=b2c_tenant, user_flow=signupsignin_user_flow)
B2C_PROFILE_AUTHORITY = authority_template.format(tenant=b2c_tenant, user_flow=editprofile_user_flow)

B2C_RESET_PASSWORD_AUTHORITY = authority_template.format(tenant=b2c_tenant, user_flow=resetpassword_user_flow)

REDIRECT_PATH = "/getAToken"  

ENDPOINT = ''

SCOPE = []

SESSION_TYPE = "filesystem"  