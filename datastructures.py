Courses=["Ms Office","HTML & Css","Php","MySQL",".Net","Flutter","Javascript","Mern","c#","Laravel"]
print(Courses)
print(Courses[6])
print(Courses[-3])
print(Courses[-1])
print(Courses[2:6])
print(f"Total courses length is :{len(Courses)}")

Courses.append("Python")
print(f"After append {Courses}")

Courses.append("Hadoop")
print(f"After append {Courses}")

Courses.insert(6 ,"PWD")
print(f"After insert {Courses}")

Courses.insert(9,"Data Analytics")
print(f"After insert {Courses}")

print(f"Total courses length is :{len(Courses)}")

more_courses=["mongoDb","Node.js","Vuels"]
Courses.extend(more_courses)
print(f"After Extend {Courses}")

print(f"Total courses length is :{len(Courses)}")

Courses.remove("HTML & Css")
print(f"After Removing HTML & Css{Courses}")

Courses.pop()
print(f"After pop{Courses}")

print(f"Total courses length is :{len(Courses)}")

Courses.sort() #Ascending
print(f"Ascending Order{Courses}")

Courses.sort(reverse=True) #Descending
print(f"Descending Order{Courses}")

more_courses=["Urdu","IOT","Networking"]
Courses.extend(more_courses)
print(f"After Extend {Courses}")

print(f"Total courses length is :{len(Courses)}")

Courses.clear()
print(f"After  Clearing List : {Courses}")
print(f"Lenght of List : {len(Courses)}")
