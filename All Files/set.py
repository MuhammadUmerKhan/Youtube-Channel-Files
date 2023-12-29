#  Making a set
mySet = {"pop","rock","soul","hard Rock","rock","R&B","rock","disco"}
# print(mySet)

# Making list
album_list = ["Micheal Jackson","Thriller","Thriller",1982]
# print(album_list)
# Converting list to set
album_set = set(album_list)
# print(album_set)


# Adding data to set 
A = {"Thriller","Back in Black","AC/DC"}
# print(A)
A.add("NSYNC")  # add() method
# print(A)


# Checking that required data is in table or not
# print("DC" in A)


album_set1 = {"AC/DC","Back in Black",1982}
album_set2 = {"AC/DC","Back in Black","The Dark side of moon",1982}

# Intersection of two set
album_set3 = album_set1 & album_set2
# print(album_set3)

#  Union of two sets
# print(album_set1.union(album_set2))


# Checking that one set is subset of another
print(album_set1.issubset(album_set1))