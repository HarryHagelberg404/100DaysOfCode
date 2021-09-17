# Password Generator
fruits = input("Student heights spaced:\n").split()

for n in range(0, len(fruits)):
    fruits[n] = int(fruits[n])
print(fruits)

# calculate mean
mean = 0
for n in range(0, len(fruits)):
    mean += fruits[n]

mean /= len(fruits)
print(f"Total mean of students:{mean}")
