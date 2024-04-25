import utils.foodParser as foodParser
import database.firebaseFuncs as firebaseFuncs
import apiRequest.api_request as api_request
import json
import re

async def update_meal_handler(update, context): 
    foodMenu=foodParser.parse_food(" ".join(context.args))
    foodDict = json.loads(foodMenu)
    firebaseFuncs.setMealDoc(foodDict)
    await update.message.reply_text("Menu actualizado")

async def generate_meals(update, context):
    print("Generating meals")
    meal_Docs = firebaseFuncs.getAllMealDocs()
    
    unique_values = set(value.lower() for menu_dict in meal_Docs for value in menu_dict.values())
    unique_values_str = '\n'.join(unique_values)
    
    ans=api_request.generateMenu(unique_values_str)
    pattern = r'\{[^{}]*\}'

    matches = re.findall(pattern, ans)
    firebaseFuncs.setMealDoc(json.loads(matches[0]))
    await update.message.reply_text("el nuevo menu seria: "+matches[0])
