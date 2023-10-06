import os
import logging
import logging.config

# Get logging configurations
logging.getLogger().setLevel(logging.ERROR)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

from pyrogram import Client
from pyromod import listen


API_ID = 10738943
API_HASH = "da61e3a08b5ac78ce28b4a4cd854aeec"
BOT_TOKEN = "6412441114:AAF5nri-Vw1kcwvMn4JT4KzXH2Fjpxv3HHA"


def main():
    app = Client(name="String Session",
                 bot_token = BOT_TOKEN,
                 api_id = API_ID,
                 api_hash = API_HASH,
                 plugins = dict(root="plugins"),
                 workers = 100,
                 sleep_threshold = 15)

    app.run()


if __name__ == "__main__":
    main()
