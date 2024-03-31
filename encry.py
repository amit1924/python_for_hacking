import base64


def encrypt_pass(password):
    encoded_bytes = base64.b64encode(password.encode())
    print(encoded_bytes)


user_pass = input("Enter your password: ")
encrypt_pass(user_pass)


def decode_pass(password):
    decoded_bytes = base64.b64decode(password)
    decode_data = decoded_bytes.decode("latin-1")
    print(f"decoded password: {decode_data}")


decode_user_pass = input("Enter the base64 string: ")
decode_pass(decode_user_pass)
