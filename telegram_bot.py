from aiogram import Bot, types, executor
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

import os

storage = MemoryStorage()

bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=storage)

async def on_startup(_):
	print('Бот вышел в онлайн')

class FSMAdmin(StatesGroup):
	ptp = State()
	ptm = State()
	ptsm = State()

class FSMAdmin2(StatesGroup):
	zpa = State()
	zpb = State()
	k = State()
	f = State()
	a = State()
	o = State()
	t = State()
	s = State()
	r = State()
	so = State()
	sa = State()
	si = State()
	sr = State()
	sp = State()
	sh = State()
	ss = State()

class FSMAdmin3(StatesGroup):
	ftp = State()
	ftm = State()
	ftsm = State()

class FSMAdmin4(StatesGroup):
	fp = State()
	fm = State()
	fbs = State()
	fd = State()
	fb = State()
	fps = State()
	k = State()
	f = State()
	a = State()
	o = State()
	t = State()
	s = State()
	r = State()
	so = State()
	sa = State()
	si = State()
	sr = State()
	sp = State()
	sh = State()
	ss = State()

class FSMAdmin5(StatesGroup):
	pc = State()

class FSMAdmin6(StatesGroup):
	pc = State()

class FSMAdmin7(StatesGroup):
	pc = State()

class FSMAdmin8(StatesGroup):
	pc = State()

class FSMAdmin9(StatesGroup):
	pvz = State()
	pck = State()
	nk = State()

class FSMAdmin10(StatesGroup):
	pvz = State()
	pck = State()
	nk = State()

class FSMAdmin11(StatesGroup):
	pck = State()
	nk = State()




lf = InlineKeyboardMarkup(text='Личные финансы', callback_data='qqq')
cob = InlineKeyboardMarkup(text='Семейный общий бюджет', callback_data='www')
vio = InlineKeyboardMarkup(text='Вклады и облигации', callback_data='eee')
kii = InlineKeyboardMarkup(text='Кредиты и ипотека', callback_data='rrr')
biz = InlineKeyboardMarkup(text='Бизнес', callback_data='ttt')

b1 = InlineKeyboardMarkup(text='Обычные вклады', callback_data='yyy')
b2 = InlineKeyboardMarkup(text='Квартальную капитализацию', callback_data='uuu')
b3 = InlineKeyboardMarkup(text='Ежемесячную капитализацию', callback_data='iii')
b4 = InlineKeyboardMarkup(text='Использовать государственные облигации', callback_data='ooo')
b5 = InlineKeyboardMarkup(text='Посмотреть сравнительный анализ инструментов', callback_data='ppp')
b0 = InlineKeyboardMarkup(text='(Если ничего не надо)', callback_data='aaa')

b11 = InlineKeyboardMarkup(text='Аннуитетный кредит в банке', callback_data='sss')
b22 = InlineKeyboardMarkup(text='Дифференцированный кредит в банке', callback_data='ddd')
b33 = InlineKeyboardMarkup(text='Кредит в мелкокредитной организации', callback_data='fff')


inkb3 = InlineKeyboardMarkup(row_wight=1).add(b11).add(b22).add(b33)
inkb2 = InlineKeyboardMarkup(row_wight=1).add(b1).add(b2).add(b3).add(b4).add(b5).add(b0)
inkb = InlineKeyboardMarkup(row_wight=1).add(lf).add(cob).add(vio).add(kii).add(biz)

pcokrash = KeyboardButton('/Сокращенный')
ppolniy = KeyboardButton('/Полный')

fcokrash = KeyboardButton('/Сокрaщенный')
fpolniy = KeyboardButton('/Пoлный')

lich = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
lich.add(pcokrash).add(ppolniy)

family = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
family.add(fcokrash).add(fpolniy)


@dp.message_handler(commands=['start', 'help'])
async def commands_start(message : types.Message):
	try:
		await bot.send_message(message.from_user.id, 'Здравствуйте! Я бот "Финансовая грамотность". Меня разрабатывают, чтобы я помог Вам разобраться в финансах. Выберете интересующую Вас тему')
		await message.answer('Темы', reply_markup=inkb)
		await message.delete()
	except:
		await message.reply('Общение с ботом через ЛС, напишите ему: \nhttps://t.me/FinancialGram_bot')

