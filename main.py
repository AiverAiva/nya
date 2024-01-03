import discord
import os
from discord.ext import commands, tasks
from itertools import cycle
from threading import Thread
from utilties.multicog import apply_multicog
from utilties.embeds import Error
from dotenv import load_dotenv
load_dotenv()

devMode = os.getenv('DEVMODE') 
token = os.getenv('TOKEN') 

# flaskh app for continuous repl.it run
if devMode != "TRUE":
  from flask import Flask
  app = Flask(__name__)
  @app.route('/')
  def hello():
      return 'Your Bot Is Ready'

  def run():
    app.run(host="0.0.0.0", port=8000)
     
  if __name__ == '__main__':
    server = Thread(target=run)
    server.start()
  
# start of discord stuff
intents = discord.Intents.default()
bot = commands.Bot(command_prefix="/", intents=intents)
status = cycle(['You <3'])

@bot.event
async def on_ready():
  change_status.start()
  print('{0.user} wake the fuck up'.format(bot))

@bot.event
async def on_application_command_error(ctx: discord.ApplicationContext, error: discord.DiscordException):
    await ctx.respond(embed=Error(f"Command: `/{ctx.command}`\nError: `{error}`\n\n**__Please report this!__**\n**Service Server** https://discord.gg/kcHfpfnYzE\n**Contact Developer** @aiveraiva\n**Report Issues** https://github.com/AiverAiva/nya/issues/new/choose"))

@tasks.loop(seconds=10)
async def change_status():
  await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=next(status)))

bot.load_extension("cogs", recursive=True)
apply_multicog(bot)
# for root, dirs, files in os.walk("./cogs"):
#     for dir in dirs:
#         for file in os.listdir(os.path.join(root, dir)):
#             if file.endswith(".py"):
#                 file_path = os.path.join(root, dir, file)
#                 module_path = os.path.relpath(file_path, './cogs').replace(os.path.sep, '.')[:-3]
#                 bot.load_extension(f'cogs.{module_path}')
          
bot.run(token)