from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import ttk, messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image, ImageTk
from statistics import mean
import os

root  = Tk()
root.title("Weather App")
root.geometry("890x470+300+300")
root.configure(bg = "#57adff")
root.resizable(False, False)

def get_weather_icon(weather_code, is_day=True):
    """Map weather codes to icon files"""
    icon_mapping = {
        0: "01",  # Clear sky
        1: "02",  # Partly cloudy
        2: "03",  # Cloudy
        3: "04",  # Overcast
        45: "50", # Foggy
        48: "50", # Depositing rime fog
        51: "09", # Light drizzle
        53: "09", # Moderate drizzle
        55: "09", # Dense drizzle
        56: "09", # Light freezing drizzle
        57: "09", # Dense freezing drizzle
        61: "10", # Slight rain
        63: "10", # Moderate rain
        65: "10", # Heavy rain
        66: "10", # Light freezing rain
        67: "10", # Heavy freezing rain
        71: "13", # Slight snow
        73: "13", # Moderate snow
        75: "13", # Heavy snow
        77: "13", # Snow grains
        80: "09", # Slight rain showers
        81: "09", # Moderate rain showers
        82: "09", # Violent rain showers
        85: "13", # Slight snow showers
        86: "13", # Heavy snow showers
        95: "11", # Thunderstorm
        96: "11", # Thunderstorm with slight hail
        99: "11", # Thunderstorm with heavy hail
    }
    
    icon_code = icon_mapping.get(weather_code, "01")
    time_suffix = "d" if is_day else "n"
    icon_path = f"other_photos/icon/{icon_code}{time_suffix}@2x.png"
    
    # Check if file exists, otherwise use default
    if not os.path.exists(icon_path):
        icon_path = f"other_photos/icon/01{time_suffix}@2x.png"
    
    return icon_path

def getWeather():
    city = str(text_field.get())
    geolocator = Nominatim(user_agent = "myapplication")
    location = geolocator.geocode(city, timeout = None)
    obj = TimezoneFinder()
    result = obj.timezone_at(lng = location.longitude, lat = location.latitude)
    timezone.config(text = result)
    long_lat.config(text = f"{round(location.latitude, 4)} °N, {round(location.longitude, 4)}°E")

    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")
    clock.config(text = current_time)

    # Get current weather
    api = f""    
    json_data = requests.get(api).json()
    temp = json_data['current']['temperature_2m']
    humidity = round(mean(json_data['hourly']['relative_humidity_2m']), 2)
    wind = json_data['current']['wind_speed_10m']
    
    t.config(text = (temp, "°C"))
    h.config(text = (humidity, "%"))
    w.config(text = (wind, "m/s"))

    # Get 7-day forecast
    forecast_api = f""
    forecast_data = requests.get(forecast_api).json()
    
    # Update day labels and weather images
    first = datetime.now()
    day1.config(text = first.strftime("%A"))
    second = first + timedelta(days = 1)
    day2.config(text = second.strftime("%A"))
    third = first + timedelta(days = 2)
    day3.config(text = third.strftime("%A"))
    forth = first + timedelta(days = 3)
    day4.config(text = forth.strftime("%A"))
    fifth = first + timedelta(days = 4)
    day5.config(text = fifth.strftime("%A"))
    sixth = first + timedelta(days = 5)
    day6.config(text = sixth.strftime("%A"))
    seventh = first + timedelta(days = 6)
    day7.config(text = seventh.strftime("%A"))

    # Update weather images for each day
    try:
        # First frame (today) - use current weather
        current_weather_code = forecast_data['daily']['weather_code'][0]
        icon_path = get_weather_icon(current_weather_code, True)
        weather_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((50, 50)))
        firstimage.config(image=weather_icon)
        firstimage.image = weather_icon

        # Second frame (tomorrow)
        weather_code = forecast_data['daily']['weather_code'][1]
        icon_path = get_weather_icon(weather_code, True)
        weather_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((50, 50)))
        secondimage.config(image=weather_icon)
        secondimage.image = weather_icon

        # Third frame
        weather_code = forecast_data['daily']['weather_code'][2]
        icon_path = get_weather_icon(weather_code, True)
        weather_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((50, 50)))
        thirdimage.config(image=weather_icon)
        thirdimage.image = weather_icon

        # Fourth frame
        weather_code = forecast_data['daily']['weather_code'][3]
        icon_path = get_weather_icon(weather_code, True)
        weather_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((50, 50)))
        forthimage.config(image=weather_icon)
        forthimage.image = weather_icon

        # Fifth frame
        weather_code = forecast_data['daily']['weather_code'][4]
        icon_path = get_weather_icon(weather_code, True)
        weather_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((50, 50)))
        fifthimage.config(image=weather_icon)
        fifthimage.image = weather_icon

        # Sixth frame
        weather_code = forecast_data['daily']['weather_code'][5]
        icon_path = get_weather_icon(weather_code, True)
        weather_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((50, 50)))
        sixthimage.config(image=weather_icon)
        sixthimage.image = weather_icon

        # Seventh frame
        weather_code = forecast_data['daily']['weather_code'][6]
        icon_path = get_weather_icon(weather_code, True)
        weather_icon = ImageTk.PhotoImage(Image.open(icon_path).resize((50, 50)))
        seventhimage.config(image=weather_icon)
        seventhimage.image = weather_icon

    except Exception as e:
        print(f"Error loading weather icons: {e}")




app_icon = PhotoImage(file = "All_photos/icon2.png")
root.iconphoto(False, app_icon)

photo1 = ImageTk.PhotoImage(Image.open("All_photos/rectangle.jpg").resize((180, 120)))
label0 = Label(root, image = photo1, bg = "#57adff")
label0.place(x = 30, y = 110)

