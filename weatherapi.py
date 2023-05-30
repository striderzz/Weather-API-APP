from tkinter import*
import requests
import time
apikey="apikey"
def getWeather(window):
    city=textfield.get()
    api=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}"
    json_data=requests.get(api).json()
    condition=json_data["weather"][0]["main"]
    temp=int(json_data["main"]["temp"]-273.15)
    mintemp = int(json_data["main"]["temp_min"]-273.15)
    maxtemp = int(json_data["main"]["temp_max"]-273.15)
    humidity=json_data["main"]["humidity"]
    pressure=json_data["main"]["pressure"]
    wind=json_data["wind"]["speed"]
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-19800))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-19800))
    #print(condition,round(temp,2))
    final_info=condition+"\n"+str(temp)+".C"
    final_data=("\n"+"Max Temp: "+str(maxtemp)+"\n"+"Min Temp: "+str(mintemp)+"\n"+"Humidity: "+str(humidity)+"\n"+"Pressure: "+str(pressure)+
    "\n"+"Wind Speed: "+str(wind)+"\n"+"Sunrise: "+str(sunrise)+"\n"+"Sunset: "+str(sunset))

    label1.config(text=final_info,font=("Consolas",25,"bold"))
    label2.config(text=final_data)


window=Tk()
window.geometry("600x500")
window.title("Weather App")

f=("poppins",25,"bold")
t=("poppins",50,"bold")


textfield=Entry(window,font=t)
textfield.pack(pady=20)
textfield.focus()
textfield.bind("<Return>",getWeather)

label1=Label(window,font='f')
label1.pack()
label2=Label(window,font='f')
label2.pack()

window.mainloop()