'''************************************ЛИЧНЫЕ ФИНАНСЫ***************************************'''
@dp.callback_query_handler(text='qqq')
async def qqq_call(callback : types.CallbackQuery):
	await callback.message.answer('Выберите вариант. Полный анализ или сокращенный', reply_markup=lich)

'''************************************СОКРАЩЕННЫЙ ВАРИАНТ**********************************'''
@dp.message_handler(commands=['Сокращенный'], state=None)
async def pcokrash1_command(message : types.Message):
	await FSMAdmin.ptp.set()
	await message.answer('Введите среднюю зарплату за месяц')

@dp.message_handler(state=FSMAdmin.ptp)
async def pcokrash2_command(message : types.Message, state : FSMContext):
	global ptp
	ptp = int(message.text)
	await FSMAdmin.next()
	await message.answer('Введите средние обязательные траты(продукты питания, транспорт, кварт плата и тд)')

@dp.message_handler(state=FSMAdmin.ptm)
async def pcokrash3_command(message : types.Message, state : FSMContext):
	global ptm
	ptm = int(message.text)
	await FSMAdmin.next()
	await message.answer('Введите средние сезонные расходы в месяц(налоги на имущесто, одежда, аптека по болезни)')

@dp.message_handler(state=FSMAdmin.ptsm)
async def pcokrash4_command(message : types.Message, state : FSMContext):
	global ptsm
	ptsm= int(message.text)
	await FSMAdmin.next()
	ptt = ptp-(ptm+ptsm)
	if ptt > 0:
		await message.answer('Все хорошо')
	if ptt <= 0:
		await message.answer('Нужно проанализировать Ваши расходы')
	await state.finish()

'''************************************ПОЛНЫЙ АНАЛИЗ*******************************************'''
@dp.message_handler(commands=['Полный'], state=None)
async def ppolniy1_command(message : types.Message):
	await FSMAdmin2.zpa.set()
	await message.answer('Введите зарплату с основного места работы за этот месяц')

@dp.message_handler(state=FSMAdmin2.zpa)
async def ppolniy2_command(message : types.Message, state : FSMContext):
	global zpa
	zpa = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Введите дополнительные заработки из других мест')

@dp.message_handler(state=FSMAdmin2.zpb)
async def ppolniy3_command(message : types.Message, state : FSMContext):
	global zpb
	global ptp
	zpb = int(message.text)
	ptp = zpa+zpb #Общий возможный заработок
	await FSMAdmin2.next()
	await message.answer('Введите ежемесячные обязательные расходы')
	await message.answer('Комунальные платежи или общие траты на съемное жилье')

@dp.message_handler(state=FSMAdmin2.k)
async def ppolniy4_command(message : types.Message, state : FSMContext):
	global k
	k = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Продукты питания')

@dp.message_handler(state=FSMAdmin2.f)
async def ppolniy5_command(message : types.Message, state : FSMContext):
	global f
	f = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Ежемесячные аптечные препараты')

@dp.message_handler(state=FSMAdmin2.a)
async def ppolniy6_command(message : types.Message, state : FSMContext):
	global a
	a = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Ежемесячная одежда')

@dp.message_handler(state=FSMAdmin2.o)
async def ppolniy7_command(message : types.Message, state : FSMContext):
	global o
	o = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Транспортные расходы')

@dp.message_handler(state=FSMAdmin2.t)
async def ppolniy8_command(message : types.Message, state : FSMContext):
	global t
	t = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Секции, кружки, репетиторы и тд')

@dp.message_handler(state=FSMAdmin2.s)
async def ppolniy9_command(message : types.Message, state : FSMContext):
	global s
	s = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Развлечения, кино, рестораны')

@dp.message_handler(state=FSMAdmin2.r)
async def ppolniy10_command(message : types.Message, state : FSMContext):
	global r
	global ptm
	r = int(message.text)
	ptm = f+o+a+k+r+s+t
	await FSMAdmin2.next()
	await message.answer('Введите сезонные общие расходы')
	await message.answer('Сезонная одежда')

