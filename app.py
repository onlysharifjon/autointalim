import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup

from keyboards.default.startkey import startbut, startbutl, xodimlar

shablon = []
API_TOKEN = '5753926515:AAEusqR4Ufw_xdRSh8bjKmqakugjB3oj3nY'

logging.basicConfig(level = logging.INFO)
d = []


class NameStates(StatesGroup):
    name_step = State()
    familiya = State()
    Sharif = State()
    shir = State()
    seriya_num = State()
    seruya_number =State()
    name_avto = State()
    tel_num = State()
    uquv = State()
    result = State()
    region = State()



bot = Bot(token = API_TOKEN, parse_mode = 'HTML')
dp = Dispatcher(bot, storage = MemoryStorage())



@dp.message_handler(commands = ['start'])
async def send_welcome(message: types.Message):
    await message.answer(
        f"<b>👋Assalomu Aleykum</b>\n\n<b>👤Hurmatli:</b> {message.from_user.first_name}\n\n<b>🤝Shartnoma tuzishni xohlaysizmi</b>",
        reply_markup = startbut)



@dp.message_handler(text = "YOQ ❌")
async def yok(message: types.Message):
    await message.answer("Xayr Salomat bo`ling👋")

@dp.message_handler(text = "HA ✅")
async def tr(message: types.Message, state: FSMContext):
    await message.answer("<b>👥Ismingizni kiriting !</b>",reply_markup = xodimlar)
    await NameStates.name_step.set()


@dp.message_handler(state = NameStates.name_step, content_types = types.ContentTypes.TEXT)
async def ups(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup = xodimlar)
        await NameStates.name_step.set()
    else:
        names = message.text
        d.append(names)
        await message.answer("👥Familyangizni kiriting !")
        await state.finish()
        await NameStates.familiya.set()


@dp.message_handler(state = NameStates.familiya, content_types = types.ContentTypes.TEXT)
async def ups_och(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup = xodimlar)
        await NameStates.name_step.set()
    else:
        familiyas = message.text
        d.append(familiyas)
        await message.answer("<b>👥Sharifjingizni kiriting !</b>")
        await state.finish()
        await NameStates.Sharif.set()


@dp.message_handler(state = NameStates.Sharif, content_types = types.ContentTypes.TEXT)
async def ups_Sharifsw(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup = xodimlar)
        await NameStates.name_step.set()
    else:
        sharif_user = message.text
        d.append(sharif_user)
        await message.answer("📄Pasport <b>JSHSHIR</b> raqamini  kiriting")
        await state.finish()
        await NameStates.shir.set()


@dp.message_handler(state = NameStates.shir, content_types = types.ContentTypes.TEXT)
async def ups_dirssk(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>👥Ismingizni kiriting !</b>", reply_markup = xodimlar)
        await NameStates.name_step.set()
    else:
        shirs = message.text
        if len(shirs) == 14:
                await message.answer("Pasport Seriyasini  kiriting\n\nNAMUA: AC")
                d.append(shirs)
                await state.finish()
                await NameStates.seriya_num.set()

        else:
            await message.answer("PASPORT MA`LUMOTLARIDA XATOLIK \nJSHSHIR RAQAMINI QAYTA KIRITING !")
@dp.message_handler(state = NameStates.seriya_num, content_types = types.ContentTypes.TEXT)
async def ups_se(message: types.Message, state: FSMContext):
    ser = message.text
    if type(ser) == type("a"):
        if len(ser) == 2:
            d.append(ser)
            await message.answer("🔡Pasport seriya raqamini kiriting !\n(7 ta)")
            await state.finish()
            await NameStates.seruya_number.set()
    else:
        await message.answer("PASPORT SERIYASI XATO KIRITILDI !\nQATADAN KIRITING !")
@dp.message_handler(state = NameStates.seruya_number, content_types = types.ContentTypes.TEXT)
async def upsawdaed(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>Ismingizni kiriting !</b>", reply_markup = xodimlar)
        await NameStates.name_step.set()
    else:
        number = message.text
        if len(number) == 7:

            d.append(number)
            await message.answer("<b>🚘AVTOMAKTAB🚘</b>nomini kiriting")
            await state.finish()
            await NameStates.name_avto.set()
        else:
            await message.answer("Pasport Seriya raqami xato kiritildi !\nqaytadan kiriting !")
@dp.message_handler(state = NameStates.name_avto, content_types = types.ContentTypes.TEXT)
async def upsfhfht(message: types.Message, state: FSMContext):
    if message.text == "Orqaga🔙":
        await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
        await message.answer("<b>Ismingizni kiriting !</b>", reply_markup = startbut)
        await NameStates.name_step.set()
    else:
        avtomaktab = message.text
        d.append(avtomaktab)
        await message.answer("📞Telefon raqamingizni kiriting !")
        await state.finish()
        await NameStates.result.set()
@dp.message_handler(state = NameStates.result, content_types = types.ContentTypes.TEXT)
async def upws(message: types.Message, state: FSMContext):
    tel = message.text
    d.append(tel)
    await message.answer("<b>📝Nechita o`quvchiga shartnoma tuzmoqchisiz </b>")

    await state.finish()
    await NameStates.uquv.set()


@dp.message_handler(state = NameStates.uquv, content_types = types.ContentTypes.TEXT)
async def qups(message: types.Message, state: FSMContext):
    uquvchi_son = message.text
    d.append(uquvchi_son)
    await message.answer("📍Avtomaktab joylashgan Viloyat yoki Shaharni kiriting\n\n<b>🪪Masalan: Toshkent shahar</b>")
    await state.finish()
    await NameStates.region.set()


@dp.message_handler(state = NameStates.region, content_types = types.ContentTypes.TEXT)
async def qups(message: types.Message, state: FSMContext):
    reg = message.text
    d.append(reg)
    await message.answer("🔍Ma`lumotlar to`g`ri ekanligiga aminmisiz", reply_markup = startbutl)
    await state.finish()


@dp.message_handler(text = "HA📄")
async def y(message: types.Message):
    await message.answer(f"""<b>
🚘AVTOMAKTAB-{d[6]}
🔡P_SERIYA-{d[4]}
🔢P_RAQAM-{d[5]}
#️⃣P_JSSHIR-{d[3]}
🇺🇿Direktor FISH-{d[0]}-{d[1]}-{d[2]}
☎️tel = {d[7]}
📝Shartnoma soni-{d[8]}
📍Manzil-{d[9]}</b>
""")
    await bot.send_message(2111796525,"Yangi Ariza !")
    await bot.send_message(2111796525,f"""<b>
🚘AVTOMAKTAB-{d[6]}
🔡P_SERIYA-{d[4]}
🔢P_RAQAM-{d[5]}
#️⃣P_JSSHIR-{d[3]}
🇺🇿Direktor FISH-{d[0]}-{d[1]}-{d[2]}
☎️tel = {d[7]}
📝Shartnoma soni-{d[8]}
📍Manzil-Toshkent Shahar</b>
""")
    d.clear()
    await message.answer(f"Hurmatli <b>{message.from_user.full_name}</b> bizning kompaniya xizmatlaridan foydalanganingizdan mamnunmiz")
    await message.answer("Arizada xatoliklar bo`lsa qayta ariza topshirishingiz mumkin !\n",reply_markup = xodimlar)
@dp.message_handler(text = "YOQ✖️")
async def y(message: types.Message):
    await message.answer("Mal`lumotlarni qayta kiritishingiz mumkin")
    await message.answer("<b>Ismingizni kiriting !</b>", reply_markup = xodimlar)
    await NameStates.name_step.set()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)





