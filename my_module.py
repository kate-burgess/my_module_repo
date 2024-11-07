import matplotlib.pyplot as plt
import math
import random


#A function that generates a plot, given a function name and the range of x values
def plot(functionName, x_range_start, x_range_end):

    function = getattr(math, functionName) #turns the functionName and gets the actual math function
    x_values = []
    for x in range(x_range_start,x_range_end):
        x_values.append(x)

    y_values = []
    for x in x_values:
        y_values.append(function(x))

    plt.plot(x_values, y_values)
    plt.show()


 #The Chooser class from the OOP lecture
class Chooser:
    def __init__(self, user_list=None):
        if user_list == None:
             self.list = [1,2,3,4,5,6]
        else:
            self.list = user_list 
        self.currentVal = self.list[0]


    def get_value(self):
        return self.currentVal
 
    def select(self):
        self.currentVal = self.list[random.randint(0, len(self.list)-1)]


#Your solution to either a Project Euclid or Leetcode problem
def isPalindrome(x):
        original = str(x)
        reverse = ""
        index = len(original) - 1
        while(index >= 0):
            reverse = reverse + original[index]
            index = index - 1

        return original == reverse

if __name__ == "__main__":
    #tests for code
    print("100001 is a palindrome number: " + str(isPalindrome(100001)))

    chooser = Chooser([1,2,3,4,5,6,7,8,9,10])
    chooser.select()
    print("Random die roll with 10 sides: " + str(chooser.get_value()))
    plot("sqrt", 0, 10)