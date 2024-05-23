import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='-', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def merhaba(ctx):
    await ctx.send(f'evde ürettiğiniz atık miktarını azaltmak için yapabileceğiniz bir çok şey var,mesela:
                   Alışverişlerinizi planlayın. ...
                    Dondurucunuzu kullanın. ...
                    Bir kompost cihazı kullanın. ...
                    Evde yeşillik yetiştirin. ...
                    Kabukları saklayın. ...
                    Yiyeceklerinizin raf ömrünü uzatın. ...
                    Plastik atığını ve ambalajları azaltın. ...
                    Dökme, toptan ve donmuş ürünler alın.')

@bot.command()
async def video(ctx):
    await ctx.send(f'https://www.youtube.com/watch?v=XT1_e7cn_tQ,işte bu şekilde atık miktarını azaltabiliriz')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

bot.run("GIZLI JETON BURAYA GIRILI!1(KIMSEYE GOSTERME!!)")
