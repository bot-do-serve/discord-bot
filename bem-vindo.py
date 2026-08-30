import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Contador para armazenar a quantidade de menções
mencoes_count = 0

@bot.event
async def on_ready():
    print(f'Bot conectado com sucesso como {bot.user}')

@bot.event
async def on_message(message):
    global mencoes_count

    # Evita que o bot responda a si mesmo ou a outros bots
    if message.author.bot:
        return

    # Verifica se o bot foi mencionado na mensagem
    if bot.user in message.mentions:
        mencoes_count += 1

        if mencoes_count >= 3:
            await message.channel.send("porra ta vendo que eu não tenho nehuma funcionabilidade, para de me chama o corno, certeza que é renan")
        else:
            await message.channel.send("Eu estou em desenvolvimento e estou ansioso para participar das suas resenhas 24hs!")

    await bot.process_commands(message)

TOKEN = 'MTU0MzMwMjI2MDA4MjIxNzA4MQ.GRc_Gu.En3-6B6CIMgPI0Ytleat2Apm5anM5ys343cJ5w'
bot.run(TOKEN)