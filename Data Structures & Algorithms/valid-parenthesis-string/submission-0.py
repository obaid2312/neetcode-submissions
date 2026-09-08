class Solution:
    def checkValidString(self, s: str) -> bool:

        min_o = 0
        max_o = 0

        for char in s:

            if char == '(':

                min_o += 1
                max_o += 1

            elif char == ')':

                min_o -= 1
                max_o -= 1

            else:

                min_o -= 1
                max_o += 1

            if max_o < 0:
                return False

            if min_o < 0:
                min_o = 0

        return min_o == 0
        