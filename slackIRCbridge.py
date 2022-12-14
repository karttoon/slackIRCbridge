#! /usr/bin/env python
import irc.bot
import irc.strings
import logging, hashlib
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from slack_sdk import WebClient
from threading import Thread

__author__  = "Jeff White [karttoon] @noottrak"
__email__   = "karttoon@gmail.com"
__version__ = "1.0.1"
__date__    = "19OCT2022"

logging.basicConfig(level=logging.INFO)

# Slack
botToken = ""
appToken = ""
client = WebClient(token=botToken)
app = App(token=botToken)
slackChannel = "" 

# IRC
ircChannel = ""
ircServer = ""
ircNick = ""


class ircBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, nickname)
        self.channel = channel

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        # Send to Slack
        md5Name = hashlib.md5(e.source.nick.encode()).hexdigest()
        client.chat_postMessage(channel=slackChannel, text=f"{e.arguments[0]}", username=f"{e.source.nick}", icon_url=f"https://robohash.org/{md5Name}?size=1024x1024")
        return


@app.event("message")
def handle_message_events(body, logger):

    username = client.users_info(user=body["event"]["user"])["user"]["name"]

    # Send to IRC
    bot.connection.privmsg(ircChannel, f"<{username}>: {body['event']['text']}")
    #logger.info(body)


def main():

    logger = logging.getLogger(__name__)

    def startSlack():
        SocketModeHandler(app, appToken).start()

    def startIrc():
        global bot
        bot = ircBot(ircChannel, ircNick, ircServer, 6667)
        bot.start()

    Thread(target=startIrc).start()
    startSlack()


if __name__ == "__main__":
    main()
