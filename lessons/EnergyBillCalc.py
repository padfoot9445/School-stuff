reading = int
KWHMUL = 1.022
KWHDIVIDE = 3.6
COSTMULTIPLIER = 0.0284
CALORIFICVALUE = 39.3
def energy_cost(previous: reading, current: reading, calorific_value: float) -> int:
    units_used: reading = current - previous
    kwh: float = units_used * KWHMUL * (calorific_value / KWHDIVIDE)
    cost: float = COSTMULTIPLIER * kwh
    return int(cost)

def main():
    def __take_reading() -> int:
        r: int = int(input())
        assert -9999 <= r <= 9999, f"reading {r} exceeds limits"
        return r
    pmr = __take_reading()
    cmr = __take_reading()
    print(f"Cost is £ {energy_cost(pmr, cmr, CALORIFICVALUE)}")

if __name__ == "__main__":
    main()