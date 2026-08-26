# Return an iterator a list and print each value:

city = ("Mumbai", "Shanghai", "New York", "Tokyo", "Sydney", "Raipur")
y = len(city)
city = iter(city)
print(type(city))
print(next(city))
print(next(city))#if you want to skip any list element use only next(city) in the place of print(next(city))
print(next(city))
print(next(city))
print(next(city))
print(next(city))

