# t = "a", "b", "c"
# print(t)
#
# print("a", "b", "c")
# print(("a", "b", "c"))

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company" "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Imilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print(metallica)
# print(metallica[0])
# print(metallica[1])
# print(metallica[2])
#
# # metallica[0] = "Master of Puppets"  # Error, tuples does not support item assignment, but slicing and indexing...
#
# imelda = imelda[0], "Imelda May", imelda[2]
# print(imelda)

metallica2 = ["Ride the Lightning", "Metallica", 1984]
print(metallica2)

# a = b = c = d = 12
# print(c)
# a, b = 12, 13
# print(a, b)
#
# a, b = b, a
# print("a is {}".format(a))
# print("b is {}".format(b))

title, artist, year = imelda
print(title)
print(artist)
print(year)
