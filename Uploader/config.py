import os

import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
        handlers=[logging.FileHandler('log.txt'),
                      logging.StreamHandler()],
                          level=logging.INFO
                          )
class Config(object):
      API_ID = int(os.environ.get("API_ID","14604313"))
      API_HASH = os.environ.get("API_HASH", "a8ee65e5057b3f05cf9f28b71667203a")
      BOT_TOKEN = os.environ.get("BOT_TOKEN", "5182948779:AAEPXYNq37qCm3pbxe-0Lhz_vSa8zvdbgKs")
   # Array to store users who are authorized to use the bot
      AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "2067727305").split())
                                            # Banned Unwanted Members..
      BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split())
                                                    # the download location, where the HTTP Server runs
      DOWNLOAD_LOCATION = "./DOWNLOADS"
                                               # Update channel for Force Subscribe
      UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "uploadeda")
                                                                    # Telegram maximum file upload size
      MAX_FILE_SIZE = 50000000
      TG_MAX_FILE_SIZE = 2097152000
      FREE_USER_MAX_FILE_SIZE = 50000000
                                                                                    # chunk size that should be used with requests
      CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
                                                                                            # default thumbnail to be used in the videos
      DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
                                                                                                    # proxy for accessing youtube-dl in GeoRestricted Areas
                                                                                                        # Get your own proxy from https://github.com/rg3/youtube-dl/issues/1091#issuecomment-230163061
      HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
                                                                                                                # https://t.me/hevcbay/951
      OUO_IO_API_KEY = ""
                                                                                                                        # maximum message length in Telegram
      MAX_MESSAGE_LENGTH = 4096
                                                                                                                                # set timeout for subprocess
      PROCESS_MAX_TIMEOUT = 3600
                                                                                                                                        # watermark file
      DEF_WATER_MARK_FILE = ""
      DATABASE_URL = os.environ.get("DATABASE_URL",  "mongodb+srv://Dhruvprajapati:dhruvp54321@cluster0.qyekq.mongodb.net/?retryWrites=true&w=majority")
      SESSION_NAME = os.environ.get("SESSION_NAME", "Rename-Bot-0")
      LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -1001691956031))
      LOGGER = logging
      OWNER_ID = int(os.environ.get("OWNER_ID", "2067727305"))
      UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "uploadeda")                                                                                                                                                                    # Update channel for Force Subscribe                                                                                                                                                               
      BOT_USERNAME = os.environ.get("BOT_USERNAME", "Urluploaderdhruv")
      PRO_USERS = list(set(int(x) for x in os.environ.get("PRO_USERS", "0").split()))
      PRO_USERS.append(OWNER_ID)
      BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
