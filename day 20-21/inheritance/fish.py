from animal import Animal

class Fish(Animal):

    def __init__(self):
        super().__init__()

    def swim(self):
        print("Moving in water.")

    def breathe(self):
        super().breathe()  # Call the parent class's breathe method
        print("Fish are breathing through gills.")
        