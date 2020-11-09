'''
https://surik00.gitbooks.io/aiogram-lessons/content/chapter1.html
'''
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from loguru import logger
logger.add("log\\file_{time}.log")


from config import TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

def add_mess_db(mess):
    print('начинаем добавлять мессагу в дата бэйз')
    print(mess)
    logger.debug(mess)
    mess.photo[0].download('test1.jpg')


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):
    print('фото детект: ', message )
    await add_mess_db(message)
    print('----------------------')
    #i=message.photo
    #print(str(i.len()))
    await message.photo[0].download('test.jpg')




@dp.message_handler()
async def echo_message(msg: types.Message):
    print('получено' ,msg.from_user.id, msg.text, msg.chat, msg.from_user, msg.reply_to_message, msg)
    print('msg: ', msg)
    print('----------------------')
    logger.debug(msg)
    #await bot.answer_inline_query()
    await bot.send_message(msg.from_user.id, 'Я возвращаю вам ответ: '+ msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)