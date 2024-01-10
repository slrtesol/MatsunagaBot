import discord
import random
import re
import requests
import asyncio
import os
import cv2
import json
import aiohttp
import datetime
import youtube_dl
import pyautogui
import pyscreenshot
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from discord.ext import commands
from datetime import datetime
from youtubesearchpython import VideosSearch
from googletrans import Translator
from time import sleep
from datetime import datetime, timezone, timedelta
from PIL import Image
from io import BytesIO
from rembg import remove
from yt_dlp import YoutubeDL
from discord import FFmpegPCMAudio
from collections import deque
from PIL import ImageGrab
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import io
import numpy as np
import subprocess
import signal
import platform
import hashlib
from icrawler.builtin import GoogleImageCrawler
from icrawler.builtin import BingImageCrawler
from icrawler.builtin import BaiduImageCrawler

intents = discord.Intents.default()
intents.messages = True
loop_dic = {}


bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

naga_path = ['NaokiGOD.png','NaoPaisen.png','Naoki.png']

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.lower() == 'まぁつなんがぁ':
        await message.channel.send('やぁ！！')

    # メッセージがユーザーからのもので、かつ vxtwitter.com が含まれていない場合
    if message.author.bot == False and 'vxtwitter.com' not in message.content:
        # メッセージがユーザーからのもので、かつTwitterのリンクが含まれている場合
        if 'twitter.com' in message.content or 'x.com' in message.content:
            # メッセージを書き換えて対応するURLに自動補完
            corrected_message = message.content.replace('twitter.com', 'vxtwitter.com').replace('x.com', 'vxtwitter.com')
            await message.channel.send(f'リンクを補完しました: {corrected_message}')

    if message.attachments and '透過' in message.content:
        for attachment in message.attachments:
            if attachment.filename.endswith('.png') or attachment.filename.endswith('.jpg'):
                # ファイルをダウンロード
                await attachment.save('temp.jpg')
                # ファイルを読み込む
                img = cv2.imread('temp.jpg')
                # Noneチェック
                if img is None:
                    print('Failed to load image.')
                else:
                    # BGR -> RGB
                    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    # NumPy配列からPIL画像オブジェクトを生成
                    pil_image = Image.fromarray(rgb_img)
                    # アルファチャンネルを追加
                    pil_image.putalpha(255)
                    # 画像を保存
                    pil_image.save('temp.png', 'PNG')
                image_input = Image.open("temp.png")
                output = remove(image_input)
                output.save('temp.png')
                
                    # 画像を送信
                with open('temp.png', 'rb') as file:
                    picture = discord.File(file)
                    await message.channel.send(file=picture)

    if bot.user.mentioned_in(message):
        # ランダムな応答リスト
        responses = ["そうなんだね", "やるか??", "はぁ？","何してんの？","うへぇへへ","幼児てんこ盛り","ぐへぇ","ww","あざす","感謝","なんやそれ","ゆるさん","殺すぞ","あほ","まことに遺憾です","ロり最高★★"]
        response = random.choice(responses)
        await message.channel.send(response)
        
    # 特定の言葉に反応して指定された言葉を返す部分
    if message.content.lower() == 'まつなが':
        await message.channel.send('呼んだっ？！！')
    elif 'かっこいい人' in message.content:
        image_path = random.choice(naga_path)
        with open(image_path, 'rb') as file:
            picture = discord.File(file)
            await message.channel.send(file=picture)
    elif 'お腹すいた' in message.content or 'おなかすいた' in message.content or 'お腹空いた' in message.content:
        await message.channel.send('飯作りに行くわ、お前が食材な！')
    elif 'なんや' in message.content:
        await message.channel.send('なんやってなんや！')
    elif 'ｗｗｗｗｗｗｗｗｗｗ' in message.content:
        await message.channel.send('俺が一番おもろい！')
    elif 'おやすみ' in message.content:
        mention = message.author.mention  # メンションの取得
        await message.channel.send(f'{mention} さん、おやすみなさい！')
    elif '寝る' in message.content:
        mention = message.author.mention  # メンションの取得
        await message.channel.send(f'{mention} 寝ちゃうんだね、残念')
    elif 'ねる' in message.content:
        mention = message.author.mention  # メンションの取得
        await message.channel.send('ねぇるねるねるねぇー')
    elif 'しね' in message.content or 'ころす' in message.content or 'あほ' in message.content or '殺す' in message.content or '殺る' in message.content:
        mention = message.author.mention  # メンションの取得
        await message.channel.send(f'{mention} さん、それは暴言ですよ！')
    elif 'かす' in message.content or 'カス' in message.content or 'キモイ' in message.content or 'あ？' in message.content:
        mention = message.author.mention  # メンションの取得
        await message.channel.send(f'{mention} さん、それは暴言ですよ！')
    elif '問題出して' in message.content:
        q = ["我らが尊敬すべき委員長が今日最初に食べた、もしくは飲んだ物は何でしょう？","これは何と読むでしょう [温故知新]","これは何と読むでしょう [臥薪嘗胆]","これは何と読むでしょう [七転八起]","これは何と読むでしょう [群雄割拠]","これは何と読むでしょう [毀誉褒貶]","これは何と読むでしょう [虚心坦懐]","これは何と読むでしょう [初志貫徹]","これは何と読むでしょう [鶏鳴狗盗]","これは何と読むでしょう [一衣帯水]","これは何と読むでしょう [粒粒辛苦]","これは何と読むでしょう [抜山蓋世]","これは何と読むでしょう [文質彬彬]","これは何と読むでしょう [波瀾万丈]","log(x)の微分は","log(x)の積分は","sin(x)の微分は","cos(x)の微分は","4+4は","江戸幕府を開いた人は","鎌倉幕府を開いた人は"]
        resp = random.choice(q)
        await message.channel.send('答え知らないけど問題出すよ')
        await message.channel.send(resp)
    elif 'なが' in message.content:
        await message.channel.send('ながながながなが')
    elif 'なおき' in message.content:
        await message.channel.send('はいどうも、なおきです')
    elif 'ますお' in message.content:
        await message.channel.send('はいどうも、ますおです')
    elif '大晦日' in message.content or 'おおみそか' in message.content or '年末' in message.content or '正月' in message.content or '初詣' in message.content or 'はつもうで' in message.content:
        await message.channel.send('おまえ、ぼっちじゃんww')

    await bot.process_commands(message)

@bot.command(name='send',help='$send チャンネルID 送信するテキスト')
async def sendCH(ctx,send_chID : int , send_text):
    send_channel = bot.get_channel( send_chID )
    await send_channel.send(send_text)

@bot.command(name='pict', help='$pict')
async def picture(ctx):
    lines = [
        "＼(^o^)／",
        "／(^o^)＼",
        "＼(^o^)／",
        "／(^o^)＼",
        "＼(^o^)／"
    ]
    lines_2 =[
        "／(^o^)＼",
        "＼(^o^)／",
        "／(^o^)＼",
        "＼(^o^)／",
        "／(^o^)＼"
    ]
    send_mes = []

    for num in range(5):
        message = await ctx.send(f'{lines[num]}')
        send_mes.append(message)
    await asyncio.sleep(0.5)
    for time in range(9):
        if time%2 == 0:
            for num in range(5):
                await send_mes[num].edit(content=lines_2[num])
        else:
            for num in range(5):
                await send_mes[num].edit(content=lines[num])
        await asyncio.sleep(0.5)

