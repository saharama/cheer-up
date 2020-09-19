import discord
from discord.ext.commands import Bot

bot = Bot(command_prefix='$')
TOKEN = 'NzU2ODM5NzM0ODI2NzYyMzMx.X2Xr7g.Js7g-dk5OrZL3vblSe-jOtwdYX4'

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
	if message.content == 'test':
		await message.channel.send('Testing 1 2 3!')

bot.run(TOKEN)
