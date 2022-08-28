from FoodTruck import FoodTruck


class FoodTruckApp:
    def __init__(self) -> None:
        self.MAX_FOOD_TRUCKS: int = 5
        self.food_truck_fleet: list[FoodTruck] = [None] * self.MAX_FOOD_TRUCKS

    @staticmethod
    def main() -> None:
        food_truck_app: FoodTruckApp = FoodTruckApp()
        _ = food_truck_app.input_trucks()
        if food_truck_app.food_truck_fleet[0]:
            food_truck_app.menu()
        else:
            print("No Food Trucks in fleet. Quitting . . .")


    def __input_selector(self, input) -> None:
        if input == 1:
            self.list_all_food_trucks()
        elif input == 2:
            print(self.get_average_rating_of_food_trucks())
        elif input == 3:
            print(self.get_highest_rated_food_truck())


    def menu(self) -> None:
        active = True
        while active:
            print("----------------------------------------------")
            print("|  1. List all existing food trucks.         |")
            print("|  2. See the average rating of food trucks. |")
            print("|  3. Display the highest-rated food truck.  |")
            print("|  4. Quit the program.                      |")
            print("----------------------------------------------")
            try:
                user_input = int(input())
                    
                if user_input == 4:
                    active = False
                elif user_input > 0 and user_input < 4:
                    self.__input_selector(user_input) 
                else:
                    print("Not a valid input")
            except:
                print("Not a valid input")

    
    def input_trucks(self) -> bool:
        for i in range(0, self.MAX_FOOD_TRUCKS):
            valid_input = False
            while not valid_input:
                try:
                    print(f"What is the name of Food Truck {i+1} ('quit' to finish data entry)")
                    name = str(input()) 
                    if name == "quit":
                        return False
                    print(f"What is the food of Food Truck {i+1}")
                    food_type = str(input())
                    print(f"What is the rating of Food Truck {i+1}")
                    rating = float(input())
                    valid_input = True
                except:
                    print("Invalid input, please try again")
                    continue

            food_truck = FoodTruck(name=name, food_type=food_type, rating=rating)
            self.food_truck_fleet[i] = food_truck
        return True
    
    def list_all_food_trucks(self) -> None:
        for food_truck in self.food_truck_fleet:
            if food_truck:
                print(food_truck.__str__())


    def get_average_rating_of_food_trucks(self) -> float:
        sum: float = 0
        count = 0
        for food_truck in self.food_truck_fleet:
            if food_truck:
                sum += food_truck.get_rating()
                count += 1

        return float("{0:0.1f}".format(sum / count))
        
    
    def get_highest_rated_food_truck(self) -> str:
        highest_food_truck: FoodTruck = self.food_truck_fleet[0]

        for food_truck in self.food_truck_fleet[1:]:
            if food_truck and food_truck.get_rating() > highest_food_truck.get_rating():
                highest_food_truck = food_truck 

        return highest_food_truck.__str__()

FoodTruckApp.main()