@bot.command(name='ugg', help='$ugg チャンピオン名 モード')
async def LoLChamp(ctx, champ: str, mode: str):
    if champ == "アーゴット" or champ == "あーごっと" or champ == "Urgot" or champ == "urgot":
        champ = "urgot"
    elif champ == "アーリ" or champ == "あーり" or champ == "Ahri" or champ == "ahri":
        champ = "ahri"
    elif champ == "アイバーン" or champ == "あいばーん" or champ == "Ivern" or champ == "ivern":
        champ = "ivern"
    elif champ == "アカリ" or champ == "あかり" or champ == "Akali" or champ == "akali":
        champ = "akali"
    elif champ == "アクシャン" or champ == "あくしゃん" or champ == "Akshan" or champ == "akshan":
        champ = "akshan"
    elif champ == "アジール" or champ == "あじーる" or champ == "Azir" or champ == "azir":
        champ = "azir"
    elif champ == "アッシュ" or champ == "あっしゅ" or champ == "Ashe" or champ == "ashe":
        champ = "ashe"
    elif champ == "アニー" or champ == "あにー" or champ == "Annie" or champ == "annie":
        champ = "annie"
    elif champ == "アニビア" or champ == "あにびあ" or champ == "Anivia" or champ == "anivia":
        champ = "anivia"
    elif champ == "アフェリオス" or champ == "あふぇりおす" or champ == "Aphelios" or champ == "aphelios":
        champ = "aphelios"
    elif champ == "アムム" or champ == "あむむ" or champ == "Amumu" or champ == "amumu":
        champ = "amumu"
    elif champ == "アリスター" or champ == "ありすたー" or champ == "Alistar" or champ == "alistar":
        champ = "alistar"
    elif champ == "イブリン" or champ == "いぶりん" or champ == "Evelynn" or champ == "evelynn":
        champ = "evelynn"
    elif champ == "イラオイ" or champ == "いらおい" or champ == "Illaoi" or champ == "illaoi":
        champ = "illaoi"
    elif champ == "イレリア" or champ == "いれりあ" or champ == "Irelia" or champ == "irelia":
        champ = "irelia"
    elif champ == "ヴァイ" or champ == "ヴぁい" or champ == "Vi" or champ == "vi":
        champ = "vi"
    elif champ == "ヴァルス" or champ == "ヴぁるす" or champ == "Varus" or champ == "varus":
        champ = "varus"
    elif champ == "ヴィエゴ" or champ == "ヴぃえご" or champ == "Viego" or champ == "viego":
        champ = "viego"
    elif champ == "ウーコン" or champ == "うーこん" or champ == "Wukong" or champ == "wukong":
        champ = "wukong"
    elif champ == "ヴェイン" or champ == "ヴぇいん" or champ == "ベイン" or champ == "べいん" or champ == "Vayne" or champ == "vayne":
        champ = "vayne"
    elif champ == "ヴェックス" or champ == "ヴぇっくす" or champ == "ベックス" or champ == "べっくす" or champ == "Vex" or champ == "vex":
        champ = "vex"
    elif champ == "ヴェルコズ" or champ == "ヴぇるこず" or champ == "ヴェル＝コズ" or champ == "ヴぇる＝こず" or champ == "ベルコズ" or champ == "べるこず" or champ == "ベル＝コズ" or champ == "べる＝こず" or champ == "Vel'Koz" or champ == "velkoz":
        champ = "velkoz"
    elif champ == "ウディア" or champ == "うでぃあ" or champ == "Udyr" or champ == "udyr":
        champ = "udyr"
    elif champ == "エイトロックス" or champ == "えいとろっくす" or champ == "Aatrox" or champ == "aatrox":
        champ = "aatrox"
    elif champ == "エコー" or champ == "えこー" or champ == "Ekko" or champ == "ekko":
        champ = "ekko"
    elif champ == "エズリアル" or champ == "えずりある" or champ == "Ezreal" or champ == "ezreal":
        champ = "ezreal"
    elif champ == "エリス" or champ == "えりす" or champ == "Elise" or champ == "elise":
        champ = "elise"
    elif champ == "オーン" or champ == "おーん" or champ == "Ornn" or champ == "ornn":
        champ = "ornn"
    elif champ == "オラフ" or champ == "おらふ" or champ == "Olaf" or champ == "olaf":
        champ = "olaf"
    elif champ == "オリアナ" or champ == "おりあな" or champ == "Orianna" or champ == "orianna":
        champ = "orianna"
    elif champ == "オレリオンソル" or champ == "おれりおんそる" or champ == "オレリオン・ソル" or champ == "おれりおん・そる" or champ == "AurelionSol" or champ == "aurelionsol":
        champ = "aurelionsol"
    elif champ == "カサンテ" or champ == "かさんて" or champ == "カ・サンテ" or champ == "か・さんて" or champ == "K'Sante" or champ == "ksante":
        champ = "ksante"
    elif champ == "カジックス" or champ == "かじっくす" or champ == "カージックス" or champ == "かーじっくす" or champ == "カ＝ジックス" or champ == "か＝じっくす" or champ == "Kha'Zix" or champ == "khazix":
        champ = "khazix"
    elif champ == "カーサス" or champ == "かーさす" or champ == "Karthus" or champ == "karthus":
        champ = "karthus"
    elif champ == "カイサ" or champ == "かいさ" or champ == "カイーサ" or champ == "かいーさ" or champ == "カイ＝サ" or champ == "かい＝さ" or champ == "Kai'Sa" or champ == "kaisa":
        champ = "kaisa"
    elif champ == "カサディン" or champ == "かさでぃん" or champ == "Kassadin" or champ == "kassadin":
        champ = "kassadin"
    elif champ == "カシオペア" or champ == "かしおぺあ" or champ == "Cassiopeia" or champ == "cassiopeia":
        champ = "cassiopeia"
    elif champ == "カタリナ" or champ == "かたりな" or champ == "Katarina" or champ == "katarina":
        champ = "katarina"
    elif champ == "カミール" or champ == "かみーる" or champ == "Camille" or champ == "camille":
        champ = "camille"
    elif champ == "ガリオ" or champ == "がりお" or champ == "Galio" or champ == "galio":
        champ = "galio"
    elif champ == "カリスタ" or champ == "かりすた" or champ == "Kalista" or champ == "kalista":
        champ = "kalista"
    elif champ == "カルマ" or champ == "かるま" or champ == "Karma" or champ == "karma":
        champ = "karma"
    elif champ == "ガレン" or champ == "がれん" or champ == "Garen" or champ == "garen":
        champ = "garen"
    elif champ == "ガングプランク" or champ == "がんぐぷらんく" or champ == "Gangplank" or champ == "gangplank":
        champ = "gangplank"
    elif champ == "キヤナ" or champ == "きやな" or champ == "Qiyana" or champ == "qiyana":
        champ = "qiyana"
    elif champ == "キンドレッド" or champ == "きんどれっど" or champ == "Kindred" or champ == "kindred":
        champ = "kindred"
    elif champ == "クイン" or champ == "くいん" or champ == "Quinn" or champ == "quinn":
        champ = "quinn"
    elif champ == "グウェン" or champ == "ぐうぇん" or champ == "Gwen" or champ == "gwen":
        champ = "gwen"
    elif champ == "グラガス" or champ == "ぐらがす" or champ == "Gragas" or champ == "gragas":
        champ = "gragas"
    elif champ == "グレイブス" or champ == "ぐれいぶす" or champ == "Graves" or champ == "graves":
        champ = "graves"
    elif champ == "クレッド" or champ == "くれっど" or champ == "Kled" or champ == "kled":
        champ = "kled"
    elif champ == "ケイトリン" or champ == "けいとりん" or champ == "Caitlyn" or champ == "caitlyn":
        champ = "caitlyn"
    elif champ == "ケイル" or champ == "けいる" or champ == "Kayle" or champ == "kayle":
        champ = "kayle"
    elif champ == "ケイン" or champ == "けいん" or champ == "Kayn" or champ == "kayn":
        champ = "kayn"
    elif champ == "ケネン" or champ == "けねん" or champ == "Kennen" or champ == "kennen":
        champ = "kennen"
    elif champ == "コーキ" or champ == "こーき" or champ == "Corki" or champ == "corki":
        champ = "corki"
    elif champ == "コグマウ" or champ == "こぐまう" or champ == "コグ＝マウ" or champ == "こぐ＝まう" or champ == "Kog'Maw" or champ == "kogmaw":
        champ = "kogmaw"
    elif champ == "サイオン" or champ == "さいおん" or champ == "Sion" or champ == "sion":
        champ = "sion"
    elif champ == "ザイラ" or champ == "ざいら" or champ == "Zyra" or champ == "zyra":
        champ = "zyra"
    elif champ == "サイラス" or champ == "さいらす" or champ == "Sylas" or champ == "sylas":
        champ = "sylas"
    elif champ == "ザック" or champ == "ざっく" or champ == "Zac" or champ == "zac":
        champ = "zac"
    elif champ == "サミーラ" or champ == "さみーら" or champ == "Samira" or champ == "samira":
        champ = "samira"
    elif champ == "ザヤ" or champ == "ざや" or champ == "Xayah" or champ == "xayah":
        champ = "xayah"
    elif champ == "シヴァーナ" or champ == "しヴぁーな" or champ == "シバーナ" or champ == "しばーな" or champ == "Shyvana" or champ == "shyvana":
        champ = "shyvana"
    elif champ == "シヴィア" or champ == "しヴぃあ" or champ == "シビア" or champ == "しびあ" or champ == "Sivir" or champ == "sivir":
        champ = "sivir"
    elif champ == "ジェイス" or champ == "じぇいす" or champ == "Jayce" or champ == "jayce":
        champ = "jayce"
    elif champ == "シェン" or champ == "しぇん" or champ == "Shen" or champ == "shen":
        champ = "shen"
    elif champ == "ジグス" or champ == "じぐす" or champ == "Ziggs" or champ == "ziggs":
        champ = "ziggs"
    elif champ == "ジャーヴァンⅣ" or champ == "じゃーヴぁんⅣ" or champ == "ジャーヴァン" or champ == "じゃーヴぁん" or champ == "JarvanIV" or champ == "jarvaniv":
        champ = "jarvaniv"
    elif champ == "シャコ" or champ == "しゃこ" or champ == "Shaco" or champ == "shaco":
        champ = "shaco"
    elif champ == "ジャックス" or champ == "じゃっくす" or champ == "Jax" or champ == "jax":
        champ = "jax"
    elif champ == "ジャンナ" or champ == "じゃんな" or champ == "Janna" or champ == "janna":
        champ = "janna"
    elif champ == "ジリアン" or champ == "じりあん" or champ == "Zilean" or champ == "zilean":
        champ = "zilean"
    elif champ == "ジン" or champ == "じん" or champ == "Jhin" or champ == "jhin":
        champ = "jhin"
    elif champ == "シンジャオ" or champ == "しんじゃお" or champ == "シン・ジャオ" or champ == "しん・じゃお" or champ == "XinZhao" or champ == "xinzhao":
        champ = "xinzhao"
    elif champ == "ジンクス" or champ == "じんくす" or champ == "Jinx" or champ == "jinx":
        champ = "jinx"
    elif champ == "シンジド" or champ == "しんじど" or champ == "Singed" or champ == "singed":
        champ = "singed"
    elif champ == "シンドラ" or champ == "しんどら" or champ == "Syndra" or champ == "syndra":
        champ = "syndra"
    elif champ == "スウェイン" or champ == "すうぇいん" or champ == "Swain" or champ == "swain":
        champ = "swain"
    elif champ == "スカーナー" or champ == "すかーなー" or champ == "Skarner" or champ == "skarner":
        champ = "skarner"
    elif champ == "スレッシュ" or champ == "すれっしゅ" or champ == "Thresh" or champ == "thresh":
        champ = "thresh"
    elif champ == "セジュアニ" or champ == "せじゅあに" or champ == "Sejuani" or champ == "sejuani":
        champ = "sejuani"
    elif champ == "セト" or champ == "せと" or champ == "Sett" or champ == "sett":
        champ = "sett"
    elif champ == "ゼド" or champ == "ぜど" or champ == "Zed" or champ == "zed":
        champ = "zed"
    elif champ == "セナ" or champ == "せな" or champ == "Senna" or champ == "senna":
        champ = "senna"
    elif champ == "ゼラス" or champ == "ぜらす" or champ == "Xerath" or champ == "xerath":
        champ = "xerath"
    elif champ == "セラフィーン" or champ == "せらふぃーん" or champ == "Seraphine" or champ == "seraphine":
        champ = "seraphine"
    elif champ == "ゼリ" or champ == "ぜり" or champ == "Zeri" or champ == "zeri":
        champ = "zeri"
    elif champ == "ゾーイ" or champ == "ぞーい" or champ == "Zoe" or champ == "zoe":
        champ = "zoe"
    elif champ == "ソナ" or champ == "そな" or champ == "Sona" or champ == "sona":
        champ = "sona"
    elif champ == "ソラカ" or champ == "そらか" or champ == "Soraka" or champ == "soraka":
        champ = "soraka"
    elif champ == "ダイアナ" or champ == "だいあな" or champ == "Diana" or champ == "diana":
        champ = "diana"
    elif champ == "タムケンチ" or champ == "たむけんち" or champ == "タム・ケンチ" or champ == "たむ・けんち" or champ == "TahmKench" or champ == "tahmkench":
        champ = "tahmkench"
    elif champ == "ダリウス" or champ == "だりうす" or champ == "Darius" or champ == "darius":
        champ = "darius"
    elif champ == "タリック" or champ == "たりっく" or champ == "Taric" or champ == "taric":
        champ = "taric"
    elif champ == "タリヤ" or champ == "たりや" or champ == "Taliyah" or champ == "taliyah":
        champ = "taliyah"
    elif champ == "タロン" or champ == "たろん" or champ == "Talon" or champ == "talon":
        champ = "talon"
    elif champ == "チョガス" or champ == "ちょがす" or champ == "チョ＝ガス" or champ == "ちょ＝がす" or champ == "Cho'Gath" or champ == "chogath":
        champ = "chogath"
    elif champ == "ツイステッドフェイト" or champ == "ついすてっどふぇいと" or champ == "ツイステッド・フェイト" or champ == "ついすてっど・ふぇいと" or champ == "TwistedFate" or champ == "twistedfate":
        champ = "twistedfate"
    elif champ == "ティーモ" or champ == "てぃーも" or champ == "Teemo" or champ == "teemo":
        champ = "teemo"
    elif champ == "トゥイッチ" or champ == "とぅいっち" or champ == "ツイッチ" or champ == "ついっち" or champ == "Twitch" or champ == "twitch":
        champ = "twitch"
    elif champ == "ドクタームンド" or champ == "どくたーむんど" or champ == "ドクター・ムンド" or champ == "どくたー・むんど" or champ == "Dr.Mundo" or champ == "drmundo":
        champ = "drmundo"
    elif champ == "トランドル" or champ == "とらんどる" or champ == "Trundle" or champ == "trundle":
        champ = "trundle"
    elif champ == "トリスターナ" or champ == "とりすたーな" or champ == "Tristana" or champ == "tristana":
        champ = "tristana"
    elif champ == "トリンダメア" or champ == "とりんだめあ" or champ == "Tryndamere" or champ == "tryndamere":
        champ = "tryndamere"
    elif champ == "ドレイブン" or champ == "どれいぶん" or champ == "Draven" or champ == "draven":
        champ = "draven"
    elif champ == "ナー" or champ == "なー" or champ == "Gnar" or champ == "gnar":
        champ = "gnar"
    elif champ == "ナサス" or champ == "なさす" or champ == "Nasus" or champ == "nasus":
        champ = "nasus"
    elif champ == "ナフィーリ" or champ == "なふぃーり" or champ == "Naafiri" or champ == "naafiri":
        champ = "naafiri"
    elif champ == "ナミ" or champ == "なみ" or champ == "Nami" or champ == "nami":
        champ = "nami"
    elif champ == "ニーコ" or champ == "にーこ" or champ == "Neeko" or champ == "neeko":
        champ = "neeko"
    elif champ == "ニーラ" or champ == "にーら" or champ == "Nilah" or champ == "nilah":
        champ = "nilah"
    elif champ == "ニダリー" or champ == "にだりー" or champ == "Nidalee" or champ == "nidalee":
        champ = "nidalee"
    elif champ == "ヌヌ＆ウィルンプ" or champ == "ぬぬ＆うぃるんぷ" or champ == "ヌヌ" or champ == "ぬぬ" or champ == "Nunu&Willump" or champ == "nunu":
        champ = "nunu"
    elif champ == "ノーチラス" or champ == "のーちらす" or champ == "Nautilus" or champ == "nautilus":
        champ = "nautilus"
    elif champ == "ノクターン" or champ == "のくたーん" or champ == "Nocturne" or champ == "nocturne":
        champ = "nocturne"
    elif champ == "バード" or champ == "ばーど" or champ == "Bard" or champ == "bard":
        champ = "bard"
    elif champ == "パイク" or champ == "ぱいく" or champ == "Pyke" or champ == "pyke":
        champ = "pyke"
    elif champ == "ハイマーディンガー" or champ == "はいまーでぃんがー" or champ == "Heimerdinger" or champ == "heimerdinger":
        champ = "heimerdinger"
    elif champ == "パンテオン" or champ == "ぱんておん" or champ == "Pantheon" or champ == "pantheon":
        champ = "pantheon"
    elif champ == "ビクター" or champ == "びくたー" or champ == "Viktor" or champ == "viktor":
        champ = "viktor"
    elif champ == "フィオラ" or champ == "ふぃおら" or champ == "Fiora" or champ == "fiora":
        champ = "fiora"
    elif champ == "フィズ" or champ == "ふぃず" or champ == "Fizz" or champ == "fizz":
        champ = "fizz"
    elif champ == "フィドルスティックス" or champ == "ふぃどるすてぃっくす" or champ == "Fiddlesticks" or champ == "fiddlesticks":
        champ = "fiddlesticks"
    elif champ == "フェイ" or champ == "ふぇい" or champ == "Hwei" or champ == "hwei":
        champ = "hwei"
    elif champ == "ブライアー" or champ == "ブライアー" or champ == "Briar" or champ == "briar":
        champ = "briar"
    elif champ == "ブラウム" or champ == "ぶらうむ" or champ == "Braum" or champ == "braum":
        champ = "braum"
    elif champ == "ブラッドミア" or champ == "ぶらっどみあ" or champ == "vladimir" or champ == "vladimir":
        champ = "vladimir"
    elif champ == "ブランド" or champ == "ぶらんど" or champ == "Brand" or champ == "brand":
        champ = "brand"
    elif champ == "ブリッツクランク" or champ == "ぶりっつくらんく" or champ == "Blitzcrank" or champ == "blitzcrank":
        champ = "blitzcrank"
    elif champ == "ベイガー" or champ == "べいがー" or champ == "veigar" or champ == "veigar":
        champ = "veigar"
    elif champ == "ヘカリム" or champ == "へかりむ" or champ == "hecarim" or champ == "hecarim":
        champ = "hecarim"
    elif champ == "ベルヴェス" or champ == "べるヴぇす" or champ == "ベル＝ヴェス" or champ == "べる＝ヴぇす" or champ == "ベルベス" or champ == "べるべす" or champ == "ベル＝ベス" or champ == "べる＝べす" or champ == "Bel'Veth" or champ == "belveth":
        champ = "belveth"
    elif champ == "ポッピー" or champ == "ぽっぴー" or champ == "Poppy" or champ == "poppy":
        champ = "poppy"
    elif champ == "ボリベア" or champ == "ぼりべあ" or champ == "Volibear" or champ == "volibear":
        champ = "volibear"
    elif champ == "マオカイ" or champ == "まおかい" or champ == "Maokai" or champ == "maokai":
        champ = "maokai"
    elif champ == "マスターイー" or champ == "ますたーいー" or champ == "マスター・イー" or champ == "ますたー・いー" or champ == "MasterYi" or champ == "masteryi":
        champ = "masteryi"
    elif champ == "マルザハール" or champ == "まるざはーる" or champ == "Malzahar" or champ == "malzahar":
        champ = "malzahar"
    elif champ == "マルファイト" or champ == "まるふぁいと" or champ == "Malphite" or champ == "malphite":
        champ = "malphite"
    elif champ == "ミスフォーチュン" or champ == "みすふぉーちゅん" or champ == "ミス・フォーチュン" or champ == "みす・ふぉーちゅん" or champ == "MissFortune" or champ == "missfortune":
        champ = "missfortune"
    elif champ == "ミリオ" or champ == "みりお" or champ == "Milio" or champ == "milio":
        champ = "milio"
    elif champ == "モルガナ" or champ == "もるがな" or champ == "Morgana" or champ == "morgana":
        champ = "morgana"
    elif champ == "モルデカイザー" or champ == "もるでかいざー" or champ == "Mordekaiser" or champ == "mordekaiser":
        champ = "mordekaiser"
    elif champ == "ヤスオ" or champ == "やすお" or champ == "Yasuo" or champ == "yasuo":
        champ = "yasuo"
    elif champ == "ユーミ" or champ == "ゆーみ" or champ == "Yuumi" or champ == "yuumi":
        champ = "yuumi"
    elif champ == "ヨネ" or champ == "よね" or champ == "Yone" or champ == "yone":
        champ = "yone"
    elif champ == "ヨリック" or champ == "よりっく" or champ == "Yorick" or champ == "yorick":
        champ = "yorick"
    elif champ == "ライズ" or champ == "らいず" or champ == "Ryze" or champ == "ryze":
        champ = "ryze"
    elif champ == "ラカン" or champ == "らかん" or champ == "Rakan" or champ == "rakan":
        champ = "rakan"
    elif champ == "ラックス" or champ == "らっくす" or champ == "Lux" or champ == "lux":
        champ = "lux"
    elif champ == "ラムス" or champ == "らむす" or champ == "Rammus" or champ == "rammus":
        champ = "rammus"
    elif champ == "ランブル" or champ == "らんぶる" or champ == "Rumble" or champ == "rumble":
        champ = "rumble"
    elif champ == "リーシン" or champ == "りーしん" or champ == "リー・シン" or champ == "りー・しん" or champ == "LeeSin" or champ == "leesin":
        champ = "leesin"
    elif champ == "リヴェン" or champ == "りヴぇん" or champ == "リベン" or champ == "りべん" or champ == "Riven" or champ == "riven":
        champ = "riven"
    elif champ == "リサンドラ" or champ == "りさんどら" or champ == "Lissandra" or champ == "lissandra":
        champ = "lissandra"
    elif champ == "リリア" or champ == "りりあ" or champ == "Lillia" or champ == "lillia":
        champ = "lillia"
    elif champ == "ルシアン" or champ == "るしあん" or champ == "Lucian" or champ == "lucian":
        champ = "lucian"
    elif champ == "ルブラン" or champ == "るぶらん" or champ == "Leblanc" or champ == "leblanc":
        champ = "leblanc"
    elif champ == "ルル" or champ == "るる" or champ == "Lulu" or champ == "lulu":
        champ = "lulu"
    elif champ == "レオナ" or champ == "れおな" or champ == "Leona" or champ == "leona":
        champ = "leona"
    elif champ == "レクサイ" or champ == "れくさい" or champ == "レク＝サイ" or champ == "れく＝さい" or champ == "Rek'Sai" or champ == "reksai":
        champ = "reksai"
    elif champ == "レナータグラスク" or champ == "れなーたぐらすく" or champ == "レナータ・グラスク" or champ == "れなーた・ぐらすく" or champ == "RenataGlasc" or champ == "renata":
        champ = "renata"
    elif champ == "レネクトン" or champ == "れねくとん" or champ == "Renekton" or champ == "renekton":
        champ = "renekton"
    elif champ == "レル" or champ == "れる" or champ == "Rell" or champ == "rell":
        champ = "rell"
    elif champ == "レンガー" or champ == "れんがー" or champ == "Rengar" or champ == "rengar":
        champ = "rengar"
    elif champ == "ワーウィック" or champ == "わーうぃっく" or champ == "Warwick" or champ == "warwick":
        champ = "warwick"
    else:
        await ctx.send("チャンピオン名が違うよ\n正しく入力してね")
        return

    await LoLSS(ctx,champ,mode)

