import discord
from discord.ext import commands
from easy_pil import Editor, Canvas, load_image, load_image_async, Font
# from discord.commands import Option
import sys
# import utilties.database as Database
# import utilties.wynncraft.emoji as emoji
import database.check as check

sys.path.append("..")

bot = discord.Bot()


class Profile(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(name="profile", description="show the profile", pass_context=True)
    async def profile(self, ctx):
        # user = await bot.fetch_user()
        #         profile = await Database.getUserData(ctx.author.id)
        await check.checkUserLevelField(member=ctx.author, guild=ctx.guild)
        board = Canvas(width=1050, height=300)
        background = Editor(board).resize((1050, 300)).blur(amount=2)

        profile_image = load_image(ctx.author.display_avatar.url)
        profile = Editor(profile_image).resize((200, 210)).circle_image()
        background.paste(profile, (35, 45))

        font_25: Font = Font.poppins(size=35, variant="bold")
        font_60_bold: Font = Font.poppins(size=60, variant="bold")
        font_40_bold: Font = Font.poppins(size=50, variant="bold")

        background.text((270, 150), f"Level: 1234", font=font_25, color="white")

        background.rectangle((260, 190), width=600, height=40, radius=20)
        # user = await bot.fetch_user(ctx.author.id)
        # banner_url = user.banner.url
        # embed = discord.Embed(
        #     title=f'{ctx.author.display_name}\'s Profile',
        #
        #     # description=f'{user}'
        #     # color=
        # )

        #         image = await load_image_async(user.banner.url)
        #         editor = Editor(image)
        file = discord.File(fp=background.image_bytes, filename='rank_card.png')
        #         embed.set_thumbnail(url=ctx.author.display_avatar.url)
        #         # embed.set_image(ctx.author.banner)
        #         embed.add_field(name=f"**Linked Accounts**", value=f"{emoji.wynnIcon} Wynncraft `{profile['wynncraft']}`")
        await ctx.respond(content=ctx.author.id, file=file)


def setup(bot):
    bot.add_cog(Profile(bot))
