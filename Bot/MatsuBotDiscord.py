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
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from discord.ext import commands
from datetime import datetime
from youtubesearchpython import VideosSearch
from googletrans import Translator
from time import sleep
from datetime import datetime, timezone, timedelta
from PIL import Image
from rembg import remove


bot = commands.Bot(command_prefix='$', intents=discord.Intents.all())

naga_path = ['NaokiGOD.png','NaoPaisen.png','Naoki.png']

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

    if message.attachments:
        for attachment in message.attachments:
            if attachment.filename.endswith('.png') or attachment.filename.endswith('.jpg'):
                await attachment.save('temp.jpg')
                img = cv2.imread('temp.jpg')
                if img is None:
                    print('Failed to load image.')
                else:
                    # BGR -> RGB
                    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                    # NumPy配列からPIL画像オブジェクトを生成
                    pil_image = Image.fromarray(rgb_img)
                    # アルファチャンネルを追加
                    pil_image.putalpha(255)
                    pil_image.save('temp.png', 'PNG')
                image_input = Image.open("temp.png")
                output = remove(image_input)
                output.save('temp.png')
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
        mention = message.author.mention
        await message.channel.send(f'{mention} さん、おやすみなさい！')
    elif '寝る' in message.content:
        mention = message.author.mention
        await message.channel.send(f'{mention} 寝ちゃうんだね、残念')
    elif 'ねる' in message.content:
        mention = message.author.mention
        await message.channel.send('ねぇるねるねるねぇー')
    elif 'しね' in message.content or 'ころす' in message.content or 'あほ' in message.content or '殺す' in message.content or '殺る' in message.content:
        mention = message.author.mention
        await message.channel.send(f'{mention} さん、それは暴言ですよ！')
    elif 'かす' in message.content or 'カス' in message.content or 'キモイ' in message.content or 'あ？' in message.content:
        mention = message.author.mention
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
    elif 'くり' in message.content or 'クリ' in message.content or '年末' in message.content or '聖なる夜' in message.content or 'サンタ' in message.content:
        await message.channel.send('おまえ、ぼっちじゃんww')

    await bot.process_commands(message)



@bot.command(name='timeNow')
async def current_time(ctx):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    await ctx.send(f'現在の時刻は {current_datetime} だぜ。')

@bot.command(name='rand')
async def generate_random(ctx, min_value: int, max_value: int):
    if min_value >= max_value:
        await ctx.send("最小値は最大値より小さい必要があるんだなぁこれが")
        return
    random_number = random.randint(min_value, max_value)
    await ctx.send(f'生成された乱数: {random_number}')

@bot.command(name='searchYT')
async def search_youtube(ctx, *query):
    search_query = ' '.join(query)
    videos_search = VideosSearch(search_query, limit=1)
    if videos_search.result() and videos_search.result()['result']:
        video_url = videos_search.result()['result'][0]['link']
        await ctx.send(f'検索結果: {video_url}')
    else:
        await ctx.send('該当する動画が見つかりませんでした。')

@bot.command(name='Enzan')
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

@bot.command(name='weather')
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

@bot.command(name='count')
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

@bot.command(name='Cstart')
async def count_up_start(ctx):
    task = bot.loop.create_task(count_up_task(ctx))
    ctx.bot.count_up_task = task

@bot.command(name='Cstop')
async def count_up_stop(ctx):
    if hasattr(ctx.bot, 'count_up_task') and ctx.bot.count_up_task:
        ctx.bot.count_up_task.cancel()
        await ctx.send("止めてやったぜ★")
    else:
        await ctx.send("カウントなんてされてなかった★")

@bot.command(name='wiki')
async def web_text(ctx, url):
    urls = 'https://ja.wikipedia.org/wiki/'+ url
    response = requests.get(urls)
    response.raise_for_status()  # エラーチェック
    # BeautifulSoupを使用してHTMLを解析
    soup = BeautifulSoup(response.text, 'html.parser')
    # 前文を取得
    first_paragraph = soup.find('p').text
    # Discordに送信
    if len(first_paragraph) >= 100:
        await ctx.send(f'**{url}**\n\n{first_paragraph}')
    else:
        # 100文字以下の場合は最大500文字まで取得して送信
        additional_text = soup.find('p', string=lambda x: x and len(x) > 100)
        if additional_text:
            additional_text = additional_text.text[:400]  # 適切な文字数に調整
            await ctx.send(f'**{url}**\n\n{first_paragraph}{additional_text}...')
        else:
            await ctx.send(f'**{url}**\n\n{first_paragraph}')

@bot.command(name='trans')
async def web_text(ctx, t1,t2, text):
    def translate_text(text, target_language=t2):
        translator = Translator()
        translation = translator.translate(text, dest=target_language)
        return translation.text
    text_to_translate = text
    target_language = t2
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

@bot.command(name='Tsplit')
async def command_script(ctx, pNames,value :int):
    strings = pNames.split(',')
    shuffled_strings = random.sample(strings, len(strings))
    groups = [shuffled_strings[i:i+value] for i in range(0, len(shuffled_strings), value)]
    for index, group in enumerate(groups, start=1):
        group_text = ', '.join(group)
        await ctx.send(f'グループ {index}: {group_text}')

@bot.command(name='weekday')
async def command_weekday(ctx, year: int, month: int, day: int):
    target_date = datetime(year, month, day).date()
    weekdays = ["月曜日", "火曜日", "水曜日", "木曜日", "金曜日", "土曜日", "日曜日"]
    weekday_index = target_date.weekday()
    await ctx.send(f"{target_date.year}年{target_date.month}月{target_date.day}日は{weekdays[weekday_index]}です。")

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

@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name))
        return
    else:
        channel = ctx.message.author.voice.channel
    await channel.connect()

@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


bot.run('solに聞け!!')