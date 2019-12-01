def mass_needed(mass):

    fuel = (mass // 3) - 2

    if fuel < 0:
        fuel = 0
        
    return fuel


def calc_fuel(masses):

    fuel_needed = [mass_needed(mass) for mass in masses]

    return fuel_needed


def determine_fuels():

    inputs = 'input.txt'
    masses = []
    with open(inputs) as f:
        masses = [int(line.strip()) for line in f]
        print(masses)

    fuel_needs = [calc_fuel(masses)]

    required_total = sum(fuel_needs[0])

    done = False

    while not done:
        prev_fuels = fuel_needs[-1]
        new_fuels = calc_fuel(prev_fuels)
        if sum(new_fuels) == 0:
            done = True
        else:
            fuel_needs.append(new_fuels)

    #print(fuel_needs)
    print(f"Required Amount = {required_total}")

    sums = [sum(mass) for mass in fuel_needs]
    sums = sum(sums)
    print(f"Total fuel required = {sums}")


if __name__ == "__main__":
    determine_fuels()