#Strings: It is immutable


chai_type = "Ginger chai"
customer_name = "Aditya"

print(f"Order of {customer_name} : {chai_type} please!")

chai_description = "Aromatic and Bold"
print(f"First word: {chai_description[:8]}")
print(f"Last word: {chai_description[12:]}")
print(f"Reverse string: {chai_description[::-1]}")

label_text = "Chai Spécial"
encoded_label = label_text.encode("utf-8")
print(f"Non-Encoded Label: {label_text}")
print(f"Encoded Label: {encoded_label}")

decoded_label = encoded_label.decode("utf-8")
print(f"Decoded Label: {decoded_label}")