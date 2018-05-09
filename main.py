import sys
import logging
import traceback

import logbook
import discord
from discord.ext import commands
from logbook import Logger, StreamHandler
from logbook.compat import redirect_logging
from discord.ext.commands import Bot

from utils import config

# Plugins se inicializan en run()
plugins = ["plugins.basic", "plugins.otaku", "plugins.interact"]


class Alamo(Bot):

    def __init__(self, *args, **kwargs):
        super().__init__(command_prefix=config["discord"]["prefijo"],
                         description="Discord bot para Comunidad Gamer El Alamo")

        #Pieza de codigo tomada de https://github.com/GetRektByMe/Pixie para log
        redirect_logging()
        StreamHandler(sys.stderr).push_application()
        self.logger = Logger("Alamo")
        self.logger.level = getattr(logbook, config.get("log_level", "INFO"), logbook.INFO)
        logging.root.setLevel(self.logger.level)

    async def on_ready(self):
        await self.change_presence(game=discord.Game(name="las matatenas"))
        self.logger.info("Bot loggeado como Nombre: {0.user.name} ID: {0.user.id}".format(self))

    async def on_command_error(self, exception, ctx):
        print(exception)
        if isinstance(exception, commands.errors.CommandNotFound):
            await self.send_message(ctx.message.channel, "Mames! El comando no existe *...mirada de estas bien pendejo*")
            return
        else:
            await self.send_message(ctx.message.channel, "Mames! O ya me descompusiste o el comando no existe, cualquiera de los dos estas bien pendejo *...mirada de estas bien pendejo*")
            return

    def run(self):
        for plugin in plugins:
            # Intentamos cargar plugins y manejamos el error de suceder, asi evitamos que se cuelgue si algun error se presenta
            try:
                self.load_extension(plugin)
                self.logger.info("{0} se ha cargado".format(plugin))
            except discord.ClientException:
                self.logger.critical("{0} no tiene una funcion de setup!".format(plugin))
            except ImportError as IE:
                self.logger.critical(IE)

        super().run(config["discord"]["token"])


if __name__ == "__main__":
    bot = Alamo()
    bot.run()