lable1 = Label(root, text = "Temprature", fg = "white", bg = "#000000", font = ("poppins",12,"bold"))
#lable2 = Label(root, text = "Pressure", fg = "white", bg = "#000000", font = ("poppins",12,"bold"))
lable3 = Label(root, text = "Humidity", fg = "white", bg = "#000000", font = ("poppins",12,"bold"))
#lable4 = Label(root, text = "Description", fg = "white", bg = "#000000", font = ("poppins",12,"bold"))
lable5 = Label(root, text = "Wind Speed", fg = "white", bg = "#000000", font = ("poppins",12, "bold")) 

lable1.place(x = 50, y = 120)
#lable2.place(x = 50, y = 140)
lable3.place(x = 50, y = 160)
#lable4.place(x = 50, y = 180)
lable5.place(x = 50, y = 200)


photo2 = ImageTk.PhotoImage(Image.open("All_photos\Rounded Rectangle 3.png").resize((450, 60)))
label6 = Label(root, image = photo2, bg = "#57adff")
label6.place(x = 270, y = 120)

search_icon = ImageTk.PhotoImage(Image.open("All_photos/icon2.png").resize((45,45)))
label7 = Label(root, image = search_icon, bg = "#203243")
label7.place(x = 290, y = 127)
text_field = Entry(root, justify = "center", width = 15, font = ("poppins", 25,"bold"), bg = "#203243", border = 0, fg = "white")
text_field.place(x = 370, y = 130)
text_field.focus()
microscope = ImageTk.PhotoImage(Image.open("All_photos\microscope.png"))
search_button = Button(image = microscope, borderwidth = 0, cursor = "hand2", bg = "#203243", command = getWeather)
search_button.place(x = 645, y = 125)

frame = Frame(root, width = 900, height = 180, bg = "#212120").pack(side = BOTTOM)
box1 = ImageTk.PhotoImage(Image.open("All_photos\Rounded Rectangle 2.png"))
box2 = ImageTk.PhotoImage(Image.open("All_photos\Rounded Rectangle 2 copy.png"))
Label(frame, image = box1, bg = "#212120").place(x = 30, y = 310)
Label(frame, image = box2, bg = "#212120").place(x = 300, y = 320)
Label(frame, image = box2, bg = "#212120").place(x = 400, y = 320)
Label(frame, image = box2, bg = "#212120").place(x = 500, y = 320)
Label(frame, image = box2, bg = "#212120").place(x = 600, y = 320)
Label(frame, image = box2, bg = "#212120").place(x = 700, y = 320)
Label(frame, image = box2, bg = "#212120").place(x = 800, y = 320)

clock = Label(root, font = ("poppins", 30), fg = "white", bg = "#57adff")
clock.place(x = 30, y = 20)

timezone = Label(root, font = ("poppins", 20), fg = "white", bg = "#57adff")
timezone.place(x = 700, y = 20)

long_lat = Label(root, font = ("poppins", 10, "bold"), fg = "white", bg = "#57adff")
long_lat.place(x = 700, y = 50)

t = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#000000")
t.place(x = 150, y = 120)
h = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#000000")
h.place(x = 150, y = 160)
w = Label(root, font = ("Helvetica", 11), fg = "white", bg = "#000000")
w.place(x = 150, y = 200)

firstframe = Frame(root, width = 230, height = 132, bg = "#282829")
firstframe.place(x = 35, y = 315)
day1 = Label(firstframe, font = "arial 20", bg = "#282829", fg = "#fff")
day1.place(x = 100, y = 5)
firstimage = Label(firstframe, bg = "#282829")
firstimage.place(x = 1, y = 15)

secondframe = Frame(root, width = 70, height = 115, bg = "#282829")
secondframe.place(x = 305, y = 325)
day2 = Label(secondframe, bg = "#282829", fg = "#fff")
day2.place(x = 10, y = 5)
secondimage = Label(secondframe, bg = "#282829")
secondimage.place(x = 7, y = 20)

thirdframe = Frame(root, width = 70, height = 115, bg = "#282829")
thirdframe.place(x = 405, y = 325)
day3 = Label(thirdframe, bg = "#282829", fg = "#fff")
day3.place(x = 10, y = 5)
thirdimage = Label(thirdframe, bg = "#282829")
thirdimage.place(x = 7, y = 20)

forthframe = Frame(root, width = 70, height = 115, bg = "#282829")
forthframe.place(x = 505, y = 325)
day4 = Label(forthframe, bg = "#282829", fg = "#fff")
day4.place(x = 10, y = 5)
forthimage = Label(forthframe, bg = "#282829")
forthimage.place(x = 7, y = 20)

fifthframe = Frame(root, width = 70, height = 115, bg = "#282829")
fifthframe.place(x = 605, y = 325)
day5 = Label(fifthframe, bg = "#282829", fg = "#fff")
day5.place(x = 10, y = 5)
fifthimage = Label(fifthframe, bg = "#282829")
fifthimage.place(x = 7, y = 20)

sixthframe = Frame(root, width = 70, height = 115, bg = "#282829")
sixthframe.place(x = 705, y = 325)
day6 = Label(sixthframe, bg = "#282829", fg = "#fff")
day6.place(x = 10, y = 5)
sixthimage = Label(sixthframe, bg = "#282829")
sixthimage.place(x = 7, y = 20)

seventhframe = Frame(root, width = 70, height = 115, bg = "#282829")
seventhframe.place(x = 805, y = 325)
day7 = Label(seventhframe, bg = "#282829", fg = "#fff")
day7.place(x = 10, y = 5)
seventhimage = Label(seventhframe, bg = "#282829")
seventhimage.place(x = 7, y = 20)

root.mainloop()