import secrets

TokenLength = int(input('Enter the number of bits of the token (Recomender 32 or 64): '))

SecretToken = secrets.token_bytes(TokenLength)
HexSecretToken = secrets.token_hex(TokenLength)
UrlSecretToken = secrets.token_urlsafe(TokenLength)
print("Token in bytes: ")
print(SecretToken)
print("====================")
print(" ")
print("Token in hex: ")
print(HexSecretToken)
print("====================")
print(" ")
print("Token in URL secret: ")
print(UrlSecretToken)
