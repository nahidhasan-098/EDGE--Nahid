# Air Quality Index Calculator for PM2.5
pm25 = float(input("Enter PM2.5 concentration (µg/m³): "))

if pm25 <= 12:
    print("AQI: Good")
elif pm25 <= 35.4:
    print("AQI: Moderate")
elif pm25 <= 55.4:
    print("AQI: Unhealthy for Sensitive Groups")
elif pm25 <= 150.4:
    print("AQI: Unhealthy")
elif pm25 <= 250.4:
    print("AQI: Very Unhealthy")
else:
    print("AQI: Hazardous")