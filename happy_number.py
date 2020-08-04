class Solution():
    def isHappy(self, n):
        set_of_number = set()
        while True:
            set_of_number.add(n)
            sum_of_number = sum(int(loop) ** 2 for loop in str(n))
            n = sum_of_number
            if sum_of_number == 1:
                return True
            if n in set_of_number: 
                return False