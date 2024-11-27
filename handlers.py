from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, FSInputFile
from aiogram.fsm.context import FSMContext

from callback_data import FluxOptionsCallback, NextOptionCallback
from states import FluxStates
from keyboards import flux_options, next_button
from context import DIALOGS

router = Router()


# 1. Стартовый хендлер
@router.message(F.text == "/start")
async def start_handler(message: Message, state: FSMContext):
    await state.clear()

    await message.answer(
        text=DIALOGS["1"]['text']
    )
    await message.answer(
        text=DIALOGS["2"]['text'],
        reply_markup=flux_options(yes_id=4, no_id=3)
    )


@router.callback_query(FluxOptionsCallback.filter())
async def flux_options_callback(c: CallbackQuery, state: FSMContext):
    cd , action, context_id = c.data.split(":")
    next_id = 4
    if context_id == 3:
        next_id = 2
    btn = next_button(next_id) if action == "no" else None
    await c.message.edit_text(
        text=DIALOGS[context_id]['text'],
        reply_markup=btn
    )
    await state.set_state(FluxStates.four)


@router.callback_query(NextOptionCallback.filter())
async def next_option_callback(c: CallbackQuery, state: FSMContext):
    cd , context_id = c.data.split(":")
    if DIALOGS[context_id].get("img", False):
        await c.message.edit_reply_markup()
        await c.message.answer_photo(
            photo=FSInputFile(path=DIALOGS[context_id]["img"]),
            caption=DIALOGS[context_id]['text']
        )
    else:
        await c.message.edit_text(
            text=DIALOGS[context_id]['text'],
        )


@router.message(FluxStates.four)
async def four_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["4"]['text']: message.text})
    btn = next_button(6)
    await message.answer(
        text=DIALOGS["5"]['text'],
        reply_markup=btn
    )
    await state.set_state(FluxStates.six)


@router.message(FluxStates.six)
async def six_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["6"]['text']: message.text})
    await message.answer_photo(
        photo=FSInputFile(path=DIALOGS["7"]['img']),
        caption=DIALOGS["7"]['text']
    )
    await state.set_state(FluxStates.seven)


@router.message(FluxStates.seven)
async def seven_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["7"]['text']: message.text})
    await message.answer_photo(
        photo=FSInputFile(path=DIALOGS["8"]['img']),
        caption=DIALOGS["8"]['text']
    )
    await state.set_state(FluxStates.eight)


@router.message(FluxStates.eight)
async def eight_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["8"]['text']: message.text})
    await message.answer(
        text=DIALOGS["9"]['text']
    )
    btn = next_button(next_id=11)
    await message.answer(
        text=DIALOGS["10"]['text'],
        reply_markup=btn
    )
    await state.set_state(FluxStates.eleven)


@router.message(FluxStates.eleven)
async def eleven_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["11"]['text']: message.text})
    await message.answer(
        text=DIALOGS["12"]['text']
    )
    btn = next_button(next_id=14)
    await message.answer(
        text=DIALOGS["13"]['text'],
        reply_markup=btn
    )
    await state.set_state(FluxStates.fourteen)


@router.message(FluxStates.fourteen)
async def fourteen_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["14"]['text']: message.text})
    btn = next_button(next_id=16)
    await message.answer(
        text=DIALOGS["15"]['text'],
        reply_markup=btn
    )
    await state.set_state(FluxStates.sixteen)


@router.message(FluxStates.sixteen)
async def fourteen_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["16"]['text']: message.text})
    btn = next_button(next_id=19)
    await message.answer_photo(
        photo=FSInputFile(path=DIALOGS["17"]['img']),
        caption=DIALOGS["17"]['text'],
    )
    await message.answer(
        text=DIALOGS["18"]['text'],
        reply_markup=btn
    )
    await state.set_state(FluxStates.nineteen)



@router.message(FluxStates.nineteen)
async def fourteen_state(message: Message, state: FSMContext):
    await state.update_data({DIALOGS["19"]['text']: message.text})
    btn = next_button(next_id=21)
    await message.answer_photo(
        photo=FSInputFile(path=DIALOGS["20"]['img']),
        caption=DIALOGS["20"]['text'],
        reply_markup=btn
    )
    data = await state.get_data()

    context = f"<a href='tg://user?id={message.from_user.id}'>{message.from_user.full_name}</a>\n\n"
    for item in data.items():
        context += f"<b>{item[0]}</b>:\n<blockquote>{item[1]}</blockquote>\n\n\n"

    await message.answer(text=context)

    await state.clear()