async def LoLSS(ctx, url: str, modes: str):
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.page_load_strategy = 'normal'
    options.add_argument("--window-size=1920,1080")
    if modes == "rune" or modes == "ルーン":
        URL = "https://u.gg/lol/champions/" + url + "/runes"
        atb = 'content-section_content'
        CLCS = "class"
    elif modes == "counter" or modes == "カウンター":
        URL = "https://u.gg/lol/champions/" + url + "/counter"
        options.add_argument("--window-size=1920,2160")
        atb = 'champion-profile-content-container'
        CLCS = "class"
    elif modes == "build" or modes == "ビルド":
        URL = "https://u.gg/lol/champions/" + url + "/build"
        options.add_argument("--window-size=1920,2160")
        atb = 'content-section content-section_no-padding recommended-build_items media-query media-query_TABLET__DESKTOP_SMALL'
        CLCS = "css"
    elif modes == "aram" or modes == "らんみ" or modes == "ランミ" or modes == "ランダムミッド":
        URL = "https://u.gg/lol/champions/aram/" + url + "-aram"
        options.add_argument("--window-size=1920,2160")
        atb = 'champion-profile-content-container'
        CLCS = "class"
    else:
        await ctx.send("調べるモードが違うよ\nrune ルーン\ncounter カウンター\nbuild ビルド\naram らんみ ランミ ランダムミッド  です")
        return
    await ctx.send("検索中です..\n10秒弱かかることもあります\n")
    driver = webdriver.Chrome(service=webdriver.ChromeService(executable_path=ChromeDriverManager().install()),options=options)
    driver.get(URL)
    while True:
        element = None
        try:
            if CLCS == "class":
                element = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.CLASS_NAME, atb))
                )
        except:
            pass
        if CLCS == "css":
            loop = asyncio.get_event_loop()
            driver.save_screenshot("LoLSS.png")
            im = Image.open('LoLSS.png')
            width, height = im.size
            bottom_half = im.crop((0, height/2, width, height))
            bottom_half.save('LoLSS_bottom_half.png')
            cropped_bottom_half = bottom_half.crop((303, 85, 1318, 528)) # ここでは左上から右下までを切り出します
            cropped_bottom_half.save('LoLSS_bottom_half_cropped.png')
            await ctx.send(file=discord.File("LoLSS_bottom_half_cropped.png"))
        elif CLCS == "class":
            if element == None:
                continue
            # スクリーンショットを同期に撮る
            element.screenshot("LoLSS.png")
            await ctx.send(file=discord.File("LoLSS.png"))
        break
    driver.quit()

