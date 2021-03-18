import base64

input_string = input("-nhập chuỗi cần mã hóa: ")
string = input_string.encode("ascii")

bytes = base64.b64encode(string)
output_bytes = bytes.decode("ascii")

print(f"Encoded string: {output_bytes}")

bytes_string = input("-nhập chuỗi cần giải mã: ")
bytes = bytes_string.encode("ascii")

output_string = base64.b64decode(bytes)
output_string = output_string.decode("ascii")

print(f"Decoded string: {output_string}")