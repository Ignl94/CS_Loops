# Question 1
songs = ["ROCKSTAR", "Do It", "For The Night"]
# Question 2
print(songs[0])
print(songs[2])
print(songs[1:])
# Question 3
songs[2] = "Just Dance"
# Question 4
songs.extend(["Boom Boom Pow", "Fireflies", "Crazy Kids"])
del songs[0]
# Question 6
animals = ["Kangaroo", "Emu", "Orcha"]
animals.append("Kamodo Dragon")
print(animals[2])
del animals[0]
for i in animals:
    print(i)
