#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K / Akshay C

# the logging things
import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)

import os, time, asyncio, json
from bot.localisation import Localisation
from bot import (
  DOWNLOAD_LOCATION
)
from bot.helper_funcs.ffmpeg import (
  convert_video,
  media_info,
  take_screen_shot
)
from bot.helper_funcs.display_progress import (
  progress_for_pyrogram,
  TimeFormatter,
  humanbytes
)

from pyrogram import (
  InlineKeyboardButton,
  InlineKeyboardMarkup
)

from bot.helper_funcs.utils import(
  delete_downloads
)
        
async def incoming_start_message_f(bot, update):
    """/start command"""
    await bot.send_message(
        chat_id=update.chat.id,
        text=Localisation.START_TEXT,
        reply_to_message_id=update.message_id
    )
    
async def incoming_compress_message_f(bot, update):
  """/compress command"""
   
  if update.reply_to_message is None:
    try:
      await bot.send_message(
        chat_id=update.chat.id,
        text="🤬 Reply to telegram media 🤬",
        reply_to_message_id=update.message_id
      )
    except:
      pass
    return
  target_percentage = 50
  isAuto = False
  
    
    
