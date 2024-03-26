import discord
import asyncio
from discord import app_commands

#This script allows you to run an application through your discord bot, allowing you to claim an active developer badge.
#To use this script, you need a pre-existing application and bot on discord's developer portal already. If you don't have one, get started on Discord's portal.
#You only need to run this script and use the app once a month to keep the badge.
#Ensure discord.py is installed and working.
#See comments to fill in necessary entries

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def on_ready(self):
        await tree.sync(guild = discord.Object(id= None)) #Replace None with a proper guild (server) id
        print("Chew em' up, spit 'em out") #When this prints, bot is online and commands can be used.

client = MyClient(intents=discord.Intents.default())
tree = app_commands.CommandTree(client)

@tree.context_menu(name="Test", guild=discord.Object(id=None)) #Again, fill in id.
async def hello(interaction: discord.Interaction, user: discord.User):
    await interaction.response.send_message("The test is now over.") #put any message you want

client.run(None) #here is here you put your bot token.