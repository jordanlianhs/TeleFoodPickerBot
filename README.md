# TelegramFoodPickerBot

- [TelegramFoodPickerBot](#telegramfoodpickerbot)
  - [What are the commands available to the bot?](#what-are-the-commands-available-to-the-bot)
  - [What can the bot do?](#what-can-the-bot-do)
    - [Help](#help)
    - [Choose Cuisine](#choose-cuisine)
    - [Choose Food](#choose-food)
  - [What if there is a bug?](#what-if-there-is-a-bug)

## What are the commands available to the bot?

![Screenshot](https://github.com/jordanlianhs/TelegramFoodPickerBot/blob/main/pic/menu.png) </br>
Above shows the available commands available to the bot.

- start - Starts the bot

- choosecuisine - Starts the cuisine picker

- choosefood - Starts the food picker

- help - Provides the help for using the bot

## What can the bot do?

### Help

![Screenshot](https://github.com/jordanlianhs/TelegramFoodPickerBot/blob/main/pic/help.png) </br>

- Here you can see the available commands and what they do and also tap/click on the commands to prompt the bot to execute them </br>

### Choose Cuisine

![Screenshot](https://github.com/jordanlianhs/TelegramFoodPickerBot/blob/main/pic/choosecuisine.png) </br>

- Here you will be prompted to choose 6 different cuisine with the bot remembering your last option, before arriving at a final option
- If you press on reroll, it will not count towards the 6 different cuisines as you are unsure of the availability of both cuisines in your vicinity
- Thus this assumes that if you press on one option and it is carried over to the next option, if you press reroll, it will clear your previous option
  - This is assuming that you decided on one option and are unsure of the other, you should not press reroll but instead, the previous option that you were certain
  - For example:
    - I am first presented with ```Chinese Cuisine``` and ```African Cuisine```
    - I pick ```Chinese Cuisine```
    - Next I am presented with ```Chinese Cuisine``` *(Since it was my last option)* and ```Italian Cuisine```
    - If I am uncertain of where to get ```Italian Cuisine```, I would not recommend you press ```Reroll```, as your option for ```Chinese Cuisine``` will be deleted
    - Instead, continue with ```Chinese Cuisine```

### Choose Food

![Screenshot](https://github.com/jordanlianhs/TelegramFoodPickerBot/blob/main/pic/choosefood.png) </br>

- Here you will be prompted to choose 10 different fiids with the bot remembering your last option, before arriving at a final option
- If you press on reroll, it will not count towards the 6 different foods as you are unsure of the availability of both cuisines in your vicinity
- Thus this assumes that if you press on one option and it is carried over to the next option, if you press reroll, it will clear your previous option

## What if there is a bug?

Please pm me on telegram [@jordanlian](https://t.me/jordanlian) if you do find one!
