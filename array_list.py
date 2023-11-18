import numpy as np

class ALIterator:
    def __init__(self, start: int, end: int):
        self.current = start
        self.size = end

    def __next__(self):
        if self.current - 1 is self.size:
            raise StopIteration("No more values.")
        else:
            return_value = self.current
            self.current = self.current + 1
            return return_value
        
    def __iter__(self):
        return self
    
class ArrayList:
    def __init__(self):
        self.the_array = np.empty(16, dtype = object)
        self.size = 0

    def __getitem__(self, index):
        return self.get(index)
    
    def __iter__(self):
        return ALIterator(self.the_array[0], self.size)
    
    def __len__(self):
        return self.get_size()
    
    def __str__(self):
        if self.size == 0:
            return '[]'
        
        r = '['

        for i in range(self.size - 1):
            r += str(self.the_array[i]) + ", "

        return r + str(self.the_array[self.size - 1]) + "]"
    
    def get_size(self):
        return self.size
    
    def is_empty(self):
        return self.size == 0
    
    def get(self, index):
        if index < 0 or index > len(self.the_array):
            raise IndexError("Index is out of bounds.")
        return self.the_array[index]

    def set(self, index, new_value):
        pass

    #do not use this method outside of class
    def expand_array(self):
        #create an array twice as big; geometric expansion
        temp_array = np.empty(len(self.the_array) * 2, dtype = object)

        #copy the values from the old array to the new array
        for i in range(self.size):
            temp_array[i] = self.the_array[i]

        #change self.the_array to point to the new array
        self.the_array = temp_array

    def insert(self, index, value):
        if index < 0 or index > self.size:
            raise IndexError("Index is out of bounds.")
        
        if self.size == len(self.the_array):
            self.expand_array()
        
        for i in range(self.size - 1, index - 1, -1):
            self.the_array[i + 1] = self.the_array[i]

        self.the_array[index] = value
        self.size += 1

    def append(self, value):
        self.insert(self.size, value)

# def test_driver() -> int:
#     """
#         Description of Function:
#             creates an ArrayList object and appends the integers from 1 to 100
#             and iterates through the array using a content-based for-loop 
#             returning the sum of the integers 
#         Parameters:
#             None
#         Return:
#             int
#     """
#     #assigning variables
#     sum = 0
#     arr = ArrayList()

#     #appending integers 1-100 to ArrayList object
#     for i in range(1, 101):
#         arr.append(i)

#     #iterating through ArrayList using a content-based for-loop
#     for value in arr:
#         sum += value

#     return sum

# print(test_driver())

print(f"n\t\telapsed_time\t\truntime")
num_trial = 2
for n in (100000, 200000, 400000, 800000):
    start = time()
    for j in range(num_trial):
        some_list = ArrayListArithmetic()
        for i in range(n):
            some_list.append(n)
    stop = time()
    print(f"{n}\t\t{stop - start}\t\t{(stop - start)/num_trial}")

class ArrayListArithmetic(ArrayList):
    def __init__(self):
        ArrayList.__init__(self)
        self.size = 0

    def expand_array(self):
        #create an array twice as big; geometric expansion
        temp_array = np.empty(len(self.the_array) + 1000, dtype = object)

        #copy the values from the old array to the new array
        for i in range(self.size):
            temp_array[i] = self.the_array[i]

        #change self.the_array to point to the new array
        self.the_array = temp_array