@dp.message_handler(state=FSMAdmin2.so)
async def ppolniy11_command(message : types.Message, state : FSMContext):
	global so
	so = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Сезонная аптека')

@dp.message_handler(state=FSMAdmin2.sa)
async def ppolniy12_command(message : types.Message, state : FSMContext):
	global sa
	sa = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Спортивный инвентарь')

@dp.message_handler(state=FSMAdmin2.si)
async def ppolniy13_command(message : types.Message, state : FSMContext):
	global si
	si = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Непредвиденные расходы на ремонт техники')

@dp.message_handler(state=FSMAdmin2.sr)
async def ppolniy14_command(message : types.Message, state : FSMContext):
	global sr
	sr = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Годовые затраты на отпуск')

@dp.message_handler(state=FSMAdmin2.sp)
async def ppolniy15_command(message : types.Message, state : FSMContext):
	global sp
	sp = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Налог на имущество')

@dp.message_handler(state=FSMAdmin2.sh)
async def ppolniy16_command(message : types.Message, state : FSMContext):
	global sh
	sh = int(message.text)
	await FSMAdmin2.next()
	await message.answer('Все сборы и налог на автомобиль')

@dp.message_handler(state=FSMAdmin2.ss)
async def ppolniy17_command(message : types.Message, state : FSMContext):
	global ss
	global ptsm
	global ttg
	global ptt
	ss = int(message.text)
	ptsm = (so+sa+si+sr+sp+sh+ss)/12
	ptt = int(ptp-(ptm+ptsm)) #Денежные средства на балансе
	ttg = int(ptt*12)
	if ttg > 0:
		await message.answer('Все хорошо')
		await message.answer('Если Вы хотите класть деньги на', reply_markup=inkb2)

		@dp.callback_query_handler(text='yyy') #1
		async def yyy_call(callback : types.CallbackQuery):
			await callback.message.answer('Обычные вклады')	
			await callback.message.answer('Введите процент')	
			await FSMAdmin5.pc.set()

		@dp.message_handler(state=FSMAdmin5.pc)
		async def procent1_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg2
			global ttg
			pc = int(message.text)
			pc=(pc*0.01)
			ttg1= int(ttg*(1+pc))
			ttg2 = int(ttg1-ttg)
			await message.answer(f"Вы заработали без вклада {ttg}, Вы + вклад {ttg1}, Вы получили прибыль от вклада {ttg2}")
			await state.finish()


		@dp.callback_query_handler(text='uuu') #2
		async def uuu_call(callback : types.CallbackQuery):
			await callback.message.answer('Квартальная капитализация')
			await callback.message.answer('Введите процент')
			await FSMAdmin6.pc.set()

		@dp.message_handler(state=FSMAdmin6.pc)
		async def procent2_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg2
			global ttg
			pc = int(message.text)
			pc=(pc*0.01)/4
			ttg1= int(ttg)
			for i1 in range(4):
				ttg1=int(ttg1*pc+ttg1)
			ttg2 = int(ttg1-ttg)
			await message.answer(f"Вы заработали без вклада {ttg}, Вы + вклад {ttg1}, Вы получили прибыль от вклада {ttg2}")
			await state.finish()


		@dp.callback_query_handler(text='iii') #3
		async def iii_call(callback : types.CallbackQuery):
			await callback.message.answer('Ежемесячная капитализация')	
			await callback.message.answer('Введите процент')	
			await FSMAdmin7.pc.set()

		@dp.message_handler(state=FSMAdmin7.pc)
		async def procent3_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg2
			global ttg
			pc = int(message.text)
			pc=(pc*0.01)/12
			ttg1= int(ttg)
			for i2 in range(12):
				ttg1=int(ttg1*pc+ttg1)
			ttg2 = int(ttg1-ttg)
			await message.answer(f"Вы заработали без вклада {ttg}, Вы + вклад {ttg1}, Вы получили прибыль от вклада {ttg2}")
			await state.finish()


		@dp.callback_query_handler(text='ooo') #4
		async def ooo_call(callback : types.CallbackQuery):
			await callback.message.answer('Государственные облигации')	
			await callback.message.answer('Введите процент')	
			await FSMAdmin8.pc.set()

		@dp.message_handler(state=FSMAdmin8.pc)
		async def procent4_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg
			pc = int(message.text)
			pc=pc*0.01
			if ttg>400000:
				ttg1=int(ttg*(pc*0.01+1)+52000)
				await message.answer(f"Вы заработали вместе с облигациями {ttg1}. Процент по облигациям позволил заработать {ttg1-(52000+ttg)}. Так же был взят налоговый вычет суммой 52000") 
			else:
				ttg1=int(ttg*(pc*0.01+1)+(ttg*0.13))
				await message.answer(f"Вы заработали вместе с облигациями {ttg1}. Процент по облигациям позволил заработать {ttg1-ttg}. Так же был взят налоговый вычет суммой {ttg*0.13}")
			await state.finish()


		@dp.callback_query_handler(text='aaa') #0
		async def aaa_call(callback : types.CallbackQuery):
			await callback.message.answer(f"Вы заработали за год {ttg}")

	if ttg <= 0:
		await message.answer('Кредитная история')
		await message.answer('Выберите', reply_markup=inkb3)

		@dp.callback_query_handler(text='sss') #1
		async def sss_call(callback : types.CallbackQuery):
			await callback.message.answer('Аннуитетный кредит')	
			await callback.message.answer('Введите сумму первоначального взноса')	
			await FSMAdmin9.pvz.set()

		@dp.message_handler(state=FSMAdmin9.pvz)
		async def anuitet1_command(message : types.Message, state : FSMContext):
			global pvz
			global ttg5
			pvz = int(message.text)
			ttg5 = int(-ttg-pvz)
			await FSMAdmin9.next()
			await message.answer('Процентная ставка по кредиту')

		@dp.message_handler(state=FSMAdmin9.pck)
		async def anuitet2_command(message : types.Message, state : FSMContext):
			global pck
			pck = int(message.text)
			pck = (pck*0.01)/12
			await FSMAdmin9.next()
			await message.answer('Введите колличество месяцев на которые берется кредит')

		@dp.message_handler(state=FSMAdmin9.nk)
		async def anuitet3_command(message : types.Message, state : FSMContext):
			global nk
			global spk
			global ttgk
			global pck
			nk = int(message.text)
			spk = int(ttg5*(pck*(1+pck)**nk)/((1+pck)**nk-1)) #Формула ежемесячных платежей
			ttgk = int(spk*nk) #Общая сумма кредита
			await message.answer(f"общая сумма кредита {ttgk}. Ежемесячные платежи = {spk}. Переплаты по кредиту {ttgk-ttg5}")
			await state.finish()


		@dp.callback_query_handler(text='ddd') #2
		async def ddd_call(callback : types.CallbackQuery):
			await callback.message.answer('Дифференцированный кредит')	
			await callback.message.answer('Введите сумму первоначального взноса')	
			await FSMAdmin10.pvz.set()

		@dp.message_handler(state=FSMAdmin10.pvz)
		async def differ1_command(message : types.Message, state : FSMContext):
			global pvz
			global ttg6
			pvz = int(message.text)
			ttg6 = int(-ttg-pvz)
			await FSMAdmin10.next()
			await message.answer('Процентная ставка по кредиту')

		@dp.message_handler(state=FSMAdmin10.pck)
		async def differ2_command(message : types.Message, state : FSMContext):
			global pck
			pck = int(message.text)
			pck = (pck*0.01)/12
			await FSMAdmin10.next()
			await message.answer('Введите колличество месяцев на которые берется кредит')

		@dp.message_handler(state=FSMAdmin10.nk)
		async def differ3_command(message : types.Message, state : FSMContext):
			global nk
			global spk
			global ttgk
			global pck
			global ttg6
			nk = int(message.text)
			ttgk = 0
			while nk != 0:
				spk=int(ttg6/(nk+ttg6*pck))
				ttg6=int(ttg6-spk)
				nk-=1
				ttgk=int(ttgk+spk)
				await message.answer(f"Платеж за месяц {spk}")
			await message.answer(f"Общая сумма выплаты кредита {ttgk}. Переплаты по кредиту {ttgk-ttg6}")
			await state.finish()


		@dp.callback_query_handler(text='fff') #3
		async def fff_call(callback : types.CallbackQuery):
			await callback.message.answer('Кредит в мелкокредитной организации')	
			await callback.message.answer('Процентная ставка по кредиту в день, не больше 1%')	
			await FSMAdmin11.pck.set()

		@dp.message_handler(state=FSMAdmin11.pck)
		async def malko1_command(message : types.Message, state : FSMContext):
			global pck
			global ttg7
			ttg7=-ttg
			pck = float(message.text)
			pck=(pck*0.01)
			await FSMAdmin11.next()
			await message.answer('Введите колличество дней на которые берется микрозайм(обычно не более 90)')

		@dp.message_handler(state=FSMAdmin11.nk)
		async def malko2_command(message : types.Message, state : FSMContext):
			global nk
			global spk
			global ttgk
			global ttgp
			nk = int(message.text)
			spk=int(ttg7*pck)#Каждодневный процент
			ttgk=int(ttg7*spk*nk)#общая сумма кредита
			ttgp=int(ttg7*2.5)
			if ttgk>ttgp:
				await message.answer(f"Кредитные проценты вышли за норму, максимальная сумма которую вы заплатите = {ttgp}, из них переплаты составили {ttgp-ttg7}")
			else:
				await message.answer(f"Общая сумма кредита {ttgk}. ЕЖЕДНЕВНЫЙ процент = {spk}. Переплаты по кредиту {ttgk-ttg7}")
			await state.finish()
	await state.finish()

