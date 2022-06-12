from time import time
from inspect import getsource
import discord
import traceback
from discord.ext import commands
import sys
import os
from colorama import Fore as Color


class eval(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def resolve_variable(self, variable):
        if hasattr(variable, "__iter__"):
            var_length = len(list(variable))
            if (var_length > 100) and (not isinstance(variable, str)):
                return f"<a {type(variable).__name__} iterable with more than 100 values ({var_length})>"
            elif not var_length:
                return f"<an empty {type(variable).__name__} iterable>"

        if (not variable) and (not isinstance(variable, bool)):
            return f"<an empty {type(variable).__name__} object>"
        return (
            variable
            if (len(f"{variable}") <= 1000)
            else f"<a long {type(variable).__name__} object with the length of {len(f'{variable}'):,}>"
        )

    def prepare(self, string):
        arr = (
            string.strip("```").replace("py\n", "").replace("python\n", "").split("\n")
        )
        if not arr[::-1][0].replace(" ", "").startswith("return"):
            arr[len(arr) - 1] = "return " + arr[::-1][0]
        return "".join(f"\n\t{i}" for i in arr)

    @commands.command(
        pass_context=True,
        aliases=["eval", "exec", "evaluate"],
        description="Evaluates given code",
    )
    @commands.is_owner()
    async def _eval(self, ctx, *, code: str):
        silent = "-s" in code

        code = self.prepare(code.replace("-s", ""))
        args = {
            "discord": discord,
            "sauce": getsource,
            "sys": sys,
            "os": os,
            "imp": __import__,
            "message": ctx.message,
            "send": ctx.send,
            "self": self,
            "ctx": ctx,
            "member": ctx.author,
            "bot": self.bot,
        }

        try:
            exec(f"async def func():{code}", args)
            a = time()
            response = await eval("func()", args)
            if silent or (response is None) or isinstance(response, discord.Message):
                em = discord.Embed(
                    title="Eval Success :D",
                    description="```Code ran without any errors```",
                )
                print(f"{Color.WHITE} {ctx.author} just used the eval command. {Color.MAGENTA} Guild: {ctx.guild} {Color.CYAN} Channel: {ctx.channel}")
                await ctx.message.reply(embed=em, mention_author=False)
                del args, code
                return
            em = discord.Embed(
                title="Eval Success :o",
                description=f"```py\n{self.resolve_variable(response)}```",
            )
            em.set_footer(
                text=f"`{type(response).__name__} | {(time() - a) / 1000} ms`"
            )
            await ctx.message.reply(embed=em, mention_author=False)
        except Exception as e:
            exception = '\n'.join(traceback.format_exception(type(e), e, e.__traceback__))
            em = discord.Embed(
                title=f"Eval Error ._. ({e.__class__.__name__})",
                description=f"```py\n{exception}```",
                color = discord.Color.red()
            )

            await ctx.message.reply(embed=em, mention_author=False)

        del args, code, silent


def setup(bot):
    bot.add_cog(eval(bot))