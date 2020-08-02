# bot.py
import os
import random
import requests

import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv('token.env')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command(name='hitme', help='Adding 6 numbers after !hitme will hit you with that link.')
async def hit_me(ctx, number: str):
    if ctx.channel.name == 'hentai' or ctx.channel.name == 'nsfw':
        url = "https://nhentai.net/g/"
        newUrl = url + number

        if (checkURL(newUrl) == True):
            response = newUrl
        else:
            response = "Unfortunately that link does not exist. :point_right_tone1: :point_left_tone1:"
        await ctx.send(response)

@bot.command(name='random', help='Random link may or may not work.')
async def random_link(ctx):
    if ctx.channel.name == 'hentai' or ctx.channel.name == 'nsfw':
        while True:
            newUrl = randomURL()
            # print(newUrl)
            # print(checkURL(newUrl))
            if(checkURL(newUrl) == True):
                break
        response = newUrl
        await ctx.send(response)

@bot.command(name='yasir', help='Yasir Meme Library')
async def yasir(ctx):
        img = selectRandomFromArray(YASIR)
        response = img
        await ctx.send(response)

@bot.command(name='erik', help='Erik Meme Library')
async def erik(ctx):
        img = selectRandomFromArray(ERIK)
        response = img
        await ctx.send(response)

@bot.command(name='aj', help='AJ Meme Library')
async def aj(ctx):
        img = selectRandomFromArray(AJ)
        response = img
        await ctx.send(response)

@bot.command(name='murad', help='Murad Meme Library')
async def murad(ctx):
        img = selectRandomFromArray(MURAD)
        response = img
        await ctx.send(response)

@bot.command(name='thomas', help='Thomas Meme Library')
async def thomas(ctx):
        img = selectRandomFromArray(THOMAS)
        response = img
        await ctx.send(response)

@bot.command(name='ousman', help='Ousman Meme Library')
async def ousman(ctx):
        img = selectRandomFromArray(OUSMAN)
        response = img
        await ctx.send(response)

@bot.command(name='nick', help='Nick Meme Library')
async def nick(ctx):
        img = selectRandomFromArray(NICK)
        response = img
        await ctx.send(response)

@bot.command(name='juan', help='Juan Meme Library')
async def juan(ctx):
        img = selectRandomFromArray(JUAN)
        response = img
        await ctx.send(response)

@bot.command(name='puji', help='Puji Meme Library')
async def puji(ctx):
        img = selectRandomFromArray(PUJI)
        response = img
        await ctx.send(response)

@bot.command(name='inti', help='Inti Meme Library')
async def inti(ctx):
        img = selectRandomFromArray(INTI)
        response = img
        await ctx.send(response)

@bot.command(name='wayne', help='Wayne Meme Library')
async def wayne(ctx):
        img = selectRandomFromArray(WAYNE)
        response = img
        await ctx.send(response)

@bot.command(name='saad', help='Saad Meme Library')
async def saad(ctx):
        img = selectRandomFromArray(SAAD)
        response = img
        await ctx.send(response)

@bot.command(name='oscar', help='Oscar Meme Library')
async def oscar(ctx):
        img = selectRandomFromArray(OSCAR)
        response = img
        await ctx.send(response)

@bot.command(name='lucky', help='Lucky Meme Library')
async def lucky(ctx):
        img = selectRandomFromArray(LUCKY)
        response = img
        await ctx.send(response)

def checkURL(url):
    request = requests.get(url)
    if request.status_code == 200:
        return True

def randomURL():
    url = "https://nhentai.net/g/"
    number = random.randint(100000, 999999)
    strNumber = str(number)
    newUrl = url + strNumber
    return newUrl

def selectRandomFromArray(inputArray):
    length = len(inputArray)
    selection = random.randrange(0, length)
    return inputArray[selection]

