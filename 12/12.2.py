import requests

def ktod(kelvin):
    kelvin_num = int(kelvin)
    return f"{kelvin_num - 273.15:.2f}"

country = input("Enter the country(can be null):")
municipality = input("Enter the name of the municipality:")
request = f"http://api.openweathermap.org/data/2.5/weather?q={municipality},{country},uk&APPID=b535927b797567382a8f252b3321a171"
response = requests.get(request).json()
if response:
    try:
        print(f"The weather description is '{response['weather'][0]['description']}'")
        print("The temperature is",response["main"]["temp"],"kelvin")
        print("The temperature is",ktod(response["main"]["temp"]),"degree")
    except:
        print("Unexpected format")
else:
    print("No response generated")