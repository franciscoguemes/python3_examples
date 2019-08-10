#!/usr/bin/python3

# The place layout manager places the widgets at the specific position you want.

# Example inspired from: https://www.youtube.com/watch?v=D8-snVfekto&t=1479s

import tkinter
import requests
import sys
from PIL import Image, ImageTk

HEIGHT = 500
WIDTH = 600

def test_function(entry):
    print(f"This is the entry: {entry}")
    print("This is the entry:", entry)


# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}
def get_weather(city):
    # Here is where you place your openweathermap.org key. In order to get one you need to register
    #weather_key = 'edffd1bf975a74d5d10e58c5ac8be2d3'
    weather_key = 'a4aa5e3d83ffefaba8c00284de6ef7c3'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    weather = response.json()
    #print(weather)  
    label['text'], retrieve_icon = format_response(weather, city)
    if retrieve_icon:
        icon_name = weather['weather'][0]['icon']
        #print(icon_name)
        open_image(icon_name)
    

def format_response(weather, city):
    retrieve_icon = True
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        final_str = 'City: %s \nConditions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:        
        final_str = 'There was a problem retrieving the information for the city: ' + city
        sys.stderr.write(str(weather)) # Print in stderr the original json response form the API.
        retrieve_icon = False

    return final_str, retrieve_icon


def open_image(icon):
    size = int(lower_frame.winfo_height()*0.25)
    img = ImageTk.PhotoImage(Image.open('./resources/images/'+icon+'.png').resize((size, size)))
    weather_icon.delete("all")
    weather_icon.create_image(0,0, anchor='nw', image=img)
    weather_icon.image = img


def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    background_label.config(image = photo)
    background_label.image = photo #avoid garbage collection


window = tkinter.Tk()
window.title("Using place()")
#window.resizable(False,False) # Prevent the window from being resized in the x or y axis

# By adding a canvas is a way to force the main window to have the defined size
canvas = tkinter.Canvas(window, height=HEIGHT, width=WIDTH)
canvas.pack()

# This block of code shows the background image but it does not resize to the window size...
# background_image = tkinter.PhotoImage(file="./resources/images/weather_app/landscape.png")
# background_label = tkinter.Label(window, image=background_image)
# background_label.place(relwidth=1, relheight=1)

# This block resizes the background image to the window size --> https://stackoverflow.com/questions/24061099/tkinter-resize-background-image-to-window-size?rq=1
image=Image.open("./resources/images/landscape.png")
copy_of_image = image.copy()
background_image = ImageTk.PhotoImage(image)
background_label = tkinter.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)
background_label.bind('<Configure>', resize_image)

frame = tkinter.Frame(window,bg="#80c1ff",bd=5)
frame.place(relx=0.5,rely=0.1, relwidth=0.75, relheight=0.1, anchor="n") 

entry = tkinter.Entry(frame, font=('Courier', 18))
entry.place(relwidth=0.65, relheight=1) # Ommited parameters such as relx or rely are set to 0

button = tkinter.Button(frame,text="Get Weather", font=('Courier', 12), command=lambda:get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tkinter.Frame(window, bg="#80c1ff",bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tkinter.Label(lower_frame, font=('Courier', 14), anchor='nw', justify='left', bd=4)
label.place(relwidth=1, relheight=1)

weather_icon = tkinter.Canvas(label, bd=0, highlightthickness=0)
weather_icon.place(relx=.75, rely=0, relwidth=1, relheight=0.5)


window.mainloop()