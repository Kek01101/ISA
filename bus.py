# 23/9/2020, Blue, Nicolas Keck, Keeps track of people entering and exiting a bus at different stops
# Assuming that the bus starts its route empty and the driver is not a passenger
bus = [100, 0, 0, 20, 0, 20, 0, 20, 0, 20, 0, 20]
people = 0
if len(bus)%2 == 1:
    raise Exception("Bus array must not be odd: People must both enter and leave the bus")
else:
    stops = len(bus) // 2
for a in range(len(bus)):
    if a%2 == 0:
        people += bus[a]
    elif a%2 == 1:
        people -= bus[a]
    if people < 0:
        raise Exception("People leaving the bus must not exceed the people who have entered")
print(f"Passengers on the bus: {people}\nStops passed: {stops}")