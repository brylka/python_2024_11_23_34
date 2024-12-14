class ListProc:
    @staticmethod
    def find_min(nums):
        return min(nums)
    @staticmethod
    def find_max(nums):
        return max(nums)
    @staticmethod
    def find_min_and_max(nums):
        return min(nums), max(nums)
    @staticmethod
    def sum_list(nums):
        return sum(nums)


numbers = [1,2,3,4,23,45,-4,24,76,-45,-12]
print(f"Najmniejsza wartość: {ListProc.find_min(numbers)}")
print(f"Największa wartość: {ListProc.find_max(numbers)}")
minimum, maxsimum = ListProc.find_min_and_max(numbers)
print(f"Najmniejsza wartość: {minimum}, największa: {maxsimum}")
print(f"Zwrot dwóch wartości: {ListProc.find_min_and_max(numbers)}")
print(f"Suma elementów: {ListProc.sum_list(numbers)}")

