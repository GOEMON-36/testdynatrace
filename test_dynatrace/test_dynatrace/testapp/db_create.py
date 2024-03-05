from testapp.models import Car  # your_appはあなたのアプリケーション名に置き換えてください

# Carインスタンスを作成してデータベースに保存
cars = [
    {"car": "Toyota Camry", "prime": 2000000, "dealership": "A"},
    {"car": "Toyota Camry", "prime": 1900000, "dealership": "B"},
    {"car": "Toyota Camry", "prime": 2200000, "dealership": "C"},
    {"car": "Ford F-150", "prime": 3000000, "dealership": "B"},
    {"car": "Ford F-150", "prime": 4000000, "dealership": "C"},
    {"car": "Honda Civic", "prime": 5000000, "dealership": "A"},
    {"car": "Honda Civic", "prime": 5500000, "dealership": "B"},
    {"car": "Honda Civic", "prime": 6000000, "dealership": "C"},
    {"car": "Volkswagen Golf", "prime": 7000000, "dealership": "A"},
    {"car": "Tesla Model S", "prime": 10000000, "dealership": "A"},
    {"car": "Tesla Model S", "prime": 12000000, "dealership": "B"}
]

for car_data in cars:
    car = Car(car=car_data["car"], prime=car_data["prime"], dealership=car_data["dealership"])
    car.save()