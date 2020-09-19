import discord
from discord.ext.commands import Bot
import os

bot = Bot(command_prefix='$')

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

@bot.event
async def on_message(message):
	if message.content == 'test':
		await message.channel.send('Testing 1 2 3!')

bot.run(os.environ['DISCORD_TOKEN'])
