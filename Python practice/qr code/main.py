import qrcode

with open("L:\\Programming\\Python\\Main Problem Solving\\Python practice\\qr code\\websites_list.csv", "r") as file:
    for line in file:
        data = line.strip().split(",")
        # print(data[0], data[1])
        qrcode.make(data[1]).save(f"L:\\Programming\\Python\\Main Problem Solving\\Python practice\\qr code\\qrimg\\{data[0]}.png", scale=10)