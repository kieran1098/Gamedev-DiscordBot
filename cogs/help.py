import discord
from discord.ext import commands


# Set the bot prefix
bot_prefix = "??"
command_prefix = "/"


# Define intents
intents = discord.Intents.all()
intents.messages = True
intents.members = True  # Enable the GUILD_MEMBERS intent
intents.guilds = True

# Create a bot instance with a command prefix and intents
bot = commands.Bot(command_prefix=bot_prefix,
                   intents=intents, help_command=None)


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        # Create embeds for each help page
        pages = [
            discord.Embed(title="🧬generation Commands",
                          description="Commands for idea generation",
                          color=discord.Color.blue()),
            discord.Embed(title="🛠️Utility Commands",
                          description="Commands for utility purposes",
                          color=discord.Color.green()),
            discord.Embed(title="💻development Commands",
                          description="Commands for the development library",
                          color=discord.Color.red()),
            discord.Embed(title="🤝support Commands",
                          description="Commands for supporting my work",
                          color=discord.Color.yellow()),
            discord.Embed(title="📖resources Commands",
                          description="Commands for resources",
                          color=discord.Color.orange()),
            discord.Embed(title="⛏️tools Commands",
                          description="Commands for game dev tools",
                          color=discord.Color.purple())
        ]

        # Add fields for each page
        pages[0].add_field(
            name="idea", value="`gives you a random idea to explore.`")
        pages[0].add_field(name="image", value="`sends random images.`")
        pages[0].add_field(name="randompalette",
                           value="`generates a random color palette.`")

        pages[1].add_field(
            name="poll 'question' options", value="`starts a poll.`")
        pages[1].add_field(name="coinflip", value="`50/50 chance coinflip.`")
        pages[1].add_field(name="ping", value="`displays bots ping`")

        pages[2].add_field(name="sound", value="`sends random sounds.`")
        pages[2].add_field(name="texture(brick/metal/fabric/concrete/wood)",
                           value="`displays random texture EXAMPLE: >>texturebrick`")

        pages[3].add_field(
            name="discord", value="`sends owners discord server.`")
        pages[3].add_field(name="patreon", value="`support my work.`")
        pages[3].add_field(name="bump", value="`sends discord.me site for bot`")

        pages[4].add_field(name="ModellingTUTs",
                           value="`modelling tutorials free to download.`")
        pages[4].add_field(name="EngineTUTs",
                           value="`engine tutorials free to download.`")
        pages[4].add_field(name="TexturingTUTs",
                           value="`texturing tutorials free to download.`")
        pages[4].add_field(name="SculptingTUTs",
                           value="`sculpting tutorials free to download.`")

        pages[5].add_field(name="review 'pasted code'",
                           value="`reviews your basic code (python).`")
        pages[5].add_field(
            name="events", value="`attempts to find game dev events.`")

        # Create initial message with the first page
        current_page = 0
        message = await ctx.send(embed=pages[current_page])

        # Define emojis for navigation
        emojis = ['⬅️', '➡️']

        # Add reactions for navigation
        for emoji in emojis:
            await message.add_reaction(emoji)

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) in emojis

        while True:
            try:
                # Wait for reaction from the user
                reaction, user = await self.bot.wait_for('reaction_add',
                                                         timeout=60.0,
                                                         check=check)

                # Determine the navigation direction based on the reaction
                if str(reaction.emoji) == '⬅️':
                    current_page = (current_page - 1) % len(pages)
                elif str(reaction.emoji) == '➡️':
                    current_page = (current_page + 1) % len(pages)

                    # Add a check to reset the current page if it exceeds the length
                if current_page >= len(pages):
                    current_page = 0

                # Update the message with the new page
                await message.edit(embed=pages[current_page])

                # Remove the reaction from the user
                await message.remove_reaction(reaction, user)
            except:
                break


async def setup(bot):
    await bot.add_cog(Help(bot))
