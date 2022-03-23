This is an example based on: 
	https://github.com/KeithGalli/GUI
	https://www.youtube.com/watch?v=D8-snVfekto&t=1479s

To execute the app simply:
    ./weather_app.py

The get_weather_icons.py is an executable to get the icons from the site: openweathermap.org


/**********************************************************************************************/
    CREATE AN EXECUTABLE

In order to create an executable from this file you need first to install pyinstaller: https://www.pyinstaller.org/
    pip3 install pyinstaller

Once you have pyinstaller installed then go to the app directory, in this case:
    cd python3_examples/apps/weather_app

Finally execute the following command:
    pyinstaller --onefile --icon=./resources/images/sun_icon.ico weather_app.py