'''*********************************************СЕМЕЙНЫЙ ОБЩИЙ БЮДЖЕТ****************************************************'''
@dp.callback_query_handler(text='www')
async def www_call(callback : types.CallbackQuery):
	await callback.message.answer('Выберите вариант. Полный анализ или сокращенный', reply_markup=family)
	await callback.answer()

'''***********************************************СОКРАЩЕННЫЙ ВАРИНАТ****************************************************'''
@dp.message_handler(commands=['Сокрaщенный'], state=None)
async def fcokrash1_command(message : types.Message):
	await FSMAdmin3.ftp.set()
	await message.answer('Введите средние месячные поступления денежных средств в семью (зарплаты, пенсии, пособия)')

@dp.message_handler(state=FSMAdmin3.ftp)
async def fcokrash2_command(message : types.Message, state : FSMContext):
	global ftp
	ftp = int(message.text)
	await FSMAdmin3.next()
	await message.answer('Введите средние обязательные траты в месяц (продукты питания, квартира, транспортные расходы, обязательная аптека)')

@dp.message_handler(state=FSMAdmin3.ftm)
async def fcokrash3_command(message : types.Message, state : FSMContext):
	global ftm
	ftm = int(message.text)
	await FSMAdmin3.next()
	await message.answer('Введите средние сезонные траты в месяц (одежда, налоги, аптека по болезни)')

