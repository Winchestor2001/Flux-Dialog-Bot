from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from callback_data import FluxOptionsCallback, NextOptionCallback


# Кнопки для да/нет
def flux_options(yes_id: int, no_id: int):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Да", callback_data=FluxOptionsCallback(action="yes", context_id=yes_id).pack())],
        [InlineKeyboardButton(text="Нет", callback_data=FluxOptionsCallback(action="no", context_id=no_id).pack())]
    ])
    return keyboard

# Кнопка "Далее"
def next_button(next_id: int):
    keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Далее", callback_data=NextOptionCallback(context_id=next_id).pack())]
    ])
    return keyboard
