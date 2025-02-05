#Подключение к тг
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
TOKEN = "7926622926:AAGbOZdWTCs6ArwLEz4kWmOFRfFB9jM58qc"

position, a, b, c = 0, 0, 0, 0

 # Приветствие
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    global position
    await update.message.reply_text("Даров, помогу без б с твоими уравнениями")
    await update.message.reply_text("Твоя общая формула : ax^2 + bx + c")
    position = 0
#Бот
async def handle_message(update: Update, context: ContextTypes. DEFAULT_TYPE):
    global position, a, b, c
    text = update.message.text

    try:
        if position==0:
            a = float(text)
            position +=1
            await update.message.reply_text("✅ Принял коэффициент a")
            
        
        elif position==1:
            b = float(text)
            position +=1
            await update.message.reply_text("✅ Принял коэффициент b")
        
        elif position==2: 
            c = float(text)
            position +=1
            await update.message.reply_text("✅ Принял коэффициент c, ⌛ Произвожу расчет...")
    
    
    #   Решение после получения коефициентов
            D = b**2 - 4*a*c
            if D > 0:
                sqrt_d = D**0.5
                x1 = (-b + sqrt_d)/(2*a)
                x2 = (-b - sqrt_d)/(2*a)
                await update.message.reply_text(
                    f"🔍 Два решения:\n"
                    f"x₁ = {x1:.2f}\n"
                    f"x₂ = {x2:.2f}"
                )
            elif D == 0:
                x= -b/(2*a)
            await update.message.reply_text(f"⚡ Одно решение: x = {x:.2f}")
        else:
            await update.message.reply_text("❌ Нет действительных решений")

        position = 0

    except ValueError:
        await update.message.reply_text("Пожалуйста, вводи только числа!")
        position = 0  # Сброс при ошибке ввода
def main():
    app = Application.builder(). token(TOKEN). build()
    app.add_handler(CommandHandler("start",start_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()



