# slackIRCbridge
Lightweight Slack&lt;->IRC bridge (Slack App / Single IRC Srv)

The older Slack <-> IRC bridges broke when Slack depreciated their bots for apps and I wasn't able to find a working solution out there. Since my IDIOT friends won't get off IRC I created a super lightweight and hacky bridge myself to pass messages back and forth. Nothing crazy (no error handling/etc) but does what I need it to. Uses the Python irc, slack_bolt, and slack_sdk modules.

From the Slack side, you'll need to add an app-level token for "connections:write", enable Socket Mode, enable Event Subscriptions and subscribe to "message.channels", then add the following scopes: "chat:write", "channels:read", and "users:read". There might be scopes I'm forgetting but it will yell at you telling which you're missing if you try an action it's not authorized for.

Add the "xoxb" (Bot Token) and "xapp" (App Token) to the respective fields at the top of the "slackIRCbridge.py" file. Similarily, you'll need to add the Slack channel ID (not the friendly name -> go to the Channel Details in Slack, it'll be at the bottom).

For IRC, you'll need to fill out the IRC Channel, Server, and Nick variables as well.

I don't plan to work on this anymore than I have to but may go back to the Slack API to figure out how to impersonate users so it's a little cleaner to read the incoming IRC chat.
