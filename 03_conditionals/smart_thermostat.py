device_status = input("Enter the Device Status:").lower()
temperature = int(input("Enter the temperature:"))

if device_status == "active":
    if(temperature > 35):
        print(f"High temperature alert!")
    else:
        print(f"Temperature is normal.")
else:
    print(f"Device is offline")