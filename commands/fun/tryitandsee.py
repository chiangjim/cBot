import disnake
from disnake.ext import commands


class TryItAndSeeCommand(commands.Cog):
  """還不快去試試看！"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self,message):
    if "try it and see" in message.content.lower() or "試試看" in message.content:
      await message.channel.send("https://tryitands.ee")
    await self.bot.process_commands(message)


def setup(bot: commands.Bot):
  bot.add_cog(TryItAndSeeCommand(bot))