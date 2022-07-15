import tkinter as tk
import requests
import datetime

def get_covid_data():
    api = "https://disease.sh/v3/covid-19/all"
    json_data = requests.get(api).json()
    total_cases = str(json_data['cases'])
    total_deaths = str(json_data['deaths'])
    today_cases = str(json_data['todayCases'])
    today_deaths = str(json_data['todayDeaths'])
    today_recovered = str(json_data['todayRecovered'])
    updated_at = json_data['updated']
    date = datetime.datetime.fromtimestamp(updated_at/1e3)
    label.config(text="Total Cases: " + total_cases + "\nTotal Deaths: " + total_deaths + "\nToday's Cases: " + today_cases + "\nToday's Deaths: " + today_deaths + "\nRecovered: " + today_recovered)
    label2.config(text = date)
canvas = tk.Tk()
canvas.geometry("400x400")
canvas.title("Covid-19 Tracker")

f = ("poppins", 20, "bold")
button = tk.Button(canvas, text="Get Data", font=f, command=get_covid_data)
button.pack(pady=20)

label =tk.Label(canvas, text="Covid-19 Tracker", font=f)
label.pack(pady=20)

label2 = tk.Label(canvas, font=8)
label2.pack()
get_covid_data()
canvas.mainloop()