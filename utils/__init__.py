import ujson
import aiohttp


# JSON con la config inicial
with open("cfg.json") as f:
    config = ujson.load(f)