class Hw1q2: # class defined for the functions

# ----- Methods -----
    def monomial_solver(self):
        print("-----Monomial Solver-----")
        a=int(input("Enter real number for a: "))
        b=int(input('Enter real number for b: '))
        c=int(input('Enter real number for c: ')) # inputs for a b and c
        right_half=c+(2*b)
        answer = right_half / a # performs the calculations to find x
        return answer # returns x

    def polynomial_solver(self):
        print("-----Polynomial Solver-----")
        a = int(input("Enter real number for a: "))
        b = int(input('Enter real number for b: '))
        c = int(input('Enter real number for c: ')) # inputs for a b and c
        right_side = c**2 - (2*b)
        answer = right_side / a # performs the calculations to find x
        return answer # returns x

