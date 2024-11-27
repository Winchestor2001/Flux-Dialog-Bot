from aiogram.filters.callback_data import CallbackData


class FluxOptionsCallback(CallbackData, prefix='mediation'):
    action: str
    context_id: int


class NextOptionCallback(CallbackData, prefix='next'):
    context_id: int