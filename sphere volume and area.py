pi = 3.1415

radius = float(input("Enter the radius of a sphere in inches: "))

sArea = 4 * pi * (radius ** 2)

volume = sArea * radius / 3

print("The sphere has a surface area of", sArea, "inches and a volume of", volume, "inches")
