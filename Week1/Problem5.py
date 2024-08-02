n=int(input("Enter the number upto which you want the cube : "))

print()

cubes=[]

for i in range(1,n+1) :
    cube = i ** 3
    cubes.append(cube)

print(cubes)
