#Подключение к тг
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "7926622926:AAGbOZdWTCs6ArwLEz4kWmOFRfFB9jM58qc"
position,a, b, c = 0, 0, 0
 # Приветствие
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Даров, помогу без б с твоими уравнениями")
    await update.message.reply_text("Твоя общая формула : ax^2 + bx + c")

async def echo(update: Update, context: ContextTypes. DEFAULT_TYPE):
    global position, a, b, c
    text = update.message
    if position==0:
        try:
            a = float(text)
            position =+1
        except:
            return("Сори, бро, но не понимаю текст.")
    if position==1:
        try:
            b = float(text)
            position =+1
        except:
            return("Та вводи числа, а не текст, оболдуй.")
    if position==2:
        try:
            c = float(text)
            position =-2
        except:
            return("Давай, бубна, не балуйся. Почти закончили.")
        


def main():
    app = Application.builder(). token(TOKEN). build()
    app.add_handler(CommandHandler("start",start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()

if __name__ == "__main__":
    main()



print ("Твоя общая формула : ax^2 + bx + c")
a = float(input("введи значение для а: "))
b = float(input("теперь для b: "))
c = float(input("ну и теперь c: "))


D = (b**2) - (4*a*c)
if D > 0:
    print("Уравнение имеет 2 решения:")
    square = D**0.5
    x1= (-b + square)/(2*a)
    x2= (-b - square)/(2*a)
    print ("x1= ",x1)
    print ("x2= ",x2)
if D == 0:
    print("Уравнение имеет только одно решение")
    x= -b/(2*a)
    print("x= ",x)
if D<0:
     print("Уравнение не имеет решений")