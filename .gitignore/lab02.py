

f = open("score2.txt", "r")

listOfStudents = []
totalScores = {}

for x in f:
    listOfStudents.append(x.split())
    firstName = listOfStudents[-1][2]
    lastName = listOfStudents[-1][3]
    point = int(listOfStudents[-1][4])
    
    if(firstName + ' ' + lastName) not in totalScores.keys():
        totalScores[firstName + ' ' + lastName] = point

    else:
        totalScores[firstName + ' ' + lastName] += point


orderdList= sorted(totalScores.items(),reverse=True, key=lambda item: item[1])
highestValue = orderdList[0][1]

for x in orderdList:
    if x[1] >= highestValue :
        print(x)


f.close()


 