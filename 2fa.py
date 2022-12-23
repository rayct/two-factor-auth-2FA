import time
import pyotp
import qrcode

key = "RaymondTurnerMyOtp"

# Verify Code Function
totp = pyotp.TOTP(key)

while True:
    print(totp.verify(input("Enter Code:")))






# TEST CODE
# ********************
# Create the QrCode
# uri = pyotp.totp.TOTP(key).provisioning_uri(name="YourName2FA_App",
#                                            issuer_name="2FA App")
# print(uri)
# qrcode.make(uri).save("./assets/totp.png")
# ********************

# ********************
# totp = pyotp.TOTP(key)
# print(totp.now())
# input_code = input("Enter 2FA Code:")
# ********************

# ********************
# Input Code Time Tester
# totp.verify(input_code)
# print(totp.verify(input_code))
# ********************

# ********************
# Time Code Reset Test 
# time.sleep(30)
# print(totp.now())
# ********************