import nextcord  # Imports the nextcord library
from nextcord.ext import commands  # Imports the commands function

client = commands.Bot(command_prefix="!")  # Defines your bot as a client and gives your bot a standard command prefix
Token = "YOUR DISCORD BOT TOKEN"  # Defines your bot token (REPLACE "YOUR DISCORD BOT TOKEN" WITH YOU BOT TOKEN)
testingServerid = 1234567890 # Defines your guild id (REPLACE "1234567890" WITH YOUR GUILD ID)

@client.event                               
async def on_ready():                       # Prints a message when the file was succesfully loaded
  print(f"I'm ready as: {client.user}")
 
@client.slash_command(description="Ping command", guild_ids=[testingServerid])
async def ping(interaction : nextcord.Interaction):
  await interaction.send("Pong!")
  
@client.run(Token)   # Runs your bot
