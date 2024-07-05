list1 = ["dev", "111", "e111"]
list2 = ["stg", "22", "e222"]
list3 = ["qa", "33", "e333"]
list4 = ["dev", "444", "e444"]

d = {}

d[l[0]] = {l[1]:l[2]}

print(d)