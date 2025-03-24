class Person:
    def __init__(self, n="no one", e="no email", a = 0):
      self.name = n
      self.email = e
      self.age = a
    def __str__(self):
      return("{" + self.name + "," + str(self.age) + "}")
    def  __eq__(self, a:int):
      return self.age == a
      

if __name__=="__main__":
    pass