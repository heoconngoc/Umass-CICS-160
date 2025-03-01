import Vehicle
import KeyboardMover
import Map

def main():
    car1 = Vehicle.Vehicle("O", locx=0, locy=2) 
    tree = Vehicle.Vehicle("T", locx=4, locy=3)  
    car2 = Vehicle.Vehicle("X", locx=2, locy=2)  
    
    listOfVehicles = [car1, tree, car2]
    
    kbReader       = KeyboardMover.KeyboardMover(car1, "l")
    kbReader2      = KeyboardMover.KeyboardMover(car2, "d")
    
    myMap          = Map.Map((10,5))
    
    keepRunning = True
    while (keepRunning):
        keepRunning = kbReader.processOneEvent() and kbReader2.processOneEvent()
        myMap.update(listOfVehicles)
            
if __name__ == "__main__":
    main()
