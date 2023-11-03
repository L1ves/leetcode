class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        for count in range(n):
            count += 1
        fizz_list = []
        for i in range(1,count +1):
            div3and5 = i % 3 == 0 and i % 5 == 0
            div3 = i % 3 == 0 #Fizz
            div5 = i % 5 == 0 #Fuzz
            if div3and5:
                fizz_list.append("FizzBuzz")
            elif div3:
                fizz_list.append("Fizz")
            elif div5:
                fizz_list.append("Buzz")
            else:
                fizz_list.append(str(i))
        return(fizz_list)