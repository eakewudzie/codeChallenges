# Given an integer, , perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5 , print Not Weird
# If n is even and in the inclusive range of 6 to 20 , print Weird
# If n is even and greater than 20, print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird. Otherwise, print Not Weird.

# Sample Input 0

# 3
# Sample Output 0

# Weird
# Explanation 0


#  3 is odd and odd numbers are weird, so print Weird.

# Sample Input 1

# 24
# Sample Output 1

# Not Weird
# Explanation 1


# 24 and  is even, so it is not weird.

def check_weird(n):
    if n%2 == 1 or (n%2==0 and 6<=n<=20):
     print("Weird")
    else:
       print("Not weird")

# print("enter a number")
n = int(input("Enter a number: ").strip())

check_weird(n)