import logging
from aiogram import Bot, Dispatcher, executor, types
from config import TOKEN
from translit_func import translit_func

logging.basicConfig(level=logging.INFO,filename="logs.log") 

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start']) 
async def send_welcome(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = f'Привет, {user_name}! Какой текст вы хотите транслитерировать?'
    logging.info(f'{user_name=} {user_id=} sent message: {message.text}')
    await message.reply(text)

@dp.message_handler() 
async def send_translit(message: types.Message):
    user_name = message.from_user.full_name
    user_id = message.from_user.id
    text = translit_func(message.text)

    logging.info(f'{user_name=} {user_id=} sent message: {text}')
    await bot.send_message(user_id, text)

if __name__ == '__main__':
    executor.start_polling(dp)
    

    
