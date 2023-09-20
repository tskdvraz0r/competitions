class Solution:
    def romanToInt(self, s: str) -> int:
        
        DICT_WITH_ROMAN_NUMBERS: dict[str, int] = {
            "CM" : 900,
            "CD" : 400,

            "XC" : 90,
            "XL" : 40,

            "IX" : 9,
            "IV" : 4,

            "M" : 1000,

            "D" : 500,
            "C" : 100,
            "L" : 50,

            "X" : 10,

            "V" : 5,
            "I" : 1
        }

        result: int = 0

        for key, value in DICT_WITH_ROMAN_NUMBERS.items():
            while key in s:
                s = s.replace(str(object = key), "", 1)

                result += value

        return result