done = ''
list = []
weight = []
while done != "yes":
    inp = int(input("Enter grade recieved: "))
    w = int(input("Enter weight: "))
    done = input("done? ")
    weight.append(w)
    list.append((inp/100)* w)

final = int(input("what grade would you like? "))
if sum(weight) >=100:
    print("not possible")
else:
    t= 100 - sum(weight)
    sum = final - sum(list)
    newsum = (sum/t)*100
    print("you will need a", newsum, "% to get you target grade")
