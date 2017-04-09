import fraction

A = fraction.Fraction( 1, 2 )
B = fraction.Fraction( 2, 3 )
E = fraction.Fraction( 3, 4 )
C = A.__lt__(B)

D = fraction.Fraction( )

print(A)
print(B)
print(C)
print(D.__repr__())
print(E)