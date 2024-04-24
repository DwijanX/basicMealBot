import utils.foodParser as foodParser
import database.firebaseFuncs as firebaseFuncs
import json

async def update_meal_handler(update, context): 
    foodMenu=foodParser.parse_food(" ".join(context.args))
    foodDict = json.loads(foodMenu)
    firebaseFuncs.setMealDoc(foodDict)

