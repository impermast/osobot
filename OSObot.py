# Bot for MEPhI discord server for students
#
# 
#
# made by DS Kalashnikov


import discord
import datetime
from datetime import datetime
import asyncio

from dotenv import load_dotenv
import os
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#import ides
IdChSystem = 742480874297229342
IdChCmd = 746487413186101400
IdChRespond = 742480826763313152
#IdChKurator = 

IdMsgRules = 747532389017976992

IdRoleKurator = 742476738839183361
IdRoleBuro = 742487382657597560
IdRoleIyft = 742484261449236500
IdRoleLaplas = 743162727542947940
IdRoleIfib = 743163172529373214
IdRoleIntel = 743162929553342567
IdRoleIics = 743163343925280890
IdRoleIftis = 743210280900886630
IdRoleFbiuks = 744637033154084944
IdRoleImo = 743210079695667300
IdRoleIfteb = 743209866331684877


EmojiList = {
    "iyft":IdRoleIyft,
    'laplas':IdRoleLaplas,
    'ifib':IdRoleIfib,
    'intel':IdRoleIntel,
    'iics':IdRoleIics,
    'iftis':IdRoleIftis,
    'ifteb':IdRoleIfteb,
    'imo':IdRoleImo,
    'fbiuks':IdRoleFbiuks
}

#BotCode
class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_member_join(self, member):
        print('[COMAND] !emb')
        #Сообщение в системный чат
        dt=datetime.now()
        await client.get_channel(IdChSystem).send('{} вступил в {}.'.format(member.mention, dt.strftime("%H:%M:%S %d %B")))
        #Создание задержки
        await asyncio.sleep(1.5)
    async def on_member_remove(self, member):
        await client.get_channel(IdChSystem).send('{} вышел в {}.'.format(member.mention,  dt.strftime("%H:%M:%S %d %B")))


#Автороли по реакции
    async def on_raw_reaction_add(self, react):
        if react.message_id == IdMsgRules:
            print('RoleCheck')
            dt=datetime.now()
            memb = react.member
            
            for emj, idi in EmojiList.items():
              if react.emoji.name == emj:  
                print('rendering')
                role = memb.guild.get_role(idi)
                await client.get_channel(IdChSystem).send('{} получил роль {} от реакции в {}.'.format(memb.mention, memb.guild.get_role(idi).mention, dt.strftime("%H:%M:%S %d %B")))
                await memb.add_roles(role)
             
    async def on_raw_reaction_remove(self, react):
        if react.message_id == IdMsgRules:
            print('RemoveCheck')
            guild = client.get_guild(react.guild_id)
            sys = client.get_channel(IdChSystem)
            memb = guild.get_member(react.user_id)
            dt=datetime.now()
            
            for emj, idi in EmojiList.items():
              if react.emoji.name == emj:  
                role = guild.get_role(idi)
                await sys.send('{} лишился роли {} от реакции в {}.'.format(memb.mention, guild.get_role(idi).mention,dt.strftime("%H:%M:%S %d %B")))
                await memb.remove_roles(role, reason="Убрал реакцию")
                print("cleared")
                      



    async def on_message(self, message):

#Проверка роли
      if message.guild.get_role(IdRoleBuro) in message.author.roles:

#writefunc
        if (message.content.startswith('!write'))and(message.author != self.user):
            print('[COMMAND] !w')
            await message.channel.send(message.content[6:])
            await message.delete()

#delfunc
        if message.content.startswith('!delete'):
            print('[COMMAND] !del')
            number = int(message.content[8:])
            i=0
            async for mes in message.channel.history():
                if (i > number):
                    break
                i=i+1
                ## wait for 0.5 seconds again
                await asyncio.sleep(0.1)
                ## delete the message
                await mes.delete()
            print('[COMMAND] !del over')
        
#commandsfunc        
        if (message.content.startswith('!commands'))and(message.author != self.user):
            print('[COMMAND] !cmd')
            await message.channel.send('List of comanеds: !write [text] !delete N !commands !test')
            await message.delete()
            
#testfunc
        if (message.content.startswith('!test'))and(message.author != self.user):
            print('[COMMAND] !test')
            await message.channel.send('**Launched**')
        
#bot respond
        m = message        
        if (m.content.startswith('!respond'))and(m.author != self.user)and(m.channel == client.get_channel(IdChCmd)):
            print('[COMMAND] !respond')
            await client.get_channel(IdChRespond).send(message.content[8:])
        
#emb func
        if message.content.startswith('!emb'):
           print('[COMAND] !emb')
           await message.delete()
           
           S=message.content.split('|')
           emb= discord.Embed(title = '{}'.format(S[1]), colour = discord.Color.blue())
           emb.set_thumbnail(url = 'https://sun9-61.userapi.com/c837538/v837538137/1abc5/VdZCHNTGdO0.jpg')
           emb.discription = '{}'.format(S[2])
           
           await message.channel.send(embed = emb)


client = BotClient()
client.run(TOKEN)

