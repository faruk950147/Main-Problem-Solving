import re
phone_regex = r"^(\+?\d{0,4})?\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{3}\)?)\s?-?\s?(\(?\d{4}\)?)?$"

# def phone_number(phone):
#     if phone.startswith("+88"):
#         print("Bangladesh phone number")
#     elif phone.startswith("+91"):
#         print("India phone number")
#     elif phone.startswith("+92"):
#         print("Pakistan phone number")
#     elif phone.startswith("+93"):
#         print("Afghanistan phone number")
#     elif phone.startswith("+94"):
#         print("Sri Lanka phone number")
#     elif phone.startswith("+95"):
#         print("Myanmar phone number")
#     elif phone.startswith("+96"):
#         print("Yemen phone number")
#     elif phone.startswith("+97"):
#         print("Saudi Arabia phone number")
#     elif phone.startswith("+98"):
#         print("Iran phone number")
#     elif phone.startswith("+99"):
#         print("Kuwait phone number")
#     else:
#         print("Invalid phone number")

# phone_number("+8801722222222")


def phone_number(phone):
    if re.fullmatch(phone_regex, phone):
        return True
    return False

print(phone_number("+8801722222222"))
print(phone_number("+88017222222222"))
print(phone_number("+880172222222222"))
print(phone_number("+8801722222222222"))