@dp.message_handler(state=FSMAdmin3.ftsm)
async def fcokrash4_command(message : types.Message, state : FSMContext):
	global ftsm
	ftsm= int(message.text)
	await FSMAdmin3.next()
	ftt = ftp-(ftm+ftsm)
	if ftt > 0:
		await message.answer('Все хорошо')
	if ftt <= 0:
		await message.answer('Нужен пересмотр семейного бюджета')
	await state.finish()
'''*************************************************ПОЛНЫЙ АНАЛИЗ********************************************************'''
@dp.message_handler(commands=['Пoлный'], state=None)
async def fpolniy1_command(message : types.Message):
	await FSMAdmin4.fp.set()
	await message.answer('Введите постоянную заработную плату первого члена семьи (например отца)')

@dp.message_handler(state=FSMAdmin4.fp)
async def fpolniy2_command(message : types.Message, state : FSMContext):
	global fp
	fp = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Введите постоянную заработную плату второго члена семьи (например матери)')

@dp.message_handler(state=FSMAdmin4.fm)
async def fpolniy3_command(message : types.Message, state : FSMContext):
	global fm
	fm = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Введите постоянную заработную плату третьего члена семьи (например совершеннолетние старшие дети, проживающие вместе с семьей)')

@dp.message_handler(state=FSMAdmin4.fbs)
async def fpolniy4_command(message : types.Message, state : FSMContext):
	global fbs
	fbs = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Введите постоянную заработную плату четвертого члена семьи (например дедушка, при условии совместного проживания)')

