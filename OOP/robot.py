
class Robot:
    # constant attribute
    MAX_ENERGY = 100

    def __init__(self, name="Robot", age=0):
        # instance attribute
        self.name = name
        self.age = age
        self.energy = Robot.MAX_ENERGY

    #instance method:
    def display(self):
        print(f"I am {self.name}")

if (__name__ == "__main__"):
  robot = Robot()
  robot.display()
