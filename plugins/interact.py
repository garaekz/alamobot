import random
import asyncio
import aiohttp

import discord
from discord.ext import commands as cmd

from utils import config

client = discord.Client()

class Interact:
    def __init__(self, bot):
        self.bot = bot

    @client.event
    async def on_message(self, message):
        if message.author.bot:
            return
        if self.bot.user.mentioned_in(message) and message.mention_everyone is False:
            if 'verga' in message.content.lower():
                if message.author.id == '392563417455656971':
                    await self.bot.send_message(message.channel, '¿Me llamabas, padre?')
                elif message.author.id == '391471511405330436':
                    await self.bot.send_message(message.channel, '¡Que pedo amo y señor de la República libre de Wakanda!')
                else:
                    await self.bot.send_message(message.channel, 'Ah como chingas prro!!!')
                print(message.author.id)
            elif 'test' in message.content.lower():
                    embed = discord.Embed(title=discord.Embed.Empty, description=discord.Embed.Empty, color=0x7ec0ee, url="")
                    embed.set_author(name=message.author.name, url="https://www.xvideos.com/", icon_url="https://cdn.discordapp.com/embed/avatars/0.png")
                    embed.add_field(name="PAINT ZOOM", value=("Con PAINT ZOOM olvídese de gastar un dineral en material ó contratando profesionales: PAINT ZOOM es más rápido, fácil y cómodo que los métodos tradicionales y los resultados son realmente inmejorables.\n"
                        "PAINT ZOOM es ideal para pintar tanto en interior como en exterior, en superficies lisas y porosas, tanto pequeñas ó grandes, muebles, puertas, vallas de una forma mucho mas facil \n"
                        "PAINT ZOOM es ligero y cómodo de llevar PAINT ZOOM es ligero y cómodo de llevar \n"
                        "Con PAINT ZOOM pinta 15 m2 en pocos minutos y sirve para todo tipo de pintura.\n"
                        "Pinta paredes, techos, y las zonas más complicadas de un modo rápido y uniforme, gracias a su pulverizador.\n"
                        "¡Obten resultados profesionales, sin marcas, sin goteos ni salpicaduras con PAINT ZOOM!"))
                    embed.set_image(url="https://cdn.discordapp.com/embed/avatars/0.png")
                    await self.bot.send_message(message.channel, embed=embed)
            else:
                if message.author.id == '392563417455656971':
                    await self.bot.send_message(message.channel, 'Que elocuente eres papá')
                else:
                    await self.bot.send_message(message.channel, 'Soy un bot no el puto Einsten para entender tus pendejadas *Todo raza el meco ¿si o no vato?*')
        await self.bot.process_commands(message)

def setup(bot):
    bot.add_cog(Interact(bot))