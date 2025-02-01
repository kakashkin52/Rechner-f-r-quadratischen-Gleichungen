from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import math

TOKEN = "7926622926:AAGbOZdWTCs6ArwLEz4kWmOFRfFB9jM58qc"

# Command to solve quadratic equations
async def solve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        # Extract coefficients from the command (e.g., /solve 1 -5 6)
        a = float(context.args[0])
        b = float(context.args[1])
        c = float(context.args[2])
        
        # Handle invalid input (e.g., a = 0)
        if a == 0:
            await update.message.reply_text("Error: 'a' cannot be zero (not a quadratic equation).")
            return
        
        # Calculate discriminant
        discriminant = b**2 - 4*a*c
        
        # Compute roots
        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2*a)
            root2 = (-b - math.sqrt(discriminant)) / (2*a)
            response = f"Roots: x₁ = {root1:.2f}, x₂ = {root2:.2f}"
        elif discriminant == 0:
            root = -b / (2*a)
            response = f"Double root: x = {root:.2f}"
        else:
            real_part = -b / (2*a)
            imaginary_part = math.sqrt(abs(discriminant)) / (2*a)
            response = f"Complex roots: x₁ = {real_part:.2f} + {imaginary_part:.2f}i, x₂ = {real_part:.2f} - {imaginary_part:.2f}i"
        
        await update.message.reply_text(response)
    
    except (IndexError, ValueError):
        await update.message.reply_text("⚠️ Invalid input. Use format: /solve a b c\nExample: /solve 1 -5 6")

# Start the bot
if __name__ == "__main__":
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("solve", solve))
    app.run_polling()