@bot.command(name='timeNow', help='$timeNow')
async def current_time(ctx):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'現在の時刻は {current_datetime} だぜ。')

@bot.command(name='rand', help='$rand 最小値 最大値')
async def generate_random(ctx, min_value: int, max_value: int):
    if min_value >= max_value:
        await ctx.send("最小値は最大値より小さい必要があるんだなぁこれが")
        return
    random_number = random.randint(min_value, max_value)
    await ctx.send(f'生成された乱数: {random_number}')

@bot.command(name='searchYT', help='$searchYT 検索ワード')
async def search_youtube(ctx, *query):
    search_query = ' '.join(query)
    videos_search = VideosSearch(search_query, limit=1)
    if videos_search.result() and videos_search.result()['result']:
        video_url = videos_search.result()['result'][0]['link']
        await ctx.send(f'検索結果: {video_url}')
    else:
        await ctx.send('該当する動画が見つかりませんでした。')

@bot.command(name='Enzan', help='$Enzan 第一数 演算子 第二数')
async def calculate(ctx, num1: float, operator: str, num2: float):
    result = None
    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            await ctx.send("ゼロはすべてを壊す★★")
            return
    else:
        await ctx.send("演算子が違うよ。 +, -, *, / こいつらを使ってね")
        return

    await ctx.send(f'答えは: {result} なり')

