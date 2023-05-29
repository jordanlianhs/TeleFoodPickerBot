from typing import Final
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler
import random
import creds

API: Final = creds.api_key
BOT_USERNAME: Final = '@TeleFoodPickerBot'
list_of_cuisine = [
    'Thai Cuisine', 'Vienamese Cuisine', 'Western Cuisine', 'Chinese Cuisine',
    'Indian Cuisine', 'Japanese Cuisine', 'Mexican Cuisine', 'Italian Cuisine',
    'French Cuisine', 'Spanish Cuisine', 'German Cuisine', 'Korean Cuisine',
    'Indonesian Cuisine', 'Malaysian Cuisine', 'Taiwanese Cuisine', 'Hong Kong Cuisine', 'Turkish Cuisine', 'Greek Cuisine',
    'Russian Cuisine','Peruvian Cuisine', 'Argentinian Cuisine', 'African Cuisine'
]
list_of_cuisine_copy = list_of_cuisine.copy()

specific_food = [
    'Burger', 'Pizza', 'Cai Png', 'Fried Chicken', 
    'Fishball Noodles', 'Tacos','Fried Rice', 'Nasi Lemak', 
    'Mee Rebus', 'Nasi Briyani', 'MacDonalds', 'KFC',
    'Subway', 'Pasta', 'Chicken Rice', 'Wanton Mee',
    'Mee Siam', 'Mee Soto', 'Mee Goreng', 'Nasi Goreng',
    'Tze Char', 'Dim Sum', 'Sushi', 'Sashimi',
    'Ramen', 'Pho', 'Bak Kut Teh', 'Satay',
    'Roti Prata', 'Roti Murtabak', 'Meatball Spaghetti', 'Laksa',
    'Bak Chor Mee', 'Fish Soup', 'Ban Mian', 'Kway Chap',
    'Yong Tau Foo', 'Mala', 'Hot Pot', 'Korean BBQ', 'Cheese Pizza'
]
specific_food_copy = specific_food.copy()

selected_options = []
current_option = ''

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello! Thanks for using this bot! You can use {BOT_USERNAME} to talk to me! \n\n Type /help to find out more about me!')

