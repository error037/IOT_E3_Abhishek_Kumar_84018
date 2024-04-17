sub = int(input("math marks :"))
sub2 = int(input("english marks :"))
sub3 = int(input("python marks :"))

avg_marks = (sub+sub2+sub3)/3
print("average marks:", format(avg_marks,'.2f'))

if avg_marks >= 90:
    print("grade A")
elif avg_marks >=80:
    print("grade B")
elif avg_marks >= 70:
    print("grade C")
elif avg_marks >=60:
    print("grade D")
else:
    print("grade F")