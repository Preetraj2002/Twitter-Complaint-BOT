from internetspeedtwitterbot import InternetSpeedTwitterBot

PROMISED_UP=300
PROMISED_DOWN=300

bot=InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

