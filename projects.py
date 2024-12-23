



str_length=input('Please type length:\n')
str_width=input('Plase type width\n')
str_meter=input('How much for 1 meter:\n')
# Convert type from str() to float()
meter=float(str_meter)
length=float(str_length)
width=float(str_width)

# creat area the calculate the length and width
area=length*width

print(f'The total area is {area}.')

# Multiply the area by the meter.
print(f"Give the guy:${area*meter}")











