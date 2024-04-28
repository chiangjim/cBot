import disnake
from disnake.ext import commands


class GoogleCommand(commands.Cog):
  """幫不會的人Google吧！"""

  def __init__(self, bot: commands.Bot):
    self.bot = bot

  @commands.slash_command(name="google")
  async def google_search(self, inter, query: str):
    """去google吧"""
    search_url = f"https://www.google.com/search?q={query}"
    await inter.response.send_message(search_url)


  @commands.command(name='google')
  async def google_search_command(self,inter, query = None):
    if query is None:
      return
    else:
      search_url = f"https://www.google.com/search?q={query.replace(' ','+')}"
      await inter.send(f"[{query}]({search_url})")

  @commands.message_command(name="google")
  async def google_search_message_command(self, inter, message: disnake.Message):
    search_url = f"https://www.google.com/search?q={message.content}"
    await inter.response.send_message(f"[{message.content}]({search_url})")

def setup(bot: commands.Bot):
  bot.add_cog(GoogleCommand(bot))