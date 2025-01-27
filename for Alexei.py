#Подключение к тг
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters 
TOKEN = "7926622926:AAGbOZdWTCs6ArwLEz4kWmOFRfFB9jM58qc"

async def start(update: Update, context):
    await update.message.reply_text(f"Помогу тебе решить твое любимое квадратное уравнение на раз-два")

async def echo(update: Update, context):
    user_message = update.message.text
    await update.message.reply_text(f"ті сказаль: {user_message}")
def main():
    app = Application.builder(). token(TOKEN). build()
    app.add_handler(CommandHandler("start",start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    app.run_polling()
if __name__ == "__main__":
    main()






#БОТ
print("Твоя общая формула : ax^2 + bx + c")
a = float(input("введи значение для а: "))
b = float(input("теперь для b: "))
c = float(input ("ну и теперь c: "))


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








