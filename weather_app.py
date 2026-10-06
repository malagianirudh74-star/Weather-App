# importing the requests module to make use of API request 
import requests

print("Weather Information System")

while True:

    #input the city whose current weather the user wants to know 
    city = input("Enter the city: ")

    try:
        '''
        using that city name send a request to the GEOCODING API to access the latitude and longitude of the city
        because the OPEN-METEO API only takes latitude and longitude
        ''' 
        response = requests.get(f"https://geocoding-api.open-meteo.com/v1/search?name={city}")

        #Checking if the HTTP status is successful or not, go to exception if unsuccessful
        response.raise_for_status()
    
        '''
        Now that we have sent a request, here's an another request to send the text information as an actual
        dictionary to access only a particular key-value pair from it  
        '''
        data = response.json()

    except:
        print("Unable to get information");
        continue
    
    #handling the invalid/wrong city error
    results = data.get('results')

    if not results:
        print("City not found. Please try again.")
        continue

    #Accesssing only the latitude and longitude from the given data
    lat = data['results'][0]['latitude']
    long = data['results'][0]['longitude']

    #Now, sending a request to the Open-meteo API to give the information
    response1 = requests.get(f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={long}&current=temperature_2m,weather_code")

    #Request to recive the information in the form of dictionary
    data1 = response1.json()
    weather_code = data1['current']['weather_code']

    if weather_code == 0:
        weather = "Clear sky"

    elif weather_code == 1:
        weather = "Mainly clear"

    elif weather_code == 2:
        weather = "Partly cloudy"

    elif weather_code == 3:
        weather = "Overcast"

    elif weather_code == 45 or weather_code == 48:
        weather = "Fog"

    elif weather_code >= 51 and weather_code <= 57:
        weather = "Drizzle"

    elif weather_code >= 61 and weather_code <= 67:
        weather = "Rain"

    elif weather_code >= 71 and weather_code <= 77:
        weather = "Snow"

    elif weather_code >= 80 and weather_code <= 82:
        weather = "Rain showers"

    elif weather_code == 95:
        weather = "Thunderstorm"

    else:
        weather = "Unknown weather condition"

    #Displaying the temperature and weather status
    print(f"\nCurrent Temperature in {city}: ", data1['current']['temperature_2m'], "°C")
    print("Weather:", weather)

    ch=int(input("\nWant to continue? \n1.YES \n2.NO \nEnter 1 or 2: "))
    if ch == 1:
        continue
    else:
        break   

    
