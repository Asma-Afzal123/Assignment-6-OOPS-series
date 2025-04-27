# Class A
class A:
    def show(self):
        print("Show from A")

# Class B inherits from A
class B(A):
    def show(self):
        print("Show from B")

# Class C inherits from A
class C(A):
    def show(self):
        print("Show from C")

# Class D inherits from B and C
class D(B, C):
    pass

# Example usage
d = D()
d.show()

# Print MRO
print(D.mro())
