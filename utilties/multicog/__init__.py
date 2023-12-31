"""A pycord extension that allows splitting command groups into multiple cogs."""

from typing import Callable, Dict, List, Optional

import discord
from discord.utils import copy_doc

__all__ = ("add_to_group", "apply_multicog", "Bot")


group_mapping: Dict[str, List[discord.SlashCommand]] = {}


def add_to_group(name: str) -> Callable[[discord.SlashCommand], discord.SlashCommand]:
    """A decorator to add a slash command to a slash command group.
    This will take effect and change the `parent` and `guild_ids` attributes
    of the command when `apply_multicog` is ran.
    """

    def decorator(command: discord.SlashCommand) -> discord.SlashCommand:
        if command.parent:
            raise TypeError(f"command {command.name} is already in a group.")

        try:
            group_mapping[name].append(command)
        except:
            group_mapping[name] = [command]

        return command

    return decorator


def find_group(bot: discord.Bot, name: str) -> Optional[discord.SlashCommandGroup]:
    """A helper function to find and return a (sub)group with the provided name."""

    for command in bot._pending_application_commands:
        if isinstance(command, discord.SlashCommandGroup):
            if command.name == name:
                return command

            for subcommand in command.subcommands:
                if (
                    isinstance(subcommand, discord.SlashCommandGroup)
                    and subcommand.name == name
                ):
                    return subcommand


def apply_multicog(bot: discord.Bot) -> None:
    """A function to update the attributes of the pending commands which were
    used with `add_to_group`.
    """

    for group_name, pending_commands in group_mapping.items():
        if (group := find_group(bot, group_name)) is None:
            raise RuntimeError(f"no slash command group named {group_name} found.")

        for command in pending_commands:
            command.guild_ids = group.guild_ids
            bot._pending_application_commands.remove(command)
            command.parent = group
            for cog in bot.cogs.values():
                if (
                    attr := getattr(cog, command.callback.__name__, None)
                ) and attr.callback == command.callback:
                    command.cog = cog
                    break
            else:
                command.cog = group.cog
                # fallback, will use the cog of the target group
            group.subcommands.append(command)


class Bot(discord.Bot):
    """A subclass of `discord.Bot` that calls `apply_multicog` when `sync_commands`
    is ran with no arguments."""

    @copy_doc(discord.Bot.sync_commands)
    async def sync_commands(
        self,
        commands: Optional[List[discord.ApplicationCommand]] = None,
        **kwargs,
    ) -> None:
        if not commands:
            apply_multicog(self)
        await super().sync_commands(commands, **kwargs)