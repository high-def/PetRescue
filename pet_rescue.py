class PetRescue:
    # the constructor
    def __init__(self):
        self.inventory = {"cats": 0,
                          "dogs": 0,
                          "rabbits": 0,
                          "reptiles": 0}
    def add_pets_to_inventory(self, pet_type: str, amount: int):
        self.inventory[pet_type] += amount

    def get_pet_count(self, pet_type: str) -> int:
        return self.inventory[pet_type]
