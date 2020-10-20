from unittest import TestCase

import pet_rescue as pr

class TestPetRescue(TestCase):
    def test_add_pets_to_inventory(self):
        awla = pr.PetRescue()
        awla.add_pets_to_inventory("cats", 12)
        num_pets = awla.get_pet_count("cats")
        self.assertEqual(12, num_pets)
