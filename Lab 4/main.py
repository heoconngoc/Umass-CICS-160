import Person
import People

if __name__ == "__main__":
  p1 = Person.Person("steve","ste@", 111)
  p2 = Person.Person("Dat", "dat@", 111)
  p3 = Person.Person("Thien", "ste@", 333)
  
  people = People.People()
  people.add(p1)
  people.add(p2)
  people.add(p3)
  print(people.search(111))