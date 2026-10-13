class Solution(object):
    def isPalindrome(self, s):
        temp = "".join(char.lower() for char in s if char.isalnum())

        if temp == temp[::-1]:
            return True
        else:
            return False