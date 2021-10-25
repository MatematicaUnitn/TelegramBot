import telebot
import feedparser
from datetime import date, timedelta, timezone
from time import sleep
from datetime import datetime

# Sistema il problema dei certificati
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

bot = telebot.TeleBot('2095077251:AAHSBgqqsjG23YigKDT43o-18BhDjiEj1SM')

def update_ora():
  f = open('log.txt', 'w')
  now = datetime.now(timezone.utc)
  current_time = now.strftime("%a, %d %b %Y %H:%M:%S %z")
  f.write(current_time)
  f.close()


def update(chat_id):
  with open('log.txt') as f:
      lines = f.readlines()
      last_update = datetime.strptime(lines[0], "%a, %d %b %Y %H:%M:%S %z")

  # Leggo tutti i post pubblicati su dmath e su ateneo
  feed_mate = feedparser.parse(
      "https://webmagazine.unitn.it/rss/dmath/news.xml")
  feed_ateneo = feedparser.parse(
    "https://webmagazine.unitn.it/rss/ateneo/news.xml")
  iter_mate = iter(feed_mate.entries)
  iter_ateneo = iter(feed_ateneo.entries)

  #aggiorno le news del dipartimento
  for entry in iter_mate:
    d = datetime.strptime(entry.published, "%a, %d %b %Y %H:%M:%S %z")

    #voglio stampare solo le news venute dopo l'ultimo update
    if(d >= last_update):
      mes = "#MATEMATICA" + "\n" + entry.title + \
          "\n" + entry.link + "\n" + entry.published
      bot.send_message(chat_id, mes)
      sleep(0.5)
    else:
      break

  #aggiorno le news dell'ateneo
  for entry in iter_ateneo:
    if(d >= last_update):
      mes = "#ATENEO" + "\n" + entry.title + "\n" + entry.link + "\n" + entry.published
      bot.send_message(chat_id, mes)
      sleep(0.5)
    else:
      break

  #aggiorno l'ora dell'ultimo update
  update_ora()

while True:
    update("@unitnmatematica")
    sleep(3600)
