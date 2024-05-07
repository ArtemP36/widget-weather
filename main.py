from tkinter import * 
import requests 
import json 
import datetime 
 
with open('data.json', 'r') as file: 
    loaded_data = json.load(file) 
 
city = loaded_data.get("city") 
api_key = loaded_data.get("api_key") 
 
root = Tk() 
root.title('Widget') 
 
screen_height = root.winfo_screenheight() 
screen_width = root.winfo_screenwidth() 
root.geometry("230x140+{}+{}".format(screen_width - 250, screen_height - 1050)) 
root.overrideredirect(True) 
root.configure(background="black") 
root.resizable(0, 0) 
root.wm_attributes('-topmost', True)  
root.grab_set() 
root.lift()  # Setting the window to stay in front of other windows 
root.attributes("-toolwindow", 1) 
root.attributes("-alpha", 0.50)  # Setting window transparency 
 
def update_weather(): 
    get_weather(city) 
    root.after(3600000, update_weather)  
 
def get_weather(city): 
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric" 
    response = requests.get(url) 
    if response.status_code == 200: 
        data = response.json() 
        city = data["name"] 
        country = data["sys"]["country"] 
        temp = data["main"]["temp"] 
        main = data["weather"][0]["main"] 
    else: 
        print("error") 
 
    def update_time(): 
        time = datetime.datetime.now() 
        date_time = time.strftime("%A %d.%m.%Y %H:%M") 
        time_label.config(text=f"{date_time}") 
        root.after(1000, update_time) 
 
    city_label = Label(root, font=("Montserrat", 23, "bold"), background="black", foreground="white", anchor="n") 
    city_label.config(text=f"{city}, {country}") 
    city_label.pack(anchor="nw", padx=3, pady=3) 
 
    weather_label = Label(root, font=("Montserrat", 23, "bold"), background="black", foreground="white", anchor="n") 
    weather_label.config(text=f"{temp}°С {main}") 
    weather_label.pack(anchor="nw", padx=3, pady=3) 
 
    time_label = Label(root, font=("Montserrat", 12,),  background="black", foreground="white") 
    time_label.pack(anchor="nw", padx=3, pady=3) 
 
    update_time() 
 
update_weather() 
  
root.mainloop()
