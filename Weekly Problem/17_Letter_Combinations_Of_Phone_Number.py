class Solution:
    comment = '''
   Rephrasing: not needed.


    Pseudo-algorithm:

                      d --> out of bounds (add to the array)
                    /
             a - 3 -- e
            /      \
  "" ->   2 -- b     f
            \
             c
    
    At index 0 of the digits string:
    initially we pass empty str ""
    ---> Visit 2 (digit at index 0) and then FOR EACH of its chars (a, b and c):
            FOR a
                add 'a' to the string -> "a". Make next function call with index 1 and "a" as its newComb string
                    ---> Visit 3 (digit at index 1) -> for each of its chars:
                        for d
                            add 'd' to the string -> "ad", again make next function call with index 2
                                ---> index 2 is out of bounds, which means we finished the current path, add "ad" to array

                        for e
                            add 'e' to the string -> "ae", again make next function call with index 2
                                ---> index 2 is out of bounds, which means we finished the current path, add "ae" to array

                        for f
                            add 'f' to the string -> "af", again make next function call with index 2
                                    ---> index 2 is out of bounds, which means we finished the current path, add "af" to array

            FOR b
                add 'b' to the string -> "b". Make next function call with index 1 and "b" as its newComb string
                    ---> Visit 3 (digit at index 1) -> again, FOR EACH of its chars:
                        for d
                            add 'd' to the string -> "bd", again make next function call with index 2
                                ---> index 2 is out of bounds, which means we finished the current path, add "bd" to array

                        for e
                            add 'e' to the string -> "be", again make next function call with index 2
                                ---> index 2 is out of bounds, which means we finished the current path, add "be" to array

                        for f
                            add 'f' to the string -> "bf", again make next function call with index 2
                                    ---> index 2 is out of bounds, which means we finished the current path, add "bf" to array

            FOR c
                add 'b' to the string -> "b". Make next function call with index 1 and "b" as its newComb string
                    ---> Visit 3 (digit at index 1) -> again, FOR EACH of its chars:
                        for d
                            add 'd' to the string -> "cd", again make next function call with index 2
                                ---> index 2 is out of bounds, which means we finished the current path, add "cd" to array

                        for e
                            add 'e' to the string -> "ce", again make next function call with index 2
                                ---> index 2 is out of bounds, which means we finished the current path, add "ce" to array

                        for f
                            add 'f' to the string -> "cf", again make next function call with index 2
                                    ---> index 2 is out of bounds, which means we finished the current path, add "cf" to array



            

    ---> TC = O(4^n) 
    
    ''' 
    numToLetters = {
        '2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z']
    }

    combinations = []
    
    def letterCombinations(self, digits: str) -> List[str]:
        self.combinations = []
        if digits == "":
            return []

        
        self.helper(digits, 0, "")

        return self.combinations

    
    def helper(self, digits, currentDigitIndex, newComb):
        
        if(currentDigitIndex >= len(digits)):
            self.combinations.append(newComb)
            return

        currentDigit = digits[currentDigitIndex]
        for char in self.numToLetters[currentDigit]:
            self.helper(digits, currentDigitIndex+1, newComb + char)



        