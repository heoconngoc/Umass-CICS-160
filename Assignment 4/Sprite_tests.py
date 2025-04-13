import unittest
from Sprite_collection import Sprite_collection
from My_sprite import My_sprite

class Sprite_tests(unittest.TestCase):
  def test_with_match_at_first(self):
    target = My_sprite("./Images/green_car.png", (0, 0))
    sc = Sprite_collection()
    
    s1 = My_sprite("./Images/green_car.png", (0, 0)) #result
    s2 = My_sprite("./Images/orange_truck.png", (10, 10))
    s3 = My_sprite("./Images/red_car.png", (10, 10))
    s4 = My_sprite("./Images/tree.png", (10, 10))
    
    sc.add(s1)
    sc.add(s2)
    sc.add(s3)
    sc.add(s4)
    result = sc.search(target)
    self.assertEqual(result, [s1])
    
  def test_with_match_at_end(self):
    target = My_sprite("./Images/green_car.png", (10, 10))
    sc = Sprite_collection()
    
    s1 = My_sprite("./Images/tree.png", (0, 0))
    s2 = My_sprite("./Images/orange_truck.png", (0, 0))
    s3 = My_sprite("./Images/red_car.png", (0, 0))
    s4 = My_sprite("./Images/green_car.png", (10, 10)) #result
    sc.add(s1)
    sc.add(s2)
    sc.add(s3)
    sc.add(s4)
    result = sc.search(target)
    self.assertEqual(result, [s4])
    
  def test_with_match_at_random_pos(self):
    target = My_sprite("./Images/green_car.png", (10, 10))
    sc = Sprite_collection()
    
    s1 = My_sprite("./Images/tree.png", (0, 0))
    s2 = My_sprite("./Images/orange_truck.png", (0, 0))
    s3 = My_sprite("./Images/green_car.png", (10, 10)) #result
    s4 = My_sprite("./Images/red_car.png", (0, 0))
    sc.add(s1)
    sc.add(s2)
    sc.add(s3)
    sc.add(s4)
    result = sc.search(target)
    self.assertEqual(result, [s3])

  def test_multiple_matches(self):
    target = My_sprite("./Images/green_car.png", (10,10))
    sc = Sprite_collection()
    
    s1 = My_sprite("./Images/tree.png", (0, 0))
    s2 = My_sprite("./Images/orange_truck.png", (0, 0))
    s3 = My_sprite("./Images/green_car.png", (10, 10)) #result
    s4 = My_sprite("./Images/green_car.png", (10, 10)) #result
    s5 = My_sprite("./Images/red_car.png", (0, 0))
    sc.add(s1)
    sc.add(s2)
    sc.add(s3)
    sc.add(s4)
    sc.add(s5)
    result = sc.search(target)
    self.assertEqual(result, [s3, s4])  
      
if __name__ == '__main__':
    unittest.main()