@bot.command(name='weather', help='$weather')
async def get_weather(ctx):
    city_name = '大阪'
    xml_url = 'https://weather.tsukumijima.net/primary_area.xml'
    base_url = 'https://weather.tsukumijima.net/api/forecast/'
    xml_file = requests.get(xml_url).text
    root = ET.fromstring(xml_file)
    city_id_dict={}
    for value in root.iter('city'):
        city_id_dict[value.attrib['title']] = value.attrib['id']
    json_file = requests.get(os.path.join(base_url,'city/',city_id_dict[city_name])).json()
    await ctx.send(city_name + 'の今日の天気は' + json_file['forecasts'][0]['telop'] + 'です.')
    await ctx.send(json_file['description']['text'])

@bot.command(name='count', help='$count 数値')
async def countdown(ctx, start_count: int):
    if start_count <= 0:
        await ctx.send("カウントの初期値には正の整数を入れてね!!")
        return
    message = await ctx.send(f"カウントダウン: {start_count}")
    for i in range(start_count - 1, 0, -1):
        await asyncio.sleep(1)  # Wait for 1 second
        await message.edit(content=f"カウントダウン: {i}")
    await asyncio.sleep(1)
    await message.edit(content="終了!")

# カウントアップのための非同期タスク
async def count_up_task(ctx):
    count = 0
    message = await ctx.send(f"Count: {count}")
    while True:
        await asyncio.sleep(1)
        count += 1
        await message.edit(content=f"Count: {count}")

@bot.command(name='Cstart', help='$Cstart')
async def count_up_start(ctx):
    task = bot.loop.create_task(count_up_task(ctx))
    ctx.bot.count_up_task = task

@bot.command(name='Cstop', help='$Cstop')
async def count_up_stop(ctx):
    if hasattr(ctx.bot, 'count_up_task') and ctx.bot.count_up_task:
        ctx.bot.count_up_task.cancel()
        await ctx.send("止めてやったぜ★")
    else:
        await ctx.send("カウントなんてされてなかった★")

@bot.command(name='wiki', help='$wiki 検索ワード')
async def web_text(ctx, url):
    try:
        urls = 'https://ja.wikipedia.org/wiki/'+ url
        response = requests.get(urls)
        response.raise_for_status()  # エラーチェック
        soup = BeautifulSoup(response.text, 'html.parser')
        first_paragraph = soup.find('p').text
        if len(first_paragraph) >= 100:
            await ctx.send(f'**{url}**\n\n{first_paragraph}')
        else:
            additional_text = soup.find('p', string=lambda x: x and len(x) > 100)
            if additional_text:
                additional_text = additional_text.text[:400]  # 適切な文字数に調整
                await ctx.send(f'**{url}**\n\n{first_paragraph}{additional_text}...')
            else:
                await ctx.send(f'**{url}**\n\n{first_paragraph}')
    except Exception as e:
        print(e)
        await ctx.send("ウェブページの取得に失敗しました。")

