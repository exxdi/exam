class House:
    def __init__(self):
        self.floors = []
    def add_floor(self, count_of_flats, maximal_area):
        if self.floors and maximal_area > self.floors[-1].maximal_area:
            print("You can't input more area than the floor below!")
            return
        self.floors.append(Floor(count_of_flats, maximal_area))
    def __str__(self):
        total_area = sum(floor.maximal_area for floor in self.floors)
        total_flats = sum(floor.count_of_flats for floor in self.floors)
        total_floors = len(self.floors)
        return f"Your house has {total_floors} floors, {total_flats} flats, a total area of {total_area} square meters (кв.м)."
class Floor:
    def __init__(self, count_of_flats, maximal_area):
        self.flats = [Flat(maximal_area // count_of_flats) for _ in range(count_of_flats)]
        self.maximal_area = maximal_area
        self.count_of_flats = count_of_flats
class Flat:
    def __init__(self, area):
        self.area = area
building = House()
floors_count = int(input("Enter how many floors you want in your house: "))
for i in range(floors_count):
    count_of_flats = int(input(f"Enter how many flats you want on floor {i+1}: "))
    maximal_area = int(input(f"Enter how much area you want on floor {i+1}: "))
    building.add_floor(count_of_flats, maximal_area)
print(building)