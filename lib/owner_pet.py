class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

        if owner:
            owner.add_pet(self)


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        """Returns all pets associated with the owner."""
        return self._pets

    def add_pet(self, pet):
        """Adds a pet to the owner's collection, ensuring it's a valid Pet instance."""
        if not isinstance(pet, Pet):
            raise Exception("Only instances of Pet can be added.")
        if pet not in self._pets:  # Avoid duplicate entries
            pet.owner = self
            self._pets.append(pet)

    def get_sorted_pets(self):
        """Returns pets sorted by their name."""
        return sorted(self._pets, key=lambda pet: pet.name)