import random
import asyncio
import aiohttp
import urllib

import discord
from discord.ext import commands as cmd
from discord.ext.commands import when_mentioned_or
from utils import config
from utils.helpers import clima_owm, clima_yh

class Info:
    def __init__(self, bot):
        self.bot = bot

    @cmd.command(name='8ball',
                    prefix=when_mentioned_or("&"),
                    description="Responde una pregunta de si/no.",
                    brief="Respuestas pendejas a preguntas pendejas",
                    aliases=['eight_ball', 'eightball', '8-ball', 'bola8', 'bolaocho'],
                    pass_context=True)
    async def eight_ball(self, ctx, *, pregunta=None):
        possible_responses = [
            'No se arma compa',
            'Chicle y pega',
            'Tas muy pendejo',
            'Parece que es posible pero nel',
            'Awebo prro!',
            'A lo mejor si se hace pero no esperes parado',
        ]
        print(pregunta)
        if not pregunta:
          await self.bot.say("Namames, ¡preguntame algo!")
        else:
          await self.bot.say(":8ball: **| " + random.choice(possible_responses) + ", " + ctx.message.author.mention+ "**")
          


    @cmd.command()
    async def cuadrado(self, number):
        squared_value = int(number) * int(number)
        await self.bot.say(str(number) + " al cuadrado es:  " + str(squared_value) + " *estoy bien cabrón*")
    @cmd.command(name="info")
    async def info(self):
        await self.bot.say("\n"
                           "Que pedo, soy el Alamobot; Soy un bot irreverente para mamonear en El Alamo Comunidad Gamer.\n"
                           "Podras ver mis entrañas en Github: https://github.com/garaekz/alamobot\n")
    @cmd.command()
    async def clima(self, *, ciudad=None):
        if ciudad is None:
          await self.bot.say("Namames, **¡pon la ciudad!**")
        else:
          if config["api"]["provider"] == "OWM":
            clima = await clima_owm(ciudad)
            await self.bot.say(clima)

          elif config["api"]["provider"] == "YH":
            clima = await clima_yh(ciudad)
            await self.bot.say(clima)

          else:
            pass

def setup(bot):
    bot.add_cog(Info(bot))