import re
import json

def parse_food(message):

    days_meals = re.findall(r'(Lunes|Martes|Miércoles|Jueves|Viernes|Sábado|Domingo) (\d+) (.+?)(?=(?:Lunes|Martes|Miércoles|Jueves|Viernes|Sábado|Domingo|$))', message, re.DOTALL)
    
    meal_dict = {}
    for day, day_number, dish in days_meals:
        meal_dict[day_number] = dish.strip()
    
    return json.dumps(meal_dict, ensure_ascii=False)
