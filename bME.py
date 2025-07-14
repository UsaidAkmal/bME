print(f'''
 __     _______ _______ 
|  |--.|   |   |    ___|
|  _  ||       |    ___|
|_____||__|_|__|_______|
Calculator BMI (Body Mass Index)
                       
''')

berat = float(input("Berapa berat badan kamu? (kg) "))
tinggi = float(input("Berapa tinggi badan kamu? (cm)"))

tinggi = tinggi / 100

bmi = berat / (tinggi ** 2)

print(f"\nBmi Kamu Adalah: {bmi: .2f}")

if bmi < 18.5:
    print("Kategori: Kurus")
elif bmi < 25:
    print("Kategori: Normal")
elif bmi < 30:
    print("Kategori: Gemuk")
else:
    print("Kategori: Obesitas")
