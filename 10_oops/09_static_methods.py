class ChaiUtils: 
    @staticmethod
    def clean_ingredients(text): 
        return [item.strip() for item in text.split(",")]

raw = " water, milk , ginger, honey , apple  "

# obj = ChaiUtils() 
# obj.clean_ingredients(raw)   #This is basic way to use method 


cleaned = ChaiUtils.clean_ingredients(raw)   #static method do not required object creation. 
print(cleaned)