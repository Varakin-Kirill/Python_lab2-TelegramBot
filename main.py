import aiogram
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
TOKEN_API="5916951628:AAHrbOIyqC9rpM8MarqmRvviAjxVQbFeeHY"
from aiogram.dispatcher.filters import Text
bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
HELP_COMMAND="""
<b>/help</b> -<em>список команд</em> 
<b>/game</b> - <em>начать игру</em>
<b>/start</b> -<em>запуск бота</em>"""
RULES="""
Было загадано число от 0 до 100. 
Вам необходимо угадать данное число🧠.
После каждой попытки вам будет выдаваться
ответ  «больше», «меньше» или «угадал»,
в зависимости от того, является задуманное
им число большим, меньшим или равным предложенному."""
start_buttons=["help","game"]
kb=ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(*start_buttons)
from random import randint
Check=False
@dp.message_handler(commands=['start'])
async def command_start(message: types.message):
    await message.answer( text='Добро пожаловать!', reply_markup=kb)

@dp.message_handler(Text(equals="game"))
async def game_command(message: types.Message):
    global number
    number = randint(0, 100)
    global Check
    Check=True
    await message.answer( text=RULES)
    await message.delete()
@dp.message_handler(Text(equals="help"))
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND, parse_mode='HTML')
    await message.delete()
@dp.message_handler()
async def game_mechanics(message: types.Message):
    global Check
    if Check==True:
        if message.text.isdigit() == True and number > int(message.text):
            await message.answer('загаданное число больше')
        if message.text.isdigit() == True and number < int(message.text):
            await message.answer('загаданное число меньше')
        if message.text.isdigit() == True and number == int(message.text):
            await message.answer('угадал 🎉🎉🎉!!!')
            Check = False
        if message.text.isdigit() == False:
            await message.answer('напишите число')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

