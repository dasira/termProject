#-*- coding: utf-8 -*-
import time
import telepot
from seoul import*
from telepot.loop import MessageLoop

class tBot:
    def __init__(self):
        self.token= '643814290:AAHo5VjyBEzTAzknW9jYRiidkDmjSWLRhwQ'  # 텔레그램으로부터 받은 Bot API 토큰
        self.chat_id = '840789240'
        self.bot = telepot.Bot(self.token)
        self.row= GetInfo()

        print('Listening ...')
        self.Notice()

    def SendMessage(self,text):
        self.bot.sendMessage(self.chat_id,str(text))

    def MessageaLoop(self):
        self.bot.message_loop(self.handle)

    def handle(self,msg):
        content_type, chat_type, chat_id = telepot.glance(msg)
        if content_type != 'text':
            self.bot.sendMessage(self.chat_id,'텍스트로 입력하시기 바랍니다. ')
            return

        text=msg['text']
        args=text.split(' ')

        if args[0]=='지역':
            if args[1][-1]!='구':
                args[1]+='구'
            txt='==========결과==========\n'
            result=[]
            self.SendMessage(str(args[0])+" "+str(args[1]))
            for i in self.row:
                if i.get('gooName')==args[1]:
                    result.append(i)
            for i in result:
                txt=txt+str(i.get('stationName'))+'\n'

            self.SendMessage(txt)

        elif args[0]=='대여소명':
            txt = '================결과==================\n'
            result = []
            self.SendMessage(str(args[0]) + " " + str(args[1]))
            for i in self.row:
                if args[1] in i.get('stationName'):
                    txt=txt+str(i.get('stationName'))+'\n'
                    txt=txt+str('거치대 개수 ')+str(i.get('rackTotCnt'))+'\n'
                    txt = txt +str('주차 총 건수 ')+ str(i.get('parkingBikeTotCnt'))+'\n'
                    txt= txt + str('=====================================\n')
            self.SendMessage(txt)



    def Notice(self):
        text = '========안내========\n'
        text = text+'지역명 검색: 지역 + "구단위의 찾고싶은 지역명" '
        text = text+'대여소명 검색: 대여소명 + "찾고싶은 대여소명" '
        self.SendMessage(text)

#TOKEN = '643814290:AAHo5VjyBEzTAzknW9jYRiidkDmjSWLRhwQ'    # 텔레그램으로부터 받은 Bot API 토큰
#chat_id='840789240'
##bot = telepot.Bot(TOKEN)
#MessageLoop(bot, handle).run_as_thread()
#print ('Listening ...')

# Keep the program running.
#while True:
#    time.sleep(1000)



#print(bot.getMe())
#{'id': 643814290, 'is_bot': True, 'first_name': '따릉이 봇', 'username': 'seoul_bike_bot'}
#bot.sendMessage('840789240','오우씟')

Bot=tBot()

Bot.MessageaLoop()
while 1:
    time.sleep(1)
