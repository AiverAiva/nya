import os
import discord
import yaml

from supabase import create_client, Client

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

with open("config/default.yml", "r", encoding="utf-8") as file:
    config = yaml.safe_load(file)


async def userLevelField(member: discord.Member, guild: discord.Guild):
    (supabase.table('level')
     .insert(
        {"guild_id": guild.id,
         "user_id": member.id,
         "name": str(member),
         "level": 1,
         "xp": 0,
         "message": 0,
         "voice": 0,
         "invite": 0,
         "background": config['Default_Background'],
         "xp_colour": config['Default_XP_Colour'],
         "blur": 0,
         "border": config['Default_Border']}
    )
     .execute())
