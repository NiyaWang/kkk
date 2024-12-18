from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

api = ""
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text="Рассчитать")
button2 = KeyboardButton(text="Информация")
kb.add(button, button2)

kb2 = InlineKeyboardMarkup(resize_keyboard=True)
button3 = InlineKeyboardButton(text="Рассчитать норму калорий", callback_data='calories')
button4 = InlineKeyboardButton(text="Формулы расчёта", callback_data='formulas')
kb2.add(button3)
kb2.add(button4)


@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text = "Рассчитать")
async def main_menu(message):
    await message.answer("Выберите опцию:", reply_markup=kb2)

@dp.callback_query_handler(text ='formulas')
async def get_formulas(call):
    await call.answer( "Формула Миффлина-Сан Жеора:\n"
        "Мужчины: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) + 5\n"
        "Женщины: 10 * вес (кг) + 6.25 * рост (см) - 5 * возраст (лет) - 161")

@dp.callback_query_handler(text ='calories')
async def set_age(call):
    await call.answer('Введите свой возраст:')
    await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer('Введите свой рост:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer('Введите свой вес:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()

    age = int(data['age'])
    growth = int(data['growth'])
    weight = int(data['weight'])
    calories = (10 * weight + (6.25 * growth) - (5 * age) - 161)

    await message.answer(calories)
    await state.finish()

@dp.message_handler()
async def all_message(message):
    await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
