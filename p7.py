# 7. Menu Driven Program: Student Result SystemOperations:
# Enter Marks
# Calculate Percentage
# Assign Grade

sub1=int(input("Enter subject 1 marks: "))
sub2=int(input("Enter subject 2 marks: "))
sub3=int(input("Enter subject 3 marks: "))


def marks(sub1,sub2,sub3):

    return (sub1 + sub2 + sub3) / 300 * 100

total=marks(sub1,sub2,sub3)
total1=total*100
print("Percentage of student is:",total)

def grad(total):
    if total >= 75:
        return "A Grade"
    elif total >= 50:
        return "B Grade"
    elif total >= 40:
        return "C Grade"
    elif total >= 30:
        return "D Grade"
    else:
        return "Fail"
print(grad(total))