import discord
from discord.ext import commands
from model import get_class

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(f"Guarda la imagen en ./{attachment.filename}")
            try:
                clase = get_class("keras_model.h5", "labels.txt", f"./{file_name}")
                if clase[0] == "Comida Saludable":
                    await ctx.send("Esta comida que enviaste es saludable, es muy buena para tu cuerpo ya que te proporciona energia y protección, asi que si estas comiendo de este tipo de comida constantemente, muy bien, sigue asi, tu dieta es saludable y seras una persona fuerte. ")
                elif clase[0] == "Comida Chatarra":
                    await ctx.send("Este tipo de alimento no es tan bueno para tu cuerpo, ya que te hace engordar, comerlo de vez en cuando no esta mal, pero si se vuelve constante te puede hacer mucho mal.")
            except:
                await ctx.send("Ha ocurrido un error")
    else:
        await ctx.send("Olvidaste subir la imagen :(")

bot.run("MTI0MDExMjczOTQ5ODg1NjUyOQ.GAhT-p.dX3uwKaXHhxBP_SkvYpPW_RyjoSWABdyZ91bVU")
