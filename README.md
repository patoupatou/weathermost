# Weathermost fork
Weathermost is a Python bot that fetches weather from openweather and posts it back on a mattermost channel.

# How to use it
1. Get an OpenWeatherAPI key: http://openweathermap.org/appid
2. Put the key into the bot.py script (user_api).
3. Upload the script to a server (one that is reachable from the Mattermost server).
4. Run the script or add it as a service.
5. Go to the Mattermost "Integrations" page and add another slash command.
6. Point the slash command to the server the script is running on.
7. Go to the chat rooms and try your integration!

![alt text](https://raw.githubusercontent.com/cjohannsen81/weathermost/master/images/example.png)

# Changes in this fork
With this for I changed a few things:

1) Added UTF-8 encoding
2) Added configuration directly in the script
3) Changed the OpenWeather API to the city name URL
4) Changed the URi into root and added the "city" option
5) Added Humidity as an information
6) Let the script listen to a public IP address
