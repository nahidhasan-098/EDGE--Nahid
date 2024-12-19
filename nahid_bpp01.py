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
    
    
    
    
    # AQI Calculator for PM10
pm10 = float(input("Enter PM10 concentration (µg/m³): "))

if pm10 <= 54:
    print("AQI: Good")
elif pm10 <= 154:
    print("AQI: Moderate")
elif pm10 <= 254:
    print("AQI: Unhealthy for Sensitive Groups")
elif pm10 <= 354:
    print("AQI: Unhealthy")
elif pm10 <= 424:
    print("AQI: Very Unhealthy")
else:
    print("AQI: Hazardous")
    
    
    
    
# AQI Calculator for CO
co = float(input("Enter CO concentration (ppm): "))

if co <= 4.4:
    print("AQI: Good")
elif co <= 9.4:
    print("AQI: Moderate")
elif co <= 12.4:
    print("AQI: Unhealthy for Sensitive Groups")
elif co <= 15.4:
    print("AQI: Unhealthy")
elif co <= 30.4:
    print("AQI: Very Unhealthy")
else:
    print("AQI: Hazardous")
    