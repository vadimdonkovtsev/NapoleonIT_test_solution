class Solution:
    def romanToInt(self, s):
        digit = {"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        self.s = s
        self.length = 0
        self.value = 0
        for string_value in self.s:
            if  string_value not in digit:
                print('Используйте только римские цифры')
                break
        for value in self.s:
            self.length += 1
        for index in range(self.length):
            try:
                if digit[self.s[index]] < digit[self.s[index+1]]:
                    self.value -= digit[self.s[index]]
                else:
                    self.value += digit[self.s[index]]
            except IndexError:
                self.value += digit[self.s[index]]
        if self.value  in range(1,4000) and self.length in range(1,16):
            return self.value
        elif self.value not in range(1,4000) :
            print('Используйте число не больше 3999')
        elif self.length not in range(1,16):
            print('Возьмите число длиной от 1 до 15 включительно')

s = Solution()
print(s.romanToInt('LVIII'))