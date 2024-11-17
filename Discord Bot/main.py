import nextcord  # Imports the nextcord library
from nextcord.ext import commands  # Imports the commands function

client = commands.Bot(command_prefix="!")  # Defines your bot as a client and gives your bot a standard command prefix
Token = "YOUR DISCORD BOT TOKEN"  # Defines your bot token (REPLACE "YOUR DISCORD BOT TOKEN" WITH YOU BOT TOKEN)

@client.event                               
async def on_ready():                       # Prints a message when the file was succesfully loaded
    print(f"Logged in as {client.user} (ID: {client.user.id})")
  
  
@client.run(Token)   # Runs your bot
