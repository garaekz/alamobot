import random
import asyncio
import aiohttp

import discord
from discord.ext import commands as cmd

from utils import config

class Otaku:
    def __init__(self, bot):
        self.bot = bot

    @cmd.command(name="test", pass_context=True)
    async def test(self, ctx):
        embed = discord.Embed(title="Aquí tampoco", description="Solo es una prueba", color=0x7ec0ee, url="https://www.xvideos.com/")
        embed.set_author(name="No me des click", url="https://www.xvideos.com/", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.set_footer(text="La mera posha con sebosha", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
        embed.add_field(name="PAINT ZOOM", value=("Con PAINT ZOOM olvídese de gastar un dineral en material ó contratando profesionales: PAINT ZOOM es más rápido, fácil y cómodo que los métodos tradicionales y los resultados son realmente inmejorables.\n"
            "PAINT ZOOM es ideal para pintar tanto en interior como en exterior, en superficies lisas y porosas, tanto pequeñas ó grandes, muebles, puertas, vallas de una forma mucho mas facil \n"
            "PAINT ZOOM es ligero y cómodo de llevar PAINT ZOOM es ligero y cómodo de llevar \n"
            "Con PAINT ZOOM pinta 15 m2 en pocos minutos y sirve para todo tipo de pintura.\n"
            "Pinta paredes, techos, y las zonas más complicadas de un modo rápido y uniforme, gracias a su pulverizador.\n"
            "¡Obten resultados profesionales, sin marcas, sin goteos ni salpicaduras con PAINT ZOOM!"))
        await self.bot.send_message(ctx.message.channel, embed=embed)

def setup(bot):
    bot.add_cog(Otaku(bot))