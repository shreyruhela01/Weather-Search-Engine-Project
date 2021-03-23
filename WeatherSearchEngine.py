import requests
from gtts import gTTS
import pyglet
from tkinter import *
from datetime import date
import playsound


now = date.today()
root = Tk()
name = 1
root.geometry("600x400")
root.title('Weather Forecast')
root.config(bg="black")

root.wm_attributes("-alpha", 0.95)


def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if enter_city.get() == 'Enter your city name...':
        enter_city.delete(0, "end")  # delete all the text in the entry
        enter_city.insert(0, '')  # Insert blank for user input
        enter_city.config(fg='white')


def on_focusout(event):
    if enter_city.get() == '':
        enter_city.insert(0, 'Enter your username...')
        enter_city.config(fg='grey')


def play(location):
    playsound.playsound(location, False)


def search_city():
    global name
    city = enter_city.get()
    url = "https://openweathermap.org/data/2.5/weather?q={}&appid=439d4b804bc8187953eb36d2a8c26a02".format(city)
    res = requests.get(url)
    output = res.json()
    weather = output['weather'][0]['description']
    temperature = output['main']['temp']
    humidity = output['main']['humidity']
    wind = output['wind']['speed']
    label_city.configure(text="{}".format(city.split(",")[0]))

    label_temp.configure(text="{}".format(str(temperature)) + "C")

    label_weather.configure(text="{}".format(weather))

    label_humidity.configure(text="Humidity: " + "{}".format(str(humidity)) + "%")

    label_wind.configure(text="Wind: " + "{}".format(str(wind)) + "m/s")
    label_date.configure(text="{}".format(now.strftime("%B %d, %Y")))

    read_content = 'Currently we are experiencing {} in {} \n The temperature is around {} degree celsius with {} percent humidity in air. \n The wind is blowing at a rate of {} meters per second '.format(
        weather, city.split(",")[0], str(temperature), humidity, wind)
    output_speech = gTTS(text=read_content, lang='en', slow=False)
    filename = "weather" + str(name) + ".mp3"
    name += 1
    output_speech.save(filename)
    play(filename)


enter_city = Entry(root, font=("Helvetica", 12), width=30, bd=8, bg="black", fg="white")
enter_city.insert(0, 'Enter your city name...')
enter_city.bind('<FocusIn>', on_entry_click)
enter_city.bind('<FocusOut>', on_focusout)
enter_city.config(fg='grey')
enter_city.place(x=90, y=30)

search_button = Button(root, text='Search', font=("Helvetica", 16), bd=10, fg="aquamarine", command=search_city,
                       bg="black")
search_button.place(x=400, y=20)

label_city = Label(root, font=("Helvetica", 40), fg="aquamarine", bg="black")

label_city.place(x=70, y=80)

label_date = Label(root, font=("Helvetica", 20), fg="aquamarine", bg="black")

label_date.place(x=70, y=130)

# -- coding : utf-8 --

label_temp = Label(root, font=("Arial", 60), fg="aquamarine", bg="black")

label_temp.place(x=330, y=120)

label_weather = Label(root, font=("Helvetica", 20), fg="aquamarine", bg="black")

label_weather.place(x=70, y=170)

label_humidity = Label(root, font=("Helvetica", 20), fg="aquamarine", bg="black")

label_humidity.place(x=70, y=200)

label_wind = Label(root, font=("Helvetica", 20), fg="aquamarine", bg="black")

label_wind.place(x=70, y=230)

root.resizable(False, False)

root.mainloop()


