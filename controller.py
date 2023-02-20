from id_token import TOKEN
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

""" Импорт функции и переменных """ 
from operatons import (start, 
                        choice, 
                        rational_one, 
                        rational_two, 
                        operatons_rational,
                        cancel,
                        CHOICE, 
                        RATIONAL_ONE, 
                        RATIONAL_TWO, 
                        OPERATIONS_RATIONAL)



bot = Bot(TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

""" Обучение бота """
conv_handler = ConversationHandler(entry_points = [CommandHandler('start', start)],
                                    states={CHOICE: [MessageHandler(Filters.text, choice)],
                                            RATIONAL_ONE: [MessageHandler(Filters.text, rational_one)],
                                            RATIONAL_TWO: [MessageHandler(Filters.text, rational_two)],
                                            OPERATIONS_RATIONAL: [MessageHandler(Filters.text, operatons_rational)]},
                                            fallbacks = [CommandHandler('cancel', cancel)])
                                

dispatcher.add_handler(conv_handler)
updater.start_polling()
updater.idle() 