worldRecord = False
lane = 1
athlete = input("Who is in lane" + str(lane) + "?")
country = input("Which country does" + str(athlete) + "represent?")
time = float(input("Enter the 100m time for" + str(athlete)))

if time < 8.0 or time > 20.0:
    time = "invalid"
elif time < 9.58:
    worldRecord = True

print("Competitor: ", athlete)
print("Country: " + str(country))
print("Lane Number: " + str(lane))
print("100m time: " + str(time))
print("New World Record: " + str(worldRecord))