## Create a start cuisine program command  
async def choosecuisine(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[]]
    for food in random.sample(list_of_cuisine, 2):
        keyboard[0].append(InlineKeyboardButton(food, callback_data=food))
        list_of_cuisine.remove(food)
    # Take note this randomise button is on a new row
    keyboard.append([InlineKeyboardButton('Reroll! Idk where to get any of the cuisines', callback_data='Idk Cuisine')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose one of the options below:', reply_markup=reply_markup)

## Create a cuisine button command
async def cuisinebutton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_option, selected_options
    query = update.callback_query
    if len(list_of_cuisine) <2:
        await query.message.reply_text("You have exhausted all the options!")
        if selected_options:
            await query.message.reply_text("This is what you should go and eat today based on your last option: \n\n" + current_option)
            await query.message.reply_text("You have made the following selection at the end of the program: \n\n" + str(selected_options))
        selected_options.clear()
        list_of_cuisine.extend(list_of_cuisine_copy)
        
    else:
        selected_option = query.data
        # If user chooses a cuisine
        if selected_option != 'Idk Cuisine':
            selected_options.append(selected_option)
            current_option = selected_option
            keyboard = [[]]
            keyboard[0].append(InlineKeyboardButton(current_option, callback_data=current_option))

            if len(selected_options) < 6:
                food = random.choice(list_of_cuisine)
                keyboard[0].append(InlineKeyboardButton(food, callback_data=food))
                # Take note this randomise button is on a new row
                keyboard.append([InlineKeyboardButton('Reroll! Idk where to get any of the cuisines', callback_data='Idk Cuisine')])
                list_of_cuisine.remove(food)
                reply_markup = InlineKeyboardMarkup(keyboard)
                if len(selected_options) == 1:
                    await query.message.reply_text('Good choice! \nChoose one of the options below:', reply_markup=reply_markup)
                elif selected_options[-1] == selected_options[-2]:
                    await query.message.reply_text('You have chosen the same cuisine, interesting! \nChoose one of the options below:' , reply_markup=reply_markup)                    
                else:
                    await query.message.reply_text('You have chosen something new! \nChoose one of the options below:', reply_markup=reply_markup)
            else:
                await query.message.reply_text("This is what you should go and eat today: \n\n" + current_option)
                await query.message.reply_text("You have made the following selection at the end of the program: \n\n" + str(selected_options))
                selected_options.clear()
                current_option = ''
                list_of_cuisine.extend(list_of_cuisine_copy)
        
        # If user chooses to reroll
        else:
            keyboard = [[]]
            if len(selected_options) < 6:
                for food in random.sample(list_of_cuisine, 2):
                    keyboard[0].append(InlineKeyboardButton(food, callback_data=food))
                    list_of_cuisine.remove(food)
                # Take note this randomise button is on a new row
                keyboard.append([InlineKeyboardButton('Reroll! Idk where to get any of the cuisines', callback_data='Idk Cuisine')])
                reply_markup = InlineKeyboardMarkup(keyboard)
                await query.message.reply_text('Choose one of the options below:', reply_markup=reply_markup)
            else:
                await query.message.reply_text("This is what you should go and eat today: \n\n" + current_option)
                await query.message.reply_text("You have made the following selection at the end of the program: \n\n" + str(selected_options))
                selected_options.clear()
                current_option = ''
                list_of_cuisine.extend(list_of_cuisine_copy)
            


## Create a start specifc program command  
async def choosefood(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[]]
    for food in random.sample(specific_food, 2):
        keyboard[0].append(InlineKeyboardButton(food, callback_data=food))
        specific_food.remove(food)
    # Take note this randomise button is on a new row
    keyboard.append([InlineKeyboardButton('Reroll! Idk where to get any of the food', callback_data='Idk Food')])
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Choose one of the options below:', reply_markup=reply_markup)

## Create a specific button command
async def foodbutton(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global current_option, selected_options
    query = update.callback_query
    if len(specific_food) <2:
        await query.message.reply_text("You have exhausted all the options!")
        if selected_options:
            await query.message.reply_text("This is what you should go and eat today based on your last option: \n\n" + current_option)
            await query.message.reply_text("You have made the following selection at the end of the program: \n\n" + str(selected_options))
        selected_options.clear()
        specific_food.extend(specific_food_copy)
    
    else:
        selected_option = query.data
        # If user chooses a specific food
        if selected_option != 'Idk Food':
            selected_options.append(selected_option)
            current_option = selected_option
            keyboard = [[]]
            keyboard[0].append(InlineKeyboardButton(current_option, callback_data=current_option))
            
            if len(selected_options) < 10:
                food = random.choice(specific_food)
                keyboard[0].append(InlineKeyboardButton(food, callback_data=food))
                # Take note this randomise button is on a new row
                keyboard.append([InlineKeyboardButton('Reroll! Idk where to get any of the food', callback_data='Idk Food')])
                specific_food.remove(food)
                reply_markup = InlineKeyboardMarkup(keyboard)
                if len(selected_options) == 1:
                    await query.message.reply_text('Good choice! \nChoose one of the options below:', reply_markup=reply_markup)
                elif selected_options[-1] == selected_options[-2]:
                    await query.message.reply_text('You have chosen the same food, interesting! \nChoose one of the options below:' , reply_markup=reply_markup)                    
                else:
                    await query.message.reply_text('You have chosen something new! \nChoose one of the options below:', reply_markup=reply_markup)
            else:
                await query.message.reply_text("This is what you should go and eat today: \n\n" + current_option)
                await query.message.reply_text("You have made the following selection at the end of the program: \n\n" + str(selected_options))
                selected_options.clear()
                current_option = ''
                specific_food.extend(specific_food_copy)
    
        # If user chooses to reroll
        else:
            keyboard = [[]]
            if len(selected_options) < 10:
                for food in random.sample(specific_food, 2):
                    keyboard[0].append(InlineKeyboardButton(food, callback_data=food))
                    specific_food.remove(food)
                # Take note this randomise button is on a new row
                keyboard.append([InlineKeyboardButton('Reroll! Idk where to get any of the food', callback_data='_Idk Food')])
                reply_markup = InlineKeyboardMarkup(keyboard)
                await query.message.reply_text('Choose one of the options below:', reply_markup=reply_markup)

            else:
                await query.message.reply_text("This is what you should go and eat today: \n\n" + current_option)
                await query.message.reply_text("You have made the following selection at the end of the program: \n\n" + str(selected_options))
                selected_options.clear()
                current_option = ''
                specific_food.extend(specific_food_copy)


## Create a help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('''This program helps you to decide what cuisine to eat! 
    \n
Just type /choosecuisine to choose a type of cuisine after 6 rounds of selection! 
    \n 
Just type /choosefood to choose a food after 10 rounds of selection!
''')

# Responses
## Add what ever chatbot responses you want here!
## Or AI responses if you are using an AI chatbot
def handle_response(text: str) -> str:
    processed: str = text.lower()
    
    if 'hello' in processed:
        return 'Hello there!'
    
    if 'how are you' in processed:
        return 'I am fine, thank you!'
    
    return 'Sorry, I do not understand you!'

## Takes care of responsing to whatever user that contacts our bot
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the type of message, group chat or private chat
    message_type: str = update.message.chat.type

    # Get the message text, the one we can process
    text: str = update.message.text

    # Debugging
    print(f'User ({update.message.chat.id}) in {message_type}: {text}')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)
    
    # Debugging
    print(f'Bot: {response}')
    await update.message.reply_text(response)

## Takes care of error
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


# Main
if __name__ == '__main__':
    print('Starting bot...')
    app = Application.builder().token(API).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('choosecuisine', choosecuisine))
    app.add_handler(CallbackQueryHandler(cuisinebutton, pattern='.*Cuisine$'))
    app.add_handler(CommandHandler('choosefood', choosefood))
    app.add_handler(CallbackQueryHandler(foodbutton, pattern='^(?!.*Cuisine$).*'))
    app.add_handler(CommandHandler('help', help_command))

    # Messages
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Errors
    app.add_error_handler(error)
    
    # Polling
    # Checks every 3 seconds for new messages
    print('Polling...')
    app.run_polling(poll_interval=1)
    