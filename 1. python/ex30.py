people = 40
cars = 40
trucks = 15

if cars > people:
    print("Cars more.")
elif people > cars : 
    print("People more")
else:
    print("Equal people and cars.")

if cars > trucks:
    print("Cars more.")
elif trucks > cars : 
    print("Trucks more")
else:
    print("Equal trucks and cars.")

if trucks > people:
    print("Trucks more.")
elif people > trucks : 
    print("People more")
else:
    print("Equal people and trucks.")