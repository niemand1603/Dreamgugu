import discord # 導入discord模組
from discord.ext import commands # 導入discord extension的commands

# 建置bot實體
intents = discord.Intents.all() # 設定意圖(ALL全開)
bot = commands.Bot(command_prefix='+', intents=intents) # 前綴字元為'+'

# 裝飾器
@bot.event # 事件
async def on_ready(): # bot啟動時
    print("Bot 已經上線") # 在終端機印出

@bot.event # 事件
async def on_member_join(member): # 玩家加入伺服器時
    channel = bot.get_channel(1051393978555187270) # 取得特定頻道 get_channel(頻道id)
    await channel.send(f"{member}加入了") # 在該頻道傳送訊息

@bot.event # 事件
async def on_member_remove(member): # 玩家離開伺服器時
    channel = bot.get_channel(1051393978555187270) # 取得特定頻道 get_channel(頻道id)
    await channel.send(f"{member}離開了") # 在該頻道傳送訊息

@bot.command() # 指令
async def ping(ctx): # 指令為ping # context 上下文(頻道等資訊都已經包含在ctx引數中)
    await ctx.send(f"{round(bot.latency*1000)}(ms)") # latency: 延遲(單位:秒) # 1000ms=1s # round() 四捨五入到整數
     
bot.run("MTIxNjMxOTczNjQ4NTM4NDMxMg.GRIg28.lZBrmRPeRMWubpm8me9HFikWEX6odYhkXjhvDo") # 啟動bot，run()裡面放token
