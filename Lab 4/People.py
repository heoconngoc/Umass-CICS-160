class People:
    def __init__(self):
      self.people_list = []

    def add(self, person):
      self.people_list.append(person)
            
    def __str__(self):
      return "[" + ", ".join(str(p) for p in self.people_list) + "]"

    def search(self, a:int):
      peo_res = People()
      for peo in self.people_list:
        if peo.age == a:
          peo_res.add(peo)
      return peo_res