@dp.message_handler(state=FSMAdmin4.fd)
async def fpolniy5_command(message : types.Message, state : FSMContext):
	global fd
	fd = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Введите постоянную заработнную плату пятого члена семьи (например бабушка, при условии совместного проживание)')

@dp.message_handler(state=FSMAdmin4.fb)
async def fpolniy6_command(message : types.Message, state : FSMContext):
	global fb
	fb = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Введите постоянные пособия семьи в месяц')

@dp.message_handler(state=FSMAdmin4.fps)
async def fpolniy7_command(message : types.Message, state : FSMContext):
	global fps
	global ftp
	fps = int(message.text)
	ftp = fp+fm+fbs+fd+fb+fps
	await FSMAdmin4.next()
	await message.answer('Введите ежемесячные обязательные расходы')
	await message.answer('Комунальные платежи или общие траты на съемное жилье')

@dp.message_handler(state=FSMAdmin4.k)
async def fpolniy8_command(message : types.Message, state : FSMContext):
	global k
	k = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Продукты питания')

@dp.message_handler(state=FSMAdmin4.f)
async def fpolniy9_command(message : types.Message, state : FSMContext):
	global f
	f = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Ежемесячные аптечные препараты')

@dp.message_handler(state=FSMAdmin4.a)
async def fpolniy10_command(message : types.Message, state : FSMContext):
	global a
	a = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Ежемесячная одежда')

@dp.message_handler(state=FSMAdmin4.o)
async def fpolniy11_command(message : types.Message, state : FSMContext):
	global o
	o = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Транспортные расходы')

@dp.message_handler(state=FSMAdmin4.t)
async def fpolniy12_command(message : types.Message, state : FSMContext):
	global t
	t = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Секции, кружки, репетиторы и тд')

@dp.message_handler(state=FSMAdmin4.s)
async def fpolniy13_command(message : types.Message, state : FSMContext):
	global s
	s = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Развлечения, кино, рестораны')

@dp.message_handler(state=FSMAdmin4.r)
async def fpolniy14_command(message : types.Message, state : FSMContext):
	global r
	global ftm
	r = int(message.text)
	ftm = f+o+a+k+r+s+t
	await FSMAdmin4.next()
	await message.answer('Введите сезонные общие расходы')
	await message.answer('Сезонная одежда')

@dp.message_handler(state=FSMAdmin4.so)
async def fpolniy15_command(message : types.Message, state : FSMContext):
	global so
	so = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Сезонная аптека')

@dp.message_handler(state=FSMAdmin4.sa)
async def fpolniy16_command(message : types.Message, state : FSMContext):
	global sa
	sa = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Спортивный инвентарь')

@dp.message_handler(state=FSMAdmin4.si)
async def ppolniy17_command(message : types.Message, state : FSMContext):
	global si
	si = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Непредвиденные расходы на ремонт техники')

@dp.message_handler(state=FSMAdmin4.sr)
async def fpolniy18_command(message : types.Message, state : FSMContext):
	global sr
	sr = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Годовые затраты на отпуск')

@dp.message_handler(state=FSMAdmin4.sp)
async def fpolniy19_command(message : types.Message, state : FSMContext):
	global sp
	sp = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Налог на имущество')

@dp.message_handler(state=FSMAdmin4.sh)
async def fpolniy20_command(message : types.Message, state : FSMContext):
	global sh
	sh = int(message.text)
	await FSMAdmin4.next()
	await message.answer('Все сборы и налог на автомобиль')

