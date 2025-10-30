#Take input from the user (marks), and print:
#	•	A (>= 90)
#	•	B (75–89)
#	•	C (60–74)
#	•	D (<60)

marks = int(input("enter marks: "))
if(marks >= 90 ):
    print("A")
elif(marks >= 75 and marks <= 89):
    print("B")
elif(marks >= 60 and marks <= 74):
    print("C")
else:
    print("D")