@bot.command(name='trans', help='$trans 翻訳前の言語(元の言語) 翻訳後の言語 翻訳する言葉 ')
async def web_text(ctx, t1,t2, text):
    def translate_text(text, target_language=t2):
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text
    text_to_translate = text
    target_language = t2  # 翻訳先の言語コード（日本語の場合は'ja'）
    translation_result = translate_text(text_to_translate, target_language)
    if   t1 == 'en'    :trans1 = '英語'
    elif t1 == 'ja'    :trans1 = '日本語'
    elif t1 == 'zh-CH' :trans1 = '中国語（簡体字）'
    elif t1 == 'zh-TW' :trans1 = '中国語（繁体字）'
    elif t1 == 'de'    :trans1 = 'ドイツ語'
    elif t1 == 'fr'    :trans1 = 'フランス語'
    elif t1 == 'es'    :trans1 = 'スペイン語'
    elif t1 == 'it'    :trans1 = 'イタリア語'
    elif t1 == 'ru'    :trans1 = 'ロシア語'
    elif t1 == 'ar'    :trans1 = 'アラビア語'
    elif t1 == 'pt'    :trans1 = 'ポルトガル語'
    elif t1 == 'hi'    :trans1 = 'ヒンドゥー語'
    elif t1 == 'ko'    :trans1 = '韓国語'
    elif t1 == 'tr'    :trans1 = 'トルコ語'
    if   t2 == 'en'    :trans2 = '英語'
    elif t2 == 'ja'    :trans2 = '日本語'
    elif t2 == 'zh-CH' :trans2 = '中国語（簡体字）'
    elif t2 == 'zh-TW' :trans2 = '中国語（繁体字）'
    elif t2 == 'de'    :trans2 = 'ドイツ語'
    elif t2 == 'fr'    :trans2 = 'フランス語'
    elif t2 == 'es'    :trans2 = 'スペイン語'
    elif t2 == 'it'    :trans2 = 'イタリア語'
    elif t2 == 'ru'    :trans2 = 'ロシア語'
    elif t2 == 'ar'    :trans2 = 'アラビア語'
    elif t2 == 'pt'    :trans2 = 'ポルトガル語'
    elif t2 == 'hi'    :trans2 = 'ヒンドゥー語'
    elif t2 == 'ko'    :trans2 = '韓国語'
    elif t2 == 'tr'    :trans2 = 'トルコ語'
    await ctx.send(f'翻訳言語: {trans1} 翻訳前: {text_to_translate}\n翻訳言語: {trans2} 翻訳後: {translation_result}')
    await ctx.send(f'{text_to_translate} \t=>\t {translation_result}')

@bot.command(name='Tsplit', help='$Tsplit メンバーの名前(メンバーごとに , で区切る) 一チーム当たりの人数')
async def command_script(ctx, pNames,value :int):
    strings = pNames.split(',')
    shuffled_strings = random.sample(strings, len(strings))
    groups = [shuffled_strings[i:i+value] for i in range(0, len(shuffled_strings), value)]
    for index, group in enumerate(groups, start=1):
        group_text = ', '.join(group)
        await ctx.send(f'グループ {index}: {group_text}')

@bot.command(name='weekday', help='$weekday 年 月 日')
async def command_weekday(ctx, year: int, month: int, day: int):
    try:
        target_date = datetime(year, month, day).date()
        weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
        weekday_index = target_date.weekday()
        await ctx.send(f"{target_date.year}年{target_date.month}月{target_date.day}日は{weekdays[weekday_index]}です。")
    except Exception as e:
        print(e)
        await ctx.send("曜日の取得に失敗しました。")

@bot.event
async def on_command_error(ctx, error):
    log_channel = bot.get_channel(1183064807490986085)  # ログを残すチャンネルのID testサーバーのlogチャンネル
    user = ctx.author
    # 現在の時刻をUTCで取得
    current_time_utc = datetime.utcnow()
    # JST (日本標準時) に変換
    jst = timezone(timedelta(hours=9))
    current_time_jst = current_time_utc.replace(tzinfo=timezone.utc).astimezone(jst)
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("コマンドが見つかりません。\n正しいコマンドを打ってくれ")
        await log_channel.send(f"[{current_time_jst}] コマンドが見つかりません。\n発生したユーザー: {user.name}")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("引数が不足しています。正しい構文を確認してください。\nスペルミスとか空白抜け、引数不足。\n全て人間のバグのせい")
        await log_channel.send(f"[{current_time_jst}] 引数が不足しています。正しい構文を確認してください。\n発生したユーザー: {user.name}")
    else:
        await ctx.send(f"エラーが発生しました\n君は間違えを犯した。理由はこれだ: {error}")
        await log_channel.send(f"[{current_time_jst}] エラーが発生しました: {error}\n発生したユーザー: {user.name}")

async def on_ready():
    log_channel = bot.get_channel(1183064807490986085)  # ログを残すチャンネルのID testサーバーのlogチャンネル
    await log_channel.send(f'{bot.user.name}がログインしました')


async def play_song(ctx,url):
    loop_task = asyncio.get_event_loop()
    ydl_video_opts = {
        'outtmpl': f"{str(ctx.guild.id)}.mp3",
        'format': 'bestaudio'
    }
    if os.path.isfile(f"./{str(ctx.guild.id)}.mp3"):
        os.remove(f"./{str(ctx.guild.id)}.mp3")
    YoutubeDL(ydl_video_opts).download([url])
    ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(source=f"{str(ctx.guild.id)}.mp3")), after=lambda _: loop_task.create_task(play_song(ctx,url)) if loop_dic[str(ctx.guild.id)] else None)

@bot.command(name='join', help='$join  *非推奨')
async def join(ctx, *, channel: discord.VoiceChannel):
    if ctx.voice_client is not None:
        return await ctx.voice_client.move_to(channel)
    await channel.connect()

@bot.command(name='play', help='$play YouTubeの動画のURL')
async def play(ctx, url):
    async with ctx.typing():
        await play_song(ctx,url)
        loop_dic[str(ctx.guild.id)] = False
    await ctx.send('再生中')

@bot.command(name='loop', help='$loop')
async def loop(ctx):
    if loop_dic[str(ctx.guild.id)]:
        loop_dic[str(ctx.guild.id)] = False
    else:
        loop_dic[str(ctx.guild.id)] = True
    await ctx.send("ループチェンジ {}".format(loop_dic[str(ctx.guild.id)]))

@bot.command(name='volume', help='$volume 数値(整数型のみ)')
async def volume(ctx, volume: int):
    if ctx.voice_client is None:
        return await ctx.send("ボットがボイスチャンネルにいないようだ")
    ctx.voice_client.source.volume = volume / 100
    await ctx.send("音声を {}% に変更したぜ".format(volume))

@bot.command(name='stop', help='$stop')
async def stop(ctx):
    await ctx.voice_client.disconnect()
    if str(ctx.guild.id) in loop_dic:
        del loop_dic[str(ctx.guild.id)]

@play.before_invoke
async def ensure_voice(ctx):
    if ctx.voice_client is None:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            await ctx.send("通話入っとけよ")
            raise commands.CommandError(
                    "Author not connected to a voice channel.")
    elif ctx.voice_client.is_playing():
        ctx.voice_client.stop()

@bot.listen()
async def on_voice_state_update(member, before, after):
    voice_state = member.guild.voice_client
    if voice_state is None:
        return
    if len(voice_state.channel.members) == 1:
        await voice_state.disconnect()


