import discord
import os
import giphy_client
import random
from discord.ext.commands import Bot
from giphy_client.rest import ApiException

bot = Bot(command_prefix='$')
api_instance = giphy_client.DefaultApi()

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')

async def search_gifs(query):
	try:
		response = api_instance.gifs_search_get(GIPHY_TOKEN, query, limit=3, rating='g')
		list = list(response.data)
		gif = random.choices(lst)

		return gif[0].url

	except ApiException as e:
			return "Exception when calling DefaultApi->gifs_search_get: %s\n" % e

@bot.event
async def on_message(message):
	if message.content == 'test':
		await message.channel.send('Testing 1 2 3!')

@bot.command(name='8ball')
async def magic_eight_ball(ctx)
	response = [
		'Without a doubt.',
        'Outlook good.',
        'Better not tell you now.',
        'Cannot predict now.',
        'My reply is no.',
        'Outlook not so good.',
	]

	gif = awaot search_gifs('cheese')

	await ctx.send(randomw.choice(response))
	await ctx.send('Gif URL : ' + gif)

bot.run(os.environ['DISCORD_TOKEN'])
