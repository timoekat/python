from smartphone import Smartphone

catalog = [
    Smartphone("Apple iPhone", "15 Pro", "+79667373373"),
    Smartphone("Samsung Galaxy", "S24 Ultra", "+7977487483"),
    Smartphone("Xiaomi", "14 Pro", "+798378744"),
    Smartphone("Google Pixel", "8 Pro", "+79723672467"),
    Smartphone("OnePlus", "12", "+7934784844")
]

for smartphone in catalog:
    print(f"{smartphone.brand}, {smartphone.model}, {smartphone.number}")