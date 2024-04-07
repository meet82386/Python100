import random

india = ["Himachal Pradesh", "Uttaranchal", "Punjab", "Hariyana", "Uttar Pradesh", "Bihar", "Jharkhand", "West Bengal", "Odisha", "Sikkim", "Arunachal Pradesh", "Assam", "Tripura", "Meghalaya", "Mizoram", "Manipur", "Nagaland", "Madhya Pradesh", "Rajasthan", "Gujarat", "Maharastra", "Chattisgadh", "Goa", "Karnataka", "Telangana", "Andhara Pradesh", "Tamil Nadu", "Kerala"]

india.extend(["Jammu and Kashmir", "Laddakh", "Chandigadh", "Delhi", "Daman, Diu and Dadra-nagar-haveli", "Pondicheri", "Andaman and Nikobar islands", "Lakshdweep"])

selected = random.randint(0, len(india)-1)

print(f"Selectd State/UT is: {india[selected]}")
random.shuffle(india)
print(india)