bat_exe = None
@bot.command(name='Save', help='$Save これにテキストまたはpythonファイルを添付')
async def run_command(ctx):
    exe_path = os.path.join('dist', 'rentalBot1.exe')
    if os.path.exists(exe_path):
        os.remove(exe_path)
        await ctx.send('既存の rentalBot1.exe を削除しました。')
    if not ctx.message.attachments:
        return await ctx.send('ファイルが添付されていません。')

    attachment = ctx.message.attachments[0]
    # 拡張子を取得
    _, file_extension = os.path.splitext(attachment.filename)
    # サポートされていないファイル形式か確認
    if file_extension.lower() not in ['.txt', '.py']:
        return await ctx.send('サポートされていないファイル形式です。.txtか.pyファイルを添付してください。')
    # もし.pyファイルならrentalBot1.pyを削除
    if file_extension.lower() == '.py' and os.path.exists('rentalBot1.py'):
        os.remove('rentalBot1.py')
    # もし.txtファイルならrentalBot1.pyを削除し、.pyに変更して保存
    if file_extension.lower() == '.txt' and os.path.exists('rentalBot1.py'):
        os.remove('rentalBot1.py')
    # ファイルを保存
    file_path = 'rentalBot1.py'
    await attachment.save(file_path)
    await ctx.send(f'ファイルを保存しています..')
    global bat_exe
    if bat_exe is not None and bat_exe.poll() is None:
        return await ctx.send('BotRunner1.bat は既に実行中です。')
    bat_exe = subprocess.Popen(['cmd', '/c', 'BotRunner1.bat'])
    while True:
        if os.path.exists(exe_path):
            await ctx.send(f'ファイルが正常に保存されました。')
            break

bot_process = None
script_dir = os.path.dirname(os.path.abspath(__file__))

@bot.command(name='Run', help='$Run')
async def run_command(ctx):
    global bot_process
    if bot_process is not None and bot_process.poll() is None:
        return await ctx.send('rentalBot1.exe は既に実行中です。')
    # 新しい cmd プロセスを起動して BotRunner1.bat を実行
    exe_path = os.path.join(script_dir, 'dist', 'rentalBot1.exe')
    bot_process = subprocess.Popen(['start', 'cmd', '/k', exe_path] , shell=True)
    await ctx.send('rentalBot1.exe を実行しました。')

@bot.command(name='Stop', help='$Stop')
async def stop_command(ctx):
    try:
        subprocess.run(['BotStopper1.bat'], check=True)
        await ctx.send('BotRunner1.exe を停止しました。')
    except subprocess.CalledProcessError:
        await ctx.send('BotRunner1.exe を停止できませんでした。')


@bot.command(name='saveS',help='$saveS 保存名 音声ファイルを添付(拡張子は.mp3)')
async def saveSound(ctx , file_name):
    if ctx.message.attachments:
        attachment = ctx.message.attachments[0]
        file_path = f"sound_{file_name}.mp3"
        await attachment.save(file_path)        
        await ctx.send(f"音声ファイルが保存されました: {file_path}")
    else:
        await ctx.send("添付された音声ファイルが見つかりません")

@bot.command(name='listS',help='$listS')
async def list_sounds(ctx):
    sound_files = [file for file in os.listdir() if file.startswith("sound_") and file.endswith(".mp3")]
    sound_names = [file.replace("sound_", "").replace(".mp3", "") for file in sound_files]
    if sound_files:
        embed = discord.Embed(title="保存されているサウンド", description="使うときは '$playS 保存名'\n保存名はファイル名と違って 'sound_' と '.mp3' 付けないよ\n上書きするときは、保存名を同じにすると上書きできるよ")
        for sound_file, sound_name in zip(sound_files, sound_names):
            embed.add_field(name=f"• {sound_name}", value=f" {sound_file}", inline=False)
        await ctx.send(embed=embed)
    else:
        await ctx.send("う～ん、音声ファイル。一個もないね")

@bot.command(name='playS', help='$playS 保存名')
async def play_sound(ctx, sound_name):
    sound_file_path = f"sound_{sound_name}.mp3"
    if ctx.author.voice and ctx.author.voice.channel:
        channel = ctx.author.voice.channel
        if ctx.voice_client is not None:
            voice_channel = ctx.voice_client
        else:
            voice_channel = await channel.connect()
        voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=sound_file_path))
    else:
        await ctx.send("ボイスチャンネルに接続している必要があります")

@bot.command(name='gazo',help='$gazo キーワード')
async def gazoSearch(ctx , key_word):
    log = await ctx.send("以前のデータを削除中..")
    for engine in ["Google", "Bing"]:
        engine_dir = os.path.join(os.getcwd(), engine)
        for file_name in os.listdir(engine_dir):
            file_path = os.path.join(engine_dir, file_name)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    os.rmdir(file_path)
            except Exception as e:
                print(e)

    log = await log.edit(content="Googleで検索中..")
    google_crawler = GoogleImageCrawler(storage={"root_dir": "Google"})
    google_crawler.crawl(keyword=key_word, max_num=2)
    log = await log.edit(content="Bingで検索中..")
    bing_crawler = BingImageCrawler(storage={"root_dir": "Bing"})
    bing_crawler.crawl(keyword=key_word, max_num=2)
    log = await log.edit(content="画像を整列中..")
    image_paths = []
    for engine in ["Google", "Bing"]:
        for i, file_name in enumerate(os.listdir(os.path.join(os.getcwd(), engine)), start=1):
            file_path = os.path.join(engine, file_name)
            new_file_path = os.path.join(engine, f"{i}.jpg")
            os.rename(file_path, new_file_path)
            image_paths.append(new_file_path)
    log = await log.edit(content="画像を送信中..")
    for image_path in image_paths:
        if os.path.exists(image_path) and os.path.getsize(image_path) > 0:
            with open(image_path, 'rb') as file:
                picture = discord.File(file, filename=f"image.jpg")
                await ctx.send(file=picture,silent=True)
        else:
            await ctx.send(f"File {image_path} does not exist.")
    log = await log.edit(content="送信完了。")

@bot.command(name='enq',help='$enq アンケートのタイトル')
async def enq_create(ctx , enq_title):
    open( enq_title+'.enq', 'w').close()
    await ctx.send(f"'{enq_title}'というアンケートを作成しました")

@bot.command(name='enqW',help='$enqW 書き込むアンケート名 書き込む内容')
async def enq_write(ctx , enq_title , enq_opinion):
    username = ctx.author.name
    new_entry = username + '\n' + enq_opinion + '\n'
    if os.path.exists(enq_title+'.enq'):
        with open(enq_title+'.enq', 'r') as f:
            lines = f.readlines()
        if username + '\n' in lines:
            index = lines.index(username + '\n')
            lines[index + 1] = enq_opinion + '\n'
        else:
            lines.append(new_entry)
        with open(enq_title+'.enq', 'w') as f:
            f.writelines(lines)
    else:
        with open(enq_title+'.enq', 'w') as f:
            f.write(new_entry)
    await ctx.send(f"'{enq_title}'に書き込みが完了しました")

@bot.command(name='enqR',help='$enqR 読み込むアンケート名')
async def enq_read(ctx , enq_title):
    with open( enq_title+'.enq', 'r') as file:
        content = file.read()
    split_content = content.split('\n')
    usernames = split_content[::2]
    enq_opinions = split_content[1::2]
    embed = discord.Embed(title=enq_title, description="各ユーザーの意見", color=0x7fffd4)
    for username, opinion in zip(usernames, enq_opinions):
        embed.add_field(name=f"• {username}", value=f"{opinion}", inline=False)
    await ctx.send(embed=embed)

@bot.command(name='enqL', help='$enqL')
async def list_enq(ctx):
    files = os.listdir()
    enq_files = [file for file in files if file.endswith('.enq')]
    embed = discord.Embed(title="今登録されているアンケート", color=0x00fa9a)
    for enq_file in enq_files:
        file_name = os.path.splitext(enq_file)[0]
        embed.add_field(name=file_name, value="" , inline=False)
    await ctx.send(embed=embed)

@bot.command(name='enqD',help='$enqD 消去するアンケート名')
async def delete_enq(ctx , enq_title):
    if os.path.exists(enq_title+'.enq'):
        os.remove(enq_title+'.enq')
        await ctx.send(f"'{enq_title}'を削除しました")
    else:
        await ctx.send(f"'{enq_title}'というアンケートは現時点では存在していません")


