
class FoodTruck:
    pk: int = 1

    def __init__(self, name=str, food_type=str, rating=float) -> None:
        self.__id = FoodTruck.pk
        self.__name = name
        self.__food_type = food_type
        self.__rating = float("{0:0.1f}".format(rating))
        FoodTruck.pk += 1

    def __str__(self) -> str:
        return f"\n \
        -------------------------\n \
        | ID: {self.__id} \n \
        | Name: {self.__name} \n \
        | Food: {self.__food_type} \n \
        | Rating: {self.__rating} \n \
        -------------------------"

    """
    Getters and Setters
    """
    def get_id(self) -> int:
        return self.__id

    def set_name(self, name=str) -> None:
        self.__name = name
    def get_name(self) -> str:
        return self.__name

    def set_food_type(self, food_type=str) -> None:
        self.__food_type = food_type
    def get_food_type(self) -> str:
        return self.__food_type

    def set_rating(self, rating=float) -> None:
        self.__rating = float("{0:0.1f}".format(rating))
    def get_rating(self) -> float:
        return self.__rating

