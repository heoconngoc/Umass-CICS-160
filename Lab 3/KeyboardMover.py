class KeyboardMover:
    def __init__(self, vehicle, key_char):
        self.vehicle = vehicle
        self.key = key_char

    def processOneEvent(self):
        key_pressed = input("Enter move key (or 'q' to quit): ").strip().lower()
        
        if key_pressed == self.key:
            self.vehicle.setPosition(self.vehicle.getX() + 1, self.vehicle.getY())

        if key_pressed == 'q':
            return False  # Exit condition

        return True