import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print('Loggend in Bot: ', bot.user.name)
    print('Bot id: ', bot.user.id)
    print('connection was succesful!')
    print('=' * 30)

@bot.command(aliases=['hi', 'Hello'])
async def hello(ctx):
    await ctx.send("{0}, hi".format(ctx.author.mention))

@bot.command(aliases=['곰', 'Bear'])
async def bear(ctx, *, msg):
    BEAR = "고민재"
    if msg == BEAR:
        await ctx.send("{0}은 곰입니다".format(msg))
    else:
        await ctx.send("{0}은 곰이 아닙니다".format(msg))

@bot.command()
async def embed(ctx):
    embed = discord.Embed(title="예준이", description="잡다한거 다 하는 봇", color=0xf08080)
    # embed.set_thumbnail(url="")
    embed.add_field(name="-명령어 모음-", value="명령어 사용법", inline=False)
    embed.add_field(name="인사", value="!hello, !hi, !Hello", inline=False)
    embed.add_field(name="곰판별기", value="!bear 이름, !Bear 이름, !곰 이름", inline=False)
    embed.add_field(name="추가 예정", value="coming soon", inline=False)
    embed.set_footer(text="Bot Made by waterdog05")

    await ctx.send(embed=embed)

bot.run('my tocken')
