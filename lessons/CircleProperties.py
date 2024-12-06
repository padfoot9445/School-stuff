class Circle:
    @property
    def pi(self) -> float:
        return 3.14
    def __init__(self, diameter: float):
        self.diameter = diameter
    @property
    def radius(self) -> float:
        return self.diameter / 2
    @property
    def circle_area(self) -> float:
        return self.pi * (self.radius ** 2)
    @property
    def circle_circumference(self) -> float:
        return self.diameter * self.pi

def main():
    x = float(input()) #let it throw if not parsable
    assert x not in [float("infinity") , float("-infinity")]
    circle = Circle(x)
    print(f"Area: {circle.circle_area}")
    print(f"Circumference: {circle.circle_circumference}")

if __name__ == "__main__":
    main()
