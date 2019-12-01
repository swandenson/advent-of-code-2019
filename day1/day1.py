# day one:
# (mass / 3 (round down)) - 2


myfile = open("day1_input.txt", "r")
modules = myfile.read()

modules = modules.split("\n")
modules = [int(i) for i in modules]

def calc_fuel(mass):
	for i in range(len(modules)):
		modules[i] = ((modules[i] // 3) - 2)
	return sum(modules)	

print(calc_fuel(modules))

def total_fuel(data):
	totalFuel = 0
	for i in range(len(modules)):
		add_fuel = calc_fuel(modules[i])
		if add_fuel <= 0:
			break
		totalFuel += add_fuel
	return totalFuel

print(total_fuel(modules))