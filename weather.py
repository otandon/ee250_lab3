import requests

# WeatherAPI key
WEATHER_API_KEY = 'ea87a03d4eb64955a8673441261102'  # TODO: Replace with your own WeatherAPI key

def get_weather(city):
    # TODO: Build the API request URL using the base API endpoint, the API key, and the city name provided by the user.
    url = "http://api.weatherapi.com/v1/current.json"
    params = {"key": WEATHER_API_KEY, "q": city}
    # TODO: Make the HTTP request to fetch weather data using the 'requests' library.
    try:
        response = requests.get(url, params=params, timeout=10)
    except requests.RequestException as e:
        print(f"Network Error: {e}")
        return
    # TODO: Handle HTTP status codes:
    # - Check if the status code is 200 (OK), meaning the request was successful.
    # - If not 200, handle common errors like 400 (Bad Request), 401 (Unauthorized), 404 (Not Found), and any other relevant codes.
    
    if response.status_code == 200:
        # TODO: Parse the JSON data returned by the API. Extract and process the following information:
        # - Current temperature in Fahrenheit
        # - The "feels like" temperature
        # - Weather condition (e.g., sunny, cloudy, rainy)
        # - Humidity percentage
        # - Wind speed and direction
        # - Atmospheric pressure in mb
        # - UV Index value
        # - Cloud cover percentage
        # - Visibility in miles
        try:
            data = response.json()
        except ValueError:
            print("Error: Could not parse json response")
            return
        current = data.get("current", {})

        condition = current.get("condition", {})
        temp_f = current.get("temp_f")
        feelslike_f = current.get("feelslike_f")
        condition_text = condition.get("text")
        humidity = current.get("humidity")
        wind_mph = current.get("wind_mph")
        wind_dir = current.get("wind_dir")
        pressure_mb = current.get("pressure_mb")
        uv = current.get("uv")
        cloud = current.get("cloud")
        vis_miles = current.get("vis_miles")
        # TODO: Display the extracted weather information in a well-formatted manner.
        print(f"Status {response.status_code}: OK")
        print(f"Weather for {city}:")
        print(f"Temperature: {temp_f}°F (feels like {feelslike_f}°F)")
        print(f"Condition: {condition_text}")
        print(f"Humidity: {humidity}%")
        print(f"Wind: {wind_mph} mph {wind_dir}")
        print(f"Pressure: {pressure_mb} mb")
        print(f"UV Index: {uv}")
        print(f"Cloud cover: {cloud}%")
        print(f"Visibility: {vis_miles} miles")
    else:
        # TODO: Implement error handling for common status codes. Provide meaningful error messages based on the status code.
        if response.status_code == 400:
            print("Error 400 (Bad Request): City name may be invalid or request is malformed.")
        elif response.status_code == 401:
            print("Error 401 (Unauthorized): API key is missing/invalid.")
        elif response.status_code == 403:
            print("Error 403 (Forbidden): Server understood request but refused it to authorize it.")
        elif response.status_code == 404:
            print("Error 404 (Not Found): City not found.")
        else:
            print(f"Error {response.status_code}: {response.text}")

if __name__ == '__main__':
    # TODO: Prompt the user to input a city name.
    city = input("Enter a city name: ").strip()
    
    # TODO: Call the 'get_weather' function with the city name provided by the user.
    if not city:
        print("Please enter a valid city name.")
    else:
        get_weather(city)
