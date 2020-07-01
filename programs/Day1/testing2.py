from itertools import accumulate, count

tgt=int(input("Please enter the volume of a tetrahedron: "))

triangles=accumulate(count(1))
tetrahedrals=accumulate(triangles)
print(next(n for n, t in enumerate(tetrahedrals, 1) if t>=tgt), "balls")