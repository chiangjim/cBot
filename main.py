import os
import disnake
from disnake.ext import commands

token = os.environ['token']


bot = commands.Bot(command_prefix="c", intents=disnake.Intents.all())

# for folder in os.listdir("./commands"):
#   for file in os.listdir(f"./commands/{folder}"):
#     if file.endswith(".py"):
#       bot.load_extension(f"commands.{folder}.{file[:-3]}")
#       print(f"✅ {folder}.{file[:-3]} 已完成載入")

@bot.event
async def on_ready():
  print(f"{bot.user.name} is ready!")


from tqdm import tqdm

files = []
for folder in os.listdir("./commands"):
  for file in os.listdir(f"./commands/{folder}"):
    files.append(f"{folder}.{file[:-3]}")

for file in tqdm(files):
  if file.endswith(".py"):
    bot.load_extension(f"commands.{file[:-3]}")



bot.run(token)