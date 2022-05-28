# set => a set is collection which is unordered and unindexed. No duplicate values

utensils = {"fork","spoon","knife"}
dishes = {"bowl", "plate","cup","knife"}

utensils.add("napkin")
utensils.remove("fork")
# utensils.update(dishes)

dinner_table = utensils.union(dishes)
print(utensils.difference(dishes))
print(utensils.intersection(dishes))


for x in dinner_table:
    print(x)
    
utensils.clear()