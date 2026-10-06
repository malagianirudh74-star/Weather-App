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

    
