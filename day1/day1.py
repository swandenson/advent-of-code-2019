# day one:
# (mass / 3 (round down)) - 2


myfile = open("day1_input.txt", "r")
modules = myfile.read()

modules = modules.split("\n")
modules = [int(i) for i in modules]
print(modules)

for i in range(len(modules)):
	modules[i] = ((modules[i] // 3) - 2)

print(sum(modules))
