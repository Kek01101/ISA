import datetime, requests, json, time, random

#I wasn't quite sure what to do for the extension so the death day was what I came up with
#Gets today's date, time until senior, name, and weather. As well as gets a random number for time until death
thetime = time.asctime(time.gmtime()).split(" ")
senior = datetime.date(2021,6,16) - datetime.date.today()
apikey = "5e093de05118836a2ef0b850c653b320"
weather = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={apikey}&q=aberdeen").json()
death = random.randint(1, 10000)
name = input("Good day sir/madam. Please input your name to begin:\n")

#Prints the gathered info back to the user
print(f"Good day, {name}")
print(f"It is currently {thetime[1]} {thetime[2]}")
print(f"There are {senior.days} days left until June 16th, when you will become a senior")
print(f"The prominent weather feature currently should be {weather['weather'][0]['description']}")
print(f"Good news! Your death is only {death} days away!")