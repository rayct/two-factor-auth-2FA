import time
import pyotp
import qrcode

key = "RaymondTurnerMyOtp"

uri = pyotp.totp.TOTP(key).provisioning_uri(name="RayTurners_2FA_App",
                                           issuer_name="2FA App")

print(uri)

qrcode.make(uri).save("./assets/totp.png")






# TEST CODE
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