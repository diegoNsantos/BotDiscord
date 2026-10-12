import discord
from discord.ext import commands

intents = discord.Intents.all()
bot = commands.Bot(".", intents=intents)


@bot.event
async def on_ready():
    print("Bot Ligado")


@bot.command()
async def somar(ctx: commands.Context, num1: float, num2: float):
    resultado = num1 + num2
    await ctx.send(f"A soma entre `{num1}` e `{num2}` é igual a `{resultado}`")

bot.run("CHAVE DO BOT AQUI")