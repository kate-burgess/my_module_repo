from my_module import isPalindrome, Chooser, plot

def test_isPalindrome():
    assert isPalindrome(100001) == True
    assert isPalindrome(123) == False


def test_Chooser():
    chooser = Chooser()

    assert chooser.get_value() == 1
    chooser.select()
    assert chooser.get_value() in [1,2,3,4,5,6]

def test_plot():
   plot("sin", 0, 10)
    #couldn't figure out how to check here

     