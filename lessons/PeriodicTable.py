from dataclasses import dataclass
from enum import Enum
from typing import ClassVar
class Groups(Enum):
    AlkaliMetals = "Alkali metals"
    Halogens = "Halogens"
@dataclass
class Element():
    weight: float
    group: Groups
    symbol: str
    name: str
    elements: ClassVar[list["Element"]] = []
    def __post_init__(self):
        self.elements.append(self)

Element(6.94, Groups.AlkaliMetals, "Li", "Lithium"  )
Element(22.99, Groups.AlkaliMetals, "Na", "Sodium"  )
Element(39.098, Groups.AlkaliMetals, "K", "Potassium"  )
Element(18.998, Groups.Halogens, "F", "Fluorine"  )
Element(35.45, Groups.Halogens, "Cl", "Chlorine"  )
Element(79.904, Groups.Halogens, "Br", "Bromine"  )
def periodic_table(symbol_or_name):
    if len(searchresult_symbol := [i for i in Element.elements if i.symbol == symbol_or_name]) == 1:
        return searchresult_symbol[0]
    elif len(searchresult_name := [i for i in Element.elements if i.name == symbol_or_name]) == 1:
        return searchresult_name[0]

def main():
    element = periodic_table(input())
    print(
f"""Element: {element.name}
Atomic weight: {element.weight}
Group: {element.group.value}""")

if __name__ == "__main__":
    main()