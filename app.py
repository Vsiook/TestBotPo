from aiogram.utils import executor
import logging


if __name__ == '__main__':
    from hendlers import dp

    executor.start_polling(dp, skip_updates=True)