YASIR = ["https://media.discordapp.net/attachments/724774470157336596/730626389463793764/IMG7002211315044085409.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730620749072826468/IMG4570228553027885153.jpg", "https://media.discordapp.net/attachments/724774470157336596/730620733939646474/IMG3769845791982926796.jpg", "https://cdn.discordapp.com/attachments/724774470157336596/730620705510785097/Snapchat-2924121080950177554.mp4", "https://media.discordapp.net/attachments/724774470157336596/730620699852538006/IMG7384379545458939486.jpg", "https://media.discordapp.net/attachments/724774470157336596/730618756425842688/IMG6361184593080416035.jpg?width=407&height=677", "https://media.discordapp.net/attachments/724774470157336596/730618450250301520/IMG8943275589067208213.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730616708687200316/540x960.png?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730616426540564560/603x804.png?width=508&height=677", "https://media.discordapp.net/attachments/724774470157336596/730611115071111168/1125x1500.png?width=508&height=677", "https://i.groupme.com/603x1073.jpeg.331611a40a49485785ce2d28e80446b2.large", "https://media.discordapp.net/attachments/681651011496181772/709832472728305705/603x804.png?width=508&height=677","https://media.discordapp.net/attachments/681651011496181772/709832510586224730/603x804.png?width=508&height=677","https://media.discordapp.net/attachments/681651011496181772/709833384150695936/400x533.png", "https://media.discordapp.net/attachments/681651011496181772/709834422404251668/400x300.png", "https://media.discordapp.net/attachments/681651011496181772/709834467048554667/603x804.png?width=508&height=677", "https://media.discordapp.net/attachments/681651011496181772/709834507750211604/603x804.png?width=508&height=677", "https://v.groupme.com/24106911/2020-07-09T02:16:19Z/64e46c34.640x360r90.mp4"]
ERIK = ["https://cdn.discordapp.com/attachments/724774470157336596/730626199126278166/Snapchat-240202354.mp4", "https://media.discordapp.net/attachments/724774470157336596/730617553717821480/400x532.png", "https://media.discordapp.net/attachments/681651011496181772/709833479323648030/400x533.png", "https://media.discordapp.net/attachments/681651011496181772/709836628356759662/500x888.png?width=381&height=677", "https://media.discordapp.net/attachments/681651011496181772/709836686166720552/416x740.png?width=380&height=677", "https://cdn.discordapp.com/attachments/681651011496181772/709837257997025372/video0.mp4", "https://i.groupme.com/1125x1500.jpeg.ac4f9bdce4074efc8d2574a59c49dfeb.large"]
AJ = ["https://media.discordapp.net/attachments/724774470157336596/730624848933683311/Screenshot_20200708-232140_GroupMe.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730624081229119498/Screenshot_20200708-231906_GroupMe.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730623608308629504/IMG1099937308245824009.jpg?width=529&height=677", "https://media.discordapp.net/attachments/724774470157336596/730622428526411847/IMG3425445765268684396.jpg?width=677&height=677", "https://media.discordapp.net/attachments/724774470157336596/730620343835689010/IMG7926874424126553455.jpg?width=451&height=677", "https://cdn.discordapp.com/attachments/724774470157336596/730620045767475200/Snapchat-81023934.mp4", "https://cdn.discordapp.com/attachments/724774470157336596/730619923319095326/Snapchat-1675116556.mp4", "https://media.discordapp.net/attachments/724774470157336596/730619649007550534/IMG4654979846180850080.jpg?width=380&height=676", "https://media.discordapp.net/attachments/724774470157336596/730619145766567977/400x533.png", "https://media.discordapp.net/attachments/724774470157336596/730618846783995985/IMG5407616199633363405.jpg?width=508&height=677", "https://media.discordapp.net/attachments/724774470157336596/730618233962364989/IMG1666306457376356551.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617866973347860/Snapchat-1040820447.jpg?width=349&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617855803916338/IMG7284940503531791735.jpg", "https://media.discordapp.net/attachments/724774470157336596/730617811407208528/Snapchat-240735567.jpg?width=349&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617721573736482/IMG8061211520133796465.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617682394742914/IMG5575341217040918713.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730617551167684608/IMG7160663888795305344.jpg?width=677&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617294232879144/IMG1686674164329156604.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617293813579806/IMG7476863097896991627.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617293524041788/IMG8775787060398762490.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617293234634843/IMG6272117328818112609.jpg?width=407&height=677", "https://i.groupme.com/1125x1500.jpeg.e02e4a49bd9147ef90081ae30b48f4d5.large","https://media.discordapp.net/attachments/681651011496181772/709831188122042468/1170x1170.png?width=677&height=677", "https://media.discordapp.net/attachments/681651011496181772/709833332782792724/747x960.png?width=527&height=677", "https://media.discordapp.net/attachments/681651011496181772/709833747385811034/844x1006.png?width=568&height=677", "https://i.groupme.com/1002x1264.jpeg.adb3f7b1fd64468abc7952123cdfa329.large"]
MURAD = ["https://media.discordapp.net/attachments/725870134857564331/730832221048406096/603x603.png?width=547&height=547", "https://media.discordapp.net/attachments/724774470157336596/730635830363815966/image1.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730635829579612160/image0.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730629328714596382/Screenshot_20200708-233855_GroupMe.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730623948324077678/Screenshot_2018-02-21-22-16-0701.PNG?width=668&height=677", "https://media.discordapp.net/attachments/724774470157336596/730623266544418896/Screenshot_2016-09-16-21-00-25.PNG?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730623103603965952/720x540.png", "https://media.discordapp.net/attachments/724774470157336596/730620415298240563/640x1136.png?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730618003678298193/IMG7446060318862642103.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617935659270214/IMG834184658362781279.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617866973347860/Snapchat-1040820447.jpg?width=349&height=677", "https://media.discordapp.net/attachments/724774470157336596/730617451183865866/IMG7987815929185144687.jpg", "https://media.discordapp.net/attachments/681651011496181772/709834094997012490/564x1000.png?width=381&height=677", "https://media.discordapp.net/attachments/681651011496181772/709835036102492280/640x960.png?width=451&height=677", "https://media.discordapp.net/attachments/681651011496181772/709835231028314112/1125x1500.png?width=508&height=677", "https://cdn.discordapp.com/attachments/681651011496181772/709835502861418568/6e84ab07.320x568r.mp4"]
THOMAS = ["https://cdn.discordapp.com/attachments/724774470157336596/730634358280683570/video0.mp4", "https://media.discordapp.net/attachments/724774470157336596/730627769960103971/Screenshot_20200708-233344_GroupMe.jpg?width=329&height=676", "https://cdn.discordapp.com/attachments/724774470157336596/730626705986814011/Screenshot_20200327-151643.png", "https://media.discordapp.net/attachments/724774470157336596/730626599417937940/Screenshot_20180208-174528.png?width=329&height=676", "https://cdn.discordapp.com/attachments/724774470157336596/730626321054695424/IMG2289842727894938081.mp4", "https://media.discordapp.net/attachments/724774470157336596/730626032859873350/Snapchat-687696731.jpg?width=349&height=677", "https://media.discordapp.net/attachments/724774470157336596/730625856241664030/Screenshot_20170510-153029.png?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730625504327106611/Screenshot_20200708-232409.png?width=321&height=677", "https://media.discordapp.net/attachments/724774470157336596/730625354217160784/400x400.png", "https://media.discordapp.net/attachments/724774470157336596/730623396643340419/Screenshot_20180610-115257_Snapchat.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730622834489163837/IMG_20180118_053801_802.jpg", "https://media.discordapp.net/attachments/724774470157336596/730622621573578762/IMG1282693618.jpg?width=329&height=677", "https://media.discordapp.net/attachments/724774470157336596/730621792011550850/Screenshot_20161203-192439.png?width=381&height=677", "https://cdn.discordapp.com/attachments/724774470157336596/730620121806012446/Snapchat-2055036001.mp4", "https://media.discordapp.net/attachments/724774470157336596/730619452642558002/image0.jpg?width=382&height=677", "https://media.discordapp.net/attachments/724774470157336596/730619445143142500/image0.jpg?width=382&height=677", "https://media.discordapp.net/attachments/724774470157336596/730616982659006484/Snapchat-289475458.jpg?width=349&height=677", "https://media.discordapp.net/attachments/724774470157336596/730616921690472468/Snapchat-1359115204.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730616884134936616/IMG7618570104318469044.jpg?width=508&height=677", "https://media.discordapp.net/attachments/724774470157336596/730616867869163580/Snapchat-380816265.jpg?width=381&height=677", "https://i.groupme.com/720x1280.jpeg.2b974cd46b004073ba57e248e6beb053.large", "https://media.discordapp.net/attachments/681651011496181772/709834783022120970/603x828.png?width=493&height=677", "https://media.discordapp.net/attachments/681651011496181772/709835303367606336/722x1280.png?width=382&height=677", "https://media.discordapp.net/attachments/681651011496181772/709836543648333865/504x897.png?width=380&height=676", "https://media.discordapp.net/attachments/681651011496181772/709836742676447282/640x1136.png?width=381&height=677", ]
OUSMAN = ["https://media.discordapp.net/attachments/724774470157336596/730623069508468756/Screenshot_20200708-231430_GroupMe.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730623038030217323/IMG-687322800.JPG", "https://media.discordapp.net/attachments/724774470157336596/730622908657041448/Screenshot_20180118-055545.png?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730622834489163837/IMG_20180118_053801_802.jpg", "https://media.discordapp.net/attachments/724774470157336596/730622514664964176/Screenshot_20171227-185844.png?width=329&height=676", "https://cdn.discordapp.com/attachments/724774470157336596/730618160830611526/Snapchat-420188649.mp4", "https://media.discordapp.net/attachments/724774470157336596/730617203187253341/IMG2417617216554497167.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730612883053871134/1125x1500.png?width=508&height=677", "https://media.discordapp.net/attachments/724774470157336596/730612714845765683/722x1280.png?width=382&height=677", "https://media.discordapp.net/attachments/724774470157336596/730611744413581332/IMG333354997943637164.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730610318379712552/400x533.png", "https://media.discordapp.net/attachments/724774470157336596/730610127643607050/500x888.png?width=381&height=677", "https://i.groupme.com/720x1280.jpeg.2b974cd46b004073ba57e248e6beb053.large", "https://media.discordapp.net/attachments/681651011496181772/709832173774962708/747x1328.png?width=381&height=677", "https://media.discordapp.net/attachments/681651011496181772/709832246097477712/747x1328.png?width=381&height=677", "https://media.discordapp.net/attachments/681651011496181772/709832289999257600/747x1328.png?width=381&height=677", "https://media.discordapp.net/attachments/681651011496181772/709832713980608602/720x1280.png?width=381&height=677", "https://media.discordapp.net/attachments/681651011496181772/709833104570843276/224x254.png", "https://media.discordapp.net/attachments/681651011496181772/709834322722422884/603x804.png?width=508&height=677", "https://media.discordapp.net/attachments/681651011496181772/709834613115322368/603x1072.png?width=381&height=677"] 
NICK = ["https://media.discordapp.net/attachments/724774470157336596/730622245642174484/IMG8884363342640188088.jpg?width=382&height=677", "https://media.discordapp.net/attachments/724774470157336596/730622223202910288/Screenshot_20170921-172736.png?width=381&height=677", "https://cdn.discordapp.com/attachments/724774470157336596/730620416577634345/Snapchat-394806981.mp4", "https://cdn.discordapp.com/attachments/724774470157336596/730619764178944060/Snapchat-1219183773.mp4", "https://media.discordapp.net/attachments/724774470157336596/730617172401061888/IMG7139366970191909662.jpg?width=508&height=677","https://media.discordapp.net/attachments/724774470157336596/730617039437430824/IMG1811546968265897941.jpg?width=380&height=676" "https://media.discordapp.net/attachments/724774470157336596/730616979815137370/IMG4761696832319248676.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730616782758477864/603x941.png?width=434&height=677", "https://media.discordapp.net/attachments/724774470157336596/730615063685365810/540x960.png?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730610693736497202/844x1500.png?width=677&height=677", "https://media.discordapp.net/attachments/681651011496181772/709831393835876442/844x1500.png?width=381&height=677", "https://media.discordapp.net/attachments/689559890338906167/730605700652204043/1195x1593.png?width=508&height=677", "https://media.discordapp.net/attachments/724774470157336596/730606770120163438/844x1500.png?width=381&height=677"]
JUAN =["https://media.discordapp.net/attachments/725870134857564331/730832382885757070/1080x1920.png?width=307&height=547", "https://media.discordapp.net/attachments/724774470157336596/730621469914169366/IMG8949945139375006393.jpg?width=381&height=677", "https://media.discordapp.net/attachments/681651011496181772/709833835835162684/747x1328.png?width=677&height=677", "https://media.discordapp.net/attachments/681651011496181772/709835607429349509/603x804.png?width=508&height=677", "https://cdn.discordapp.com/attachments/681651011496181772/709837257997025372/video0.mp4"]
PUJI = ["https://media.discordapp.net/attachments/725870134857564331/730832514205220914/1328x747.png", "https://media.discordapp.net/attachments/724774470157336596/730622752192462888/IMG1661776788.JPG", "https://media.discordapp.net/attachments/724774470157336596/730622268043952178/603x804.png?width=508&height=677", "https://media.discordapp.net/attachments/724774470157336596/730621500994093116/603x603.png", "https://media.discordapp.net/attachments/724774470157336596/730613137866489956/603x1068.png?width=382&height=677", "https://v.groupme.com/15482174/2015-09-23T00:36:58Z/7927b201.568x320r90.mp4", "https://media.discordapp.net/attachments/681651011496181772/709831980476399816/318x435.png"]
INTI = ["https://media.discordapp.net/attachments/724774470157336596/730622428526411847/IMG3425445765268684396.jpg?width=677&height=677", "https://v.groupme.com/15482174/2016-04-28T23:36:33Z/329203d1.568x320r90.mp4", "https://v.groupme.com/15482174/2016-04-28T22:14:07Z/165a76e8.568x320r90.mp4", "https://v.groupme.com/15482174/2016-03-31T16:18:02Z/72e6fe2f.640x360r90.mp4"]
RAHUL = ["https://media.discordapp.net/attachments/724774470157336596/730610898682511501/603x1073.png?width=380&height=677"]
WAYNE =["https://media.discordapp.net/attachments/724774470157336596/730624688241246238/Screenshot_20190314-225048_Video_Player.jpg?width=329&height=676", "https://cdn.discordapp.com/attachments/724774470157336596/730619480148934766/video0.mp4", "https://media.discordapp.net/attachments/724774470157336596/730618233962364989/IMG1666306457376356551.jpg?width=381&height=677"]
SAAD = ["https://media.discordapp.net/attachments/724774470157336596/730625842534678580/Screenshot_20200708-232608_GroupMe.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730625156585619566/Screenshot_20200708-231942_GroupMe.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730623375591866449/IMG3035928266979937013.jpg?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730619414680043560/IMG5302152643896061879.jpg?width=677&height=677", "https://media.discordapp.net/attachments/724774470157336596/730619329439072326/IMG5922233520456898405.jpg", "https://media.discordapp.net/attachments/724774470157336596/730619241841164368/601x800.png?width=508&height=677", "https://media.discordapp.net/attachments/724774470157336596/730618899925565472/IMG2688880413934109822.jpg?width=684&height=677"]
OSCAR = ["https://media.discordapp.net/attachments/724774470157336596/730625125300437042/Screenshot_20200708-231947_GroupMe.jpg?width=329&height=676", "https://media.discordapp.net/attachments/724774470157336596/730623759542911016/504x705.png?width=484&height=677", "https://media.discordapp.net/attachments/724774470157336596/730621900400754708/Screenshot_2015-09-03-16-54-0601.PNG", "https://media.discordapp.net/attachments/724774470157336596/730621615645261924/IMG1884675137970264372.jpg", "https://media.discordapp.net/attachments/724774470157336596/730620951351263272/Snapchat-25828982776603624642.jpg?width=1204&height=677"]
LUCKY = ["https://media.discordapp.net/attachments/724774470157336596/730621235909885962/IMG2330828269296616651.jpg?width=381&height=677"]
ADAM = ["https://media.discordapp.net/attachments/724774470157336596/730623739355463820/Screenshot_2017-10-03-21-53-28.PNG?width=381&height=677", "https://media.discordapp.net/attachments/724774470157336596/730624445470736422/59444617160__A1AF046F-2B34-4A88-9C9A-FC80BAD80604.JPG?width=508&height=677"]

bot.run(TOKEN)