@dp.message_handler(state=FSMAdmin4.ss)
async def fpolniy21_command(message : types.Message, state : FSMContext):
	global ss
	global ftsm
	global ttg
	global ftt
	ss = int(message.text)
	ftsm = (so+sa+si+sr+sp+sh+ss)/12
	ftt = ftp-(ftm+ftsm) #Денежные средства на балансе
	ttg = int(ftt*12)
	if ttg > 0:
		await message.answer('Все хорошо')
		await message.answer('Если семья хочет класть деньги на', reply_markup=inkb2)

		@dp.callback_query_handler(text='yyy') #1
		async def yyy_call(callback : types.CallbackQuery):
			await callback.message.answer('Обычные вклады')	
			await callback.message.answer('Введите процент')	
			await FSMAdmin5.pc.set()

		@dp.message_handler(state=FSMAdmin5.pc)
		async def procent1_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg2
			global ttg
			pc = int(message.text)
			pc=(pc*0.01)
			ttg1= int(ttg*(1+pc))
			ttg2 = int(ttg1-ttg)
			await message.answer(f"Семья заработала без вклада {ttg}, семья + вклад {ttg1}, семья получила прибыль от вклада {ttg2}")
			await state.finish()


		@dp.callback_query_handler(text='uuu') #2
		async def uuu_call(callback : types.CallbackQuery):
			await callback.message.answer('Квартальная капитализация')	
			await callback.message.answer('Введите процент')	
			await FSMAdmin6.pc.set()

		@dp.message_handler(state=FSMAdmin6.pc)
		async def procent2_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg2
			global ttg
			pc = int(message.text)
			pc=(pc*0.01)/4
			ttg1= int(ttg)
			for i1 in range(4):
				ttg1=int(ttg1*pc+ttg1)
			ttg2 = int(ttg1-ttg)
			await message.answer(f"Семья заработала без вклада {ttg}, семья + вклад {ttg1}, семья получила прибыль от вклада {ttg2}")
			await state.finish()


		@dp.callback_query_handler(text='iii') #3
		async def iii_call(callback : types.CallbackQuery):
			await callback.message.answer('Ежемесячная копитализация')	
			await callback.message.answer('Введите процент')	
			await FSMAdmin7.pc.set()

		@dp.message_handler(state=FSMAdmin7.pc)
		async def procent3_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg2
			global ttg
			pc = int(message.text)
			pc=(pc*0.01)/12
			ttg1= int(ttg)
			for i2 in range(12):
				ttg1=int(ttg1*pc+ttg1)
			ttg2 = int(ttg1-ttg)
			await message.answer(f"Семья заработала без вклада {ttg}, семья + вклад {ttg1}, семья получила прибыль от вклада {ttg2}")
			await state.finish()


		@dp.callback_query_handler(text='ooo') #4
		async def ooo_call(callback : types.CallbackQuery):
			await callback.message.answer('Государственные облигации')	
			await callback.message.answer('Введите процент')	
			await FSMAdmin8.pc.set()

		@dp.message_handler(state=FSMAdmin8.pc)
		async def procent4_command(message : types.Message, state : FSMContext):
			global pc
			global ttg1
			global ttg
			pc = int(message.text)
			pc=pc*0.01
			if ttg>400000:
				ttg1=int(ttg*(pc*0.01+1)+52000)
				await message.answer(f"Семья заработала вместе с облигациями {ttg1}. Процент по облигациям позволил заработать {ttg1-(52000+ttg)}. Так же был взят налоговый вычет суммой 52000") 
			else:
				ttg1=int(ttg*(pc*0.01+1)+(ttg*0.13))
				await message.answer(f"Семья заработала вместе с облигациями {ttg1}. Процент по облигациям позволил заработать {ttg1-ttg}. Так же был взят налоговый вычет суммой {ttg*0.13}")
			await state.finish()


		@dp.callback_query_handler(text='aaa') #0
		async def aaa_call(callback : types.CallbackQuery):
			await callback.message.answer(f"Семья заработала за год {ttg}")	

	if ttg <= 0:
		await message.answer('Кредитная история')
		await message.answer('Выберите', reply_markup=inkb3)

		@dp.callback_query_handler(text='sss') #1
		async def sss_call(callback : types.CallbackQuery):
			await callback.message.answer('Аннуитетный кредит')	
			await callback.message.answer('Введите сумму первоначального взноса')	
			await FSMAdmin9.pvz.set()

		@dp.message_handler(state=FSMAdmin9.pvz)
		async def anuitet1_command(message : types.Message, state : FSMContext):
			global pvz
			global ttg5
			pvz = int(message.text)
			ttg5 = int(-ttg-pvz)
			await FSMAdmin9.next()
			await message.answer('Процентная ставка по кредиту')

		@dp.message_handler(state=FSMAdmin9.pck)
		async def anuitet2_command(message : types.Message, state : FSMContext):
			global pck
			pck = int(message.text)
			pck = (pck*0.01)/12
			await FSMAdmin9.next()
			await message.answer('Введите колличество месяцев на которые берется кредит')

		@dp.message_handler(state=FSMAdmin9.nk)
		async def anuitet3_command(message : types.Message, state : FSMContext):
			global nk
			global spk
			global ttgk
			global pck
			nk = int(message.text)
			spk = int(ttg5*(pck*(1+pck)**nk)/((1+pck)**nk-1)) #Формула ежемесячных платежей
			ttgk = int(spk*nk) #Общая сумма кредита
			await message.answer(f"Общая сумма кредита {ttgk}. Ежемесячные платежи = {spk}. Переплаты по кредиту {ttgk-ttg5}")
			await state.finish()


		@dp.callback_query_handler(text='ddd') #2
		async def ddd_call(callback : types.CallbackQuery):
			await callback.message.answer('Дифференцированный кредит')	
			await callback.message.answer('Введите сумму первоначального взноса')	
			await FSMAdmin10.pvz.set()

		@dp.message_handler(state=FSMAdmin10.pvz)
		async def differ1_command(message : types.Message, state : FSMContext):
			global pvz
			global ttg6
			pvz = int(message.text)
			ttg6 = int(-ttg-pvz)
			await FSMAdmin10.next()
			await message.answer('Процентная ставка по кредиту')

		@dp.message_handler(state=FSMAdmin10.pck)
		async def differ2_command(message : types.Message, state : FSMContext):
			global pck
			pck = int(message.text)
			pck = (pck*0.01)/12
			await FSMAdmin10.next()
			await message.answer('Введите колличество месяцев на которые берется кредит')

		@dp.message_handler(state=FSMAdmin10.nk)
		async def differ3_command(message : types.Message, state : FSMContext):
			global nk
			global spk
			global ttgk
			global pck
			global ttg6
			nk = int(message.text)
			ttgk = 0
			while nk != 0:
				spk=int(ttg6/(nk+ttg6*pck))
				ttg6=int(ttg6-spk)
				nk-=1
				ttgk=int(ttgk+spk)
				await message.answer(f"Платеж за месяц {spk}")
			await message.answer(f"Общая сумма выплаты кредита {ttgk}. Переплаты по кредиту {ttgk-ttg6}")
			await state.finish()


		@dp.callback_query_handler(text='fff') #3
		async def fff_call(callback : types.CallbackQuery):
			await callback.message.answer('Кредит в мелкокредитной организации')	
			await callback.message.answer('Процентная ставка по кредиту в день, не больше 1%')	
			await FSMAdmin11.pck.set()

		@dp.message_handler(state=FSMAdmin11.pck)
		async def malko1_command(message : types.Message, state : FSMContext):
			global pck
			global ttg7
			ttg7=-ttg
			pck = float(message.text)
			pck=(pck*0.01)
			await FSMAdmin11.next()
			await message.answer('Введите колличество дней на которые берется микрозайм(обычно не более 90)')

		@dp.message_handler(state=FSMAdmin11.nk)
		async def malko2_command(message : types.Message, state : FSMContext):
			global nk
			global spk
			global ttgk
			global ttgp
			nk = int(message.text)
			spk=int(ttg7*pck)#Каждодневный процент
			ttgk=int(ttg7*spk*nk)#общая сумма кредита
			ttgp=int(ttg7*2.5)
			if ttgk>ttgp:
				await message.answer(f"Кредитные проценты вышли за норму, максимальная сумма которую вы заплатите = {ttgp}, из них переплаты составили {ttgp-ttg7}")
			else:
				await message.answer(f"Общая сумма кредита {ttgk}. ЕЖЕДНЕВНЫЙ процент = {spk}. Переплаты по кредиту {ttgk-ttg7}")
			await state.finish()


@dp.message_handler()
async def echo_send(message : types.Message):
	if message.text == 'Привет':
		await message.answer('И тебе привет!')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
