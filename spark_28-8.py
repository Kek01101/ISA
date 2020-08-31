"""
Problem category: Spark of Learning
Problem definition: Create a short program to determine what
                    drink someone is drinking based upon
                    the e's in their name
Attempted solutions: Just this one, it was easy enough
Reflections: As was said in class, once you know what the
             solution to the spark is, it's pretty easy to
             implement.
"""
drinks = dict()
people = ["Elizabeth", "Bert", "Dave", "Helen"]
for person in people:
    if person.lower().count("e") == 2:
        drinks[person] = "Coffee"
    else:
        drinks[person] = "Soda"
