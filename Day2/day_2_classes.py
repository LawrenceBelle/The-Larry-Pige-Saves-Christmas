
class Cube:
    def __init__(
            self, 
            quantity: int,
            colour: str) -> None:
        
        self.quantity = quantity
        self.colour = colour

    def __str__(self):
        return f"Colour: {self.colour}, Quantity: {self.quantity}"

class Sample:
    def __init__(
            self,
            cubes: list[Cube]) -> None:
        
        self.cubes = cubes

    def __str__(self):
        sample_string = ''
        for cube in self.cubes:
            sample_string += f"{str(cube)}\n"

        return sample_string

class GameData:
    def __init__(
            self, 
            id: int,
            samples: list[Sample]) -> None:
        
        self.id = id
        self.samples = samples

    def __str__(self):
        samples_string = ''
        for sample in self.samples:
            samples_string += f"\n{str(sample)}"

        return f"Game Id = {self.id} \n\nSamples:{samples_string}\n"