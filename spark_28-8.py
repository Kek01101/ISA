#Spark of learning challenge from the 28th of August
drinks = dict()
people = ["Elizabeth", "Bert", "Dave", "Helen"]
for person in people:
    if person.lower().count("e") == 2:
        drinks[person] = "Coffee"
    else:
        drinks[person] = "Soda"