#外部プロセス
@bot.command(name='chien', help='$chien')
async def chien_send(ctx):
    await ctx.send('遅延警察MATSUNAGAに連絡しています。')


@bot.command(name = 'allHelp',help='全てのコマンドの詳細説明★★★★★★★★★ :$allHelp')
async def chien_send(ctx):
    Cstart_text = 'カウントアップする'
    Cstop_text = 'カウントアップを停止する'
    Enzan_text = '四則演算する'
    Run_text = 'アップロードしたファイルを実行'
    Save_text = '.txt または .pyファイルをアップロード'
    Stop_text = '実行したファイルを停止'
    Tsplit_text = 'チーム分けなどができる'
    Tsplit_text_2 = 'メンバーの名前は yama, kawa'
    Tsplit_text_3 = '\t\tのようにメンバーごとに , で区切る'
    chien_text = '近畿の鉄道の遅延状況を画像で表示する'
    count_text = '指定された数値からカウントダウンしていく'
    join_text = 'botをボイスチャンネルに召喚する'
    loop_text = 'その動画の音声の再生をloopさせる'
    play_text = 'botにyoutubeの音声を再生させる'
    rand_text = '乱数を生成する'
    searchYT_text = '指定した言葉をYouTubeで検索しURLを貼る'
    stop_text = '再生を停止させ、終了させる'
    timeNow_text = '現在時刻を表示する'
    trans_text = '指定の言葉を翻訳する'
    trans_text_1 = '言語を指定するときは言語コードを使うこと'
    trans_text_2 = '言語コード'
    trans_text_3 = '\t英語: en'
    trans_text_4 = '\t日本語: ja'
    trans_text_5 = '\t中国語(簡体字): zh-CN'
    trans_text_6 = '\t中国語(繁体字): zh-TW'
    trans_text_7 = '\tドイツ語: de'
    trans_text_8 = '\tフランス語: fr'
    trans_text_9 = '\tスペイン語: es'
    trans_text_10= '\tイタリア語: it'
    trans_text_11= '\tロシア語: ru'
    trans_text_12= '\tアラビア語: ar'
    trans_text_13= '\tポルトガル語: pt'
    trans_text_14= '\tヒンディー語: hi'
    trans_text_15= '\t韓国語: ko'
    trans_text_16= '\tトルコ語: tr'
    ugg_text = 'u.ggからビルド、ルーン、カウンター、ARAM'
    ugg_text_1 = 'について画像を提供する'
    ugg_text_2 = 'チャンピオン名の入力については'
    ugg_text_3 = 'ひらがな, カタカナ, 英語'
    ugg_text_4 = 'での入力に対応しています'
    volume_text = '音声のボリュームを調整する'
    weather_text = '今日と、次の日の気象情報を教えてくれる'
    weekday_text = 'その日が何曜日だったかを求める'
    wiki_text = 'Wikipediaの情報を教えてくれる'
    saveS_text = '音声ファイルを指定された名前で保存する'
    listS_text = '保存されている音声ファイルのリストを表示する'
    playS_text = '音声ファイルを再生する'
    gazo_text = 'GoogleとBingから2枚ずつ画像を検索\nヒットした2つを送信'
    enq_text = 'アンケートを作成できる\nこのアンケートは各ユーザーごとに意見が言えるやつ'
    enqD_text = '指定のアンケートを消去することができる'
    enqL_text = '現在登録されているアンケートの一覧は表示することができる'
    enqR_text = '指定のアンケートに書かれている内容を表示する\nここでエラーが起きた場合はアンケートに書く意見が多すぎるのが原因'
    enqW_text = '指定のアンケートに意見を書き込む'

    embed = discord.Embed(title="MATSUNAGAbotの登録コマンド詳細", color=0xFF0000)
    embed.add_field(name="$Cstart", value=Cstart_text, inline=False)
    embed.add_field(name="$Cstop", value=Cstop_text, inline=False)
    embed.add_field(name="$Enzan", value=Enzan_text, inline=False)
    embed.add_field(name="$Run", value=Run_text, inline=False)
    embed.add_field(name="$Save", value=Save_text, inline=False)
    embed.add_field(name="$Stop", value=Stop_text, inline=False)
    embed.add_field(name="$Tsplit", value=Tsplit_text, inline=False)
    embed.add_field(name="", value=Tsplit_text_2, inline=False)
    embed.add_field(name="", value=Tsplit_text_3, inline=False)
    embed.add_field(name="$chien", value=chien_text, inline=False)
    embed.add_field(name="$count", value=count_text, inline=False)
    embed.add_field(name="$join", value=join_text, inline=False)
    embed.add_field(name="$loop", value=loop_text, inline=False)
    embed.add_field(name="$play", value=play_text, inline=False)
    embed.add_field(name="$rand", value=rand_text, inline=False)
    embed.add_field(name="$searchYT", value=searchYT_text, inline=False)
    embed.add_field(name="$stop", value=stop_text, inline=False)
    embed.add_field(name="$timeNow", value=timeNow_text, inline=False)

    embed2 = discord.Embed(title="", color=0xFF0000)
    embed2.add_field(name="$trans", value=trans_text, inline=False)
    embed2.add_field(name="", value=trans_text_1, inline=False)
    embed2.add_field(name="", value=trans_text_2, inline=False)
    embed2.add_field(name="", value=trans_text_3, inline=False)
    embed2.add_field(name="", value=trans_text_4, inline=False)
    embed2.add_field(name="", value=trans_text_5, inline=False)
    embed2.add_field(name="", value=trans_text_6, inline=False)
    embed2.add_field(name="", value=trans_text_7, inline=False)
    embed2.add_field(name="", value=trans_text_8, inline=False)
    embed2.add_field(name="", value=trans_text_9, inline=False)
    embed2.add_field(name="", value=trans_text_10, inline=False)
    embed2.add_field(name="", value=trans_text_11, inline=False)
    embed2.add_field(name="", value=trans_text_12, inline=False)
    embed2.add_field(name="", value=trans_text_13, inline=False)
    embed2.add_field(name="", value=trans_text_14, inline=False)
    embed2.add_field(name="", value=trans_text_15, inline=False)
    embed2.add_field(name="", value=trans_text_16, inline=False)

    embed3 = discord.Embed(title="", color=0xFF0000)
    embed3.add_field(name="$ugg", value=ugg_text, inline=False)
    embed3.add_field(name="", value=ugg_text_1, inline=False)
    embed3.add_field(name="", value=ugg_text_2, inline=False)
    embed3.add_field(name="", value=ugg_text_3, inline=False)
    embed3.add_field(name="", value=ugg_text_4, inline=False)
    embed3.add_field(name="$volume", value=volume_text, inline=False)
    embed3.add_field(name="$weather", value=weather_text, inline=False)
    embed3.add_field(name="$weekday", value=weekday_text, inline=False)
    embed3.add_field(name="$wiki", value=wiki_text, inline=False)
    embed3.add_field(name="$saveS", value=saveS_text, inline=False)
    embed3.add_field(name="$listS", value=listS_text, inline=False)
    embed3.add_field(name="$playS", value=playS_text, inline=False)
    embed3.add_field(name="$gazo", value=gazo_text, inline=False)
    embed3.add_field(name="$enq", value=enq_text, inline=False)
    embed3.add_field(name="$enqD", value=enqD_text, inline=False)
    embed3.add_field(name="$enqL", value=enqL_text, inline=False)
    embed3.add_field(name="$enqR", value=enqR_text, inline=False)
    embed3.add_field(name="$enqW", value=enqW_text, inline=False)
    embed3.add_field(name="$allHelp", value='全てのコマンドの詳細説明 つまりこれ', inline=False)
    await ctx.send(content="制作者の更新し忘れが無かったら全部のコマンドの詳細が書いてるよ", embed=embed)
    await ctx.send(content="", embed=embed2)
    await ctx.send(content="", embed=embed3)

bot.run('そるに聞け!')
