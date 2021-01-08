# HLL Discord Bot

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Why Heroku?

Heroku is highly recommended by many reassons. The most important is, it is really easy to deploy the bot into your own server by simply clicking a button. Also the free tier will be enought to run the bot for long time without any problem or cost for you.

I can't afford a single bot for everyone who wants to use this, because I use BattleMetrics API in order to get current players and map on your server, and this API has its own limits (requests per minute, mostly), just like Discord API limitations of renaming channel names per minute.

## Installation

1. Create a bot account to get an API key that we can use later. You can follow [this instructions](https://discordpy.readthedocs.io/en/latest/discord.html) to learn how to create one.
2. Deploy the app to Heroku (highly recommended) or any other platform that supports Python apps.
3. **OPTIONAL STEP!** If you're not deploying it to Heroku, after get the code into your platform, follow the specific platform instructions to deploy Python apps. Many of this kind of platforms should make it automatically.
4. Go to next step on configuration guide.

## Configuration guide

You will need to set some environment variables once you have deployed the bot on Heroku (highly recommended).

* `DISCORD_TOKEN`: Your Discord API token, generated when you create a bot account.
* `SERVER_ID`: ID of your server at BattleMetrics.
* `CHANNEL_ID`: Channel ID where info will be showed.

## Contributions and issues

Please leave an issue on the repo or contact me on Discord at `Ironforge#3569`.
