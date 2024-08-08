from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'Привет <b>{message.from_user.first_name}. Рад тебя видеть в чат-боте лейбла Elysium Music!</b> \n'
                                                 f' \n'
                                                 f'Для начала заполни анкету: \n'
                                                 f' \n'
                                                 f'<i>1. Название \n'
                                                 f'2. Исполнитель/Исполнители \n'
                                                 f'3. Жанр \n'
                                                 f'4. Продакшн, если надо указать (prod. by) \n'
                                                 f'5. ФИО исполнителя, который подписывает договор \n'
                                                 f'6. Дата релиза (минимум за 4 дня, чтобы все площадки успели отгрузить, выходные не учитываются) \n'
                                                 f'7. Есть ли мат в треке/запрещённый слова на территории РФ \n'
                                                 f'8. Ссылка на карточку VK (если нет, то прочерк) \n'
                                                 f'9. Ссылка на карточку Spotify (если нет, то прочерк) \n'
                                                 f'10. Ссылка на карточку Apple Music (если нет, то прочерк) \n'
                                                 f'11. Секунды начала для TikTok \n'
                                                 f'12. Сообщение для модератора \n'
                                                 f'13. Текст трека </i> \n', parse_mode="HTML")



async def get_photo(message: Message, bot: Bot):
    await message.answer(f'Отлично! Обложка сохранена. Теперь отправь трек в формате waw')
    file = await bot.get_file(message.photo[-1].file_id)
    await bot.download_file(file.file_path,'photo.jpg')

async def skin_oblogu(message: Message, bot: Bot):
    await message.reply(f'Анкета записана! Теперь отправь мне обложку размером 3000х3000 в формате .jpg')

async def skin_waw(message: Message, bot: Bot):
    await message.reply(f'Отлично! Ваш трек сохранен.\n'
                        f' Теперь нужно заполнить информацию для договора \n'
                        f'\n'
                        f'C вас требуются следующие данные: \n'
                        f'\n'
                        f'1. ФИО \n'
                        f'2. Дата рождения \n'
                        f'3. Место рождения \n'
                        f'4. Серия, номер паспорта \n'
                        f'5. Кем выдан \n'
                        f'6. Дата выдачи \n'
                        f'7. Адрес регистрации \n'
                        f'8. Электронная почта \n'
                        f'\n'
                        f'Далее в течении дня мы вышлем вам на почту документ для подписания, его нужно будет распечать, подписать и отсканировать. После этого релиз отправится на площадки. \n'
                        f'\n'
                        f'Пример договора: \n'
                        f'https://disk.yandex.ru/i/j941Ca31cnjNbw')
    track = await bot.get_file(message.audio[-1].file_id)
    await bot.download_file(track.file_path, 'song.waw')


