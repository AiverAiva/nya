import os
import discord
import yaml

from supabase import create_client, Client

from database.insert import userLevelField

url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


async def checkUserLevelField(member: discord.Member, guild: discord.Guild):
    try:
        data = (supabase.table('level')
                .select("guild_id, user_id")
                .eq("guild_id", guild)
                .eq("user_id", member)
                .execute())
    except Exception as e:
        await userLevelField(member, guild)
        # print(e)
    # print(data)
