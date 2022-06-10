from random import randint,sample,choice
from copy import deepcopy

class game_set:
    def __init__(self):
        self.energy=5
        self.money=500
        self.health=50
        self.strength=3
        self.agility=3
        self.wisdom=3
        self.talent=3
        self.language=3
        self.luck=3
        self.badluck=3
        self.fame=50
        self.item=[]
        self.item_bag=[]
        
        self.type_list=['-days','Infinity']
        self.level_list=['Normal','Hard','Insane']
        self.character_list=[{'name':'Alex','stats':{'energy':5,'money':500,'health':50,'strength':3,'agility':3,'wisdom':3,'talent':3,'language':3,'luck':3,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Arina','stats':{'energy':3,'money':100,'health':10,'strength':-99,'agility':-99,'wisdom':0,'talent':99,'language':3,'luck':5,'badluck':3,'fame':0,'item':['Scissor']}},
                             {'name':'Bob','stats':{'energy':7,'money':500,'health':100,'strength':7,'agility':7,'wisdom':-3,'talent':0,'language':3,'luck':1,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Emma','stats':{'energy':13,'money':200,'health':70,'strength':5,'agility':5,'wisdom':2,'talent':2,'language':3,'luck':0,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Fred','stats':{'energy':7,'money':300,'health':70,'strength':8,'agility':5,'wisdom':1,'talent':5,'language':3,'luck':3,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Genie','stats':{'energy':3,'money':300,'health':30,'strength':2,'agility':2,'wisdom':13,'talent':5,'language':3,'luck':4,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Lucid','stats':{'energy':0,'money':1000,'health':100,'strength':-99,'agility':-99,'wisdom':-99,'talent':-99,'language':3,'luck':999,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Lucy','stats':{'energy':3,'money':1000,'health':40,'strength':2,'agility':2,'wisdom':2,'talent':4,'language':3,'luck':10,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Randy','stats':{'energy':randint(1,9),'money':randint(100,900),'health':randint(10,90),'strength':randint(1,5),'agility':randint(1,5),'wisdom':randint(1,5),'talent':randint(1,5),'language':randint(1,5),'luck':randint(1,5),'badluck':randint(1,5),'fame':0,'item':['WierdMushroom']}},
                             {'name':'Reco','stats':{'energy':1,'money':1000,'health':10,'strength':-99,'agility':-99,'wisdom':999,'talent':0,'language':3,'luck':0,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Richard','stats':{'energy':4,'money':3000,'health':30,'strength':2,'agility':2,'wisdom':4,'talent':3,'language':3,'luck':3,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Sonic','stats':{'energy':5,'money':300,'health':70,'strength':2,'agility':13,'wisdom':-2,'talent':5,'language':3,'luck':3,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Stella','stats':{'energy':8,'money':700,'health':60,'strength':5,'agility':4,'wisdom':3,'talent':2,'language':3,'luck':1,'badluck':3,'fame':0,'item':[]}},
                             {'name':'Steve','stats':{'energy':5,'money':300,'health':30,'strength':2,'agility':4,'wisdom':7,'talent':3,'language':3,'luck':0,'badluck':5,'fame':0,'item':['Glasses']}},
                             {'name':'Winne','stats':{'energy':20,'money':5000,'health':10,'strength':10,'agility':10,'wisdom':10,'talent':10,'language':3,'luck':10,'badluck':3,'fame':50,'item':['Cheater`s Hat']}},
                             {'name':'Tester','stats':{'energy':3,'money':30,'health':30,'strength':0,'agility':3,'wisdom':3,'talent':3,'language':3,'luck':3,'badluck':3,'fame':0,'item':[]}},
                             ]
        self.background_list=['Village', #Lv1
                              'Town','School', #Lv2
                              'Farm','Port','Train', #Lv3
                              'Webcam','Club','Pub', #Lv4
                              'Bin', #Lv5
                              'Dungeon','Spaceshuttle', #Lv6
                              'Downtown', #Lv7
                              'Basement'] #Lv10
        self.level=''
        self.character={}
        
        self.type_num=0
        self.tax_mul=[10,100]
        self.tax_add=[0,0]
        self.background_num=0

        self.utility_num=3
        self.work_num=3
        self.store_num=3

    def before_start(self):
        setting=[]
        user=''
        
        while user not in self.type_list and user[len(user)-5:] not in self.type_list:
            user=input('choose type: ')
            try:
                if user not in self.type_list:
                    judge=int(user[:len(user)-5])
                    if user[len(user)-5:] not in self.type_list:
                        print('\nincorrect input\n')
            except:
                if user not in self.type_list:
                    print('\nincorrect input\n')
                    user=''

        while user not in self.level_list:
            user=input('choose level: ')
            if user not in self.level_list:
                print('\nincorrect input\n')

        self.level=user
                
        setting.append(user)

        run=True
        character={}

        while run:
            user=input('choose character: ')
            for Dict in self.character_list:
                if user in Dict['name']:
                    self.character=Dict
                    run=False
                    break
            if run:
                print('\nincorrect input\n')
        setting.append(0)

        while user not in self.background_list:
            user=input('choose background: ')
            if user not in self.background_list:
                print('\nincorrect input\n')
        setting.append(user)

        return setting

    def setting_game(self,setting):

        if setting[0][len(setting[0])-5:]=='-days':
            self.type_num=int(setting[0][:len(setting[0])-5])
        elif setting[0]=='Infinity':
            pass

        if self.level=='Normal':
            pass
        elif self.level=='Hard':
            self.tax_mul=[50,300]
        elif self.level=='Insane':
            self.tax_mul=[50,300]
            self.tax_add=[10/100,15/100]

        self.energy=self.character['stats']['energy']
        self.money=self.character['stats']['money']
        self.health=self.character['stats']['health']
        self.strength=self.character['stats']['strength']
        self.agility=self.character['stats']['agility']
        self.wisdom=self.character['stats']['wisdom']
        self.talent=self.character['stats']['talent']
        self.language=self.character['stats']['language']
        self.luck=self.character['stats']['luck']
        self.badluck=self.character['stats']['badluck']
        self.item+=self.character['stats']['item']

        for item in self.item:
            ev.bag(item)

        if setting[2]=='Village':
            self.background=0
        else:
            print('\nnot ready...auto choose...village')
            self.background=0

class event:
    def __init__(self):
        self.utility_list=[]
        self.work_list=[]
        self.good_event_list=[
            ['PickMoney','PickClover','Party','TakeMushroom']
            ]
        self.bad_event_list=[
            ['DropMoney','Fire']
            ]
        self.upgrade_list=['Energy','Utility_board','Work_board','Store_board','Stats','Luck']
        self.item_list=[{'name':'Cheater`s Hat','stats':{'durability':99,'health':-10},'price':None},
                        {'name':'MoonStone','stats':{'durability':10,'health':1},'price':500},
                        {'name':'Linger','stats':{'durability':3,'health':5},'price':800},
                        {'name':'NoteBook','stats':{'durability':7,'wisdom':1},'price':300},
                        {'name':'Dictionary','stats':{'durability':3,'wisdom':3},'price':500},
                        {'name':'Adronalin','stats':{'durability':3,'strength':3,'health':-2},'price':700},
                        {'name':'WierdMushroom','stats':{'durability':1,'random':3},'price':None},
                        {'name':'Sneakers','stats':{'durability':7,'agility':1},'price':300},
                        {'name':'Booster','stats':{'durability':1,'agility':5,'health':-2},'price':300},
                        {'name':'Translater','stats':{'durability':10,'language':1},'price':700},
                        {'name':'Hammer','stats':{'durability':7,'strength':1,'talent':1},'price':500},
                        {'name':'Glasses','stats':{'durability':10,'wisdom':1,'talent':1,'health':-1},'price':700},
                        {'name':'Scissor','stats':{'durability':3,'talent':2},'price':400},
                        {'name':'Mushroom','stats':{'durability':1,'health':10,'strength':5,'agility':-5},'price':1000},
                        {'name':'Clover','stats':{'durability':7,'luck':7,'badluck':-7},'price':3333}
                        ]
        self.command_list=['U_','W_']

    def bag(self,item):
        for Dict in self.item_list:
            if Dict['name']==item:
                gs.item_bag.append(deepcopy(Dict))
                break
    
    def make_list(self):
        if gs.background_num==0:
            for _ in range(5): self.utility_list+=[{'name':'Recycle','stats':{'money':[50]}}
                                                   ] 
            for _ in range(4): self.utility_list+=[{'name':'EnergyDrink_I','stats':{'energy':[1],'money':[-100]}},
                                                   {'name':'Lemonade','stats':{'energy':[-1],'money':[150]}},
                                                   {'name':'Weight_I','stats':{'energy':[-1],'strength':[1]}},
                                                   {'name':'Run_I','stats':{'energy':[-1],'agility':[1]}},
                                                   {'name':'Read_I','stats':{'energy':[-1],'wisdom':[1]}},
                                                   {'name':'Origami_I','stats':{'energy':[-1],'talent':[1]}},
                                                   {'name':'Talk_I','stats':{'energy':[-1],'language':[1]}}
                                                   ] 
            for _ in range(3): self.utility_list+=[{'name':'Medicine_I','stats':{'money':[-200],'health':[10]}}
                                                   ] 
            for _ in range(2): self.utility_list+=[{'name':'EnergyDrink_II','stats':{'energy':[2],'money':[-100]}},
                                                   {'name':'MowLawn','stats':{'energy':[-2],'money':[350]}},
                                                   {'name':'Weight_II','stats':{'energy':[-2],'strength':[2]}},
                                                   {'name':'Run_II','stats':{'energy':[-2],'agility':[2]}},
                                                   {'name':'Read_II','stats':{'energy':[-2],'wisdom':[2]}},
                                                   {'name':'Origami_II','stats':{'energy':[-2],'talent':[2]}},
                                                   {'name':'Talk_II','stats':{'energy':[-2],'language':[2]}},
                                                   {'name':'GoodNight','stats':{'next_energy':[1]}},
                                                   {'name':'MakeBed','stats':{'energy':[-1],'next_energy':[2]}},
                                                   {'name':'Volunteer','stats':{'energy':[-1],'money':[-100],'fame':[1]}},
                                                   {'name':'Steal','stats':{'energy':[-1],'money':[300],'fame':[-1]}}
                                                   ] 
            self.utility_list+=[{'name':'Medicine_II','stats':{'money':[-400],'health':[25]}}
                                ] 

            for _ in range(5): self.work_list+=[{'name':'Load_I','stats':{'earn':[round(gs.health*(gs.strength+ma.strength)/4)+self.tips(gs.strength+ma.strength)
                                                                                  ],
                                                                          'energy':[-1],'strength':[3]}},
                                                {'name':'Mail_I','stats':{'earn':[round(gs.health*(gs.agility+ma.agility)/4)+self.tips(gs.agility+ma.agility)
                                                                                  ],
                                                                          'energy':[-1],'agility':[3]}},
                                                {'name':'Library_I','stats':{'earn':[round(gs.health*(gs.wisdom+ma.wisdom)/4)+self.tips(gs.wisdom+ma.wisdom)
                                                                                  ],
                                                                          'energy':[-1],'wisdom':[3]}},
                                                {'name':'Curve_I','stats':{'earn':[round(gs.health*(gs.talent+ma.talent)/4)+self.tips(gs.talent+ma.talent)
                                                                                  ],
                                                                          'energy':[-1],'talent':[3]}},
                                                {'name':'Speach_I','stats':{'earn':[round(gs.health*(gs.language+ma.language)/4)+self.tips(gs.language+ma.language)
                                                                                  ],
                                                                          'energy':[-1],'language':[3]}}
                                                ] 
            for _ in range(4): self.work_list+=[] 
            for _ in range(3): self.work_list+=[{'name':'Load_II','stats':{'earn':[round(gs.health*(gs.strength+ma.strength)/1.8)+self.tips(gs.strength+ma.strength)
                                                                                  ],
                                                                          'energy':[-2],'strength':[7]}},
                                                {'name':'Mail_II','stats':{'earn':[round(gs.health*(gs.agility+ma.agility)/1.8)+self.tips(gs.agility+ma.agility)
                                                                                  ],
                                                                          'energy':[-2],'agility':[7]}},
                                                {'name':'Library_II','stats':{'earn':[round(gs.health*(gs.wisdom+ma.wisdom)/1.8)+self.tips(gs.wisdom+ma.wisdom)
                                                                                  ],
                                                                          'energy':[-2],'wisdom':[7]}},
                                                {'name':'Curve_II','stats':{'earn':[round(gs.health*(gs.talent+ma.talent)/1.8)+self.tips(gs.talent+ma.talent)
                                                                                  ],
                                                                          'energy':[-2],'talent':[7]}},
                                                {'name':'Speach_II','stats':{'earn':[round(gs.health*(gs.language+ma.language)/1.8)+self.tips(gs.language+ma.language)
                                                                                  ],
                                                                          'energy':[-2],'language':[7]}}
                                                ] 
            for _ in range(2): self.work_list+=[] 
            self.work_list+=[{'name':'Load_III','stats':{'earn':[round(gs.health*(gs.strength+ma.strength)/1.2)+self.tips(gs.strength+ma.strength)
                                                                                  ],
                                                                          'energy':[-3],'strength':[13]}},
                             {'name':'Mail_III','stats':{'earn':[round(gs.health*(gs.agility+ma.agility)/1.2)+self.tips(gs.agility+ma.agility)
                                                                                  ],
                                                                          'energy':[-3],'agility':[13]}},
                             {'name':'Library_III','stats':{'earn':[round(gs.health*(gs.wisdom+ma.wisdom)/1.2)+self.tips(gs.wisdom+ma.wisdom)
                                                                                  ],
                                                                          'energy':[-3],'wisdom':[13]}},
                             {'name':'Curve_III','stats':{'earn':[round(gs.health*(gs.talent+ma.talent)/1.2)+self.tips(gs.talent+ma.talent)
                                                                                  ],
                                                                          'energy':[-3],'talent':[13]}},
                             {'name':'Speach_III','stats':{'earn':[round(gs.health*(gs.language+ma.language)/1.2)+self.tips(gs.language+ma.language)
                                                                                  ],
                                                                          'energy':[-3],'language':[13]}}
                             ] 
            
    def choose_utility(self):
        return [choice(self.utility_list) for x in range(gs.utility_num)]
    
    def choose_work(self):
        return [choice(self.work_list) for x in range(gs.work_num)]

    def choose_upgrade(self):
        List=[choice(self.upgrade_list) for x in range(3)]
        
        print('0'*20,'\n')
        for i in List:
            print('-',end='')
            print(i)
        print('')
        print('0'*20)
        user=''
        while not user:
            try:
                user=int(input('Upgrade...'))
                if user<1 or user>3:
                    user=''
                    print('\nincorrect input\n')
            except:
                print('\nincorrect input\n')
        self.upgrade_value(List[user-1])
        
    def choose_event(self):
        List=[1 for x in range(gs.luck+ma.luck)]
        List+=[0 for x in range((gs.luck+ma.luck+gs.badluck+ma.badluck)*3)]
        for i in range(gs.luck+ma.luck):
            if List[i]:
                Luck=[]
                for _ in range(gs.luck+ma.luck):
                    Luck.append(choice(self.good_event_list[gs.background_num]))
                for _ in range(gs.badluck+ma.badluck):
                    Luck.append(choice(self.bad_event_list[gs.background_num]))
                List[i]=choice(Luck)
        self.event_value(choice(List))

    def choose_item(self):
        result=[]
        List=[0 for i in range(gs.store_num)]
        for _ in List:
            save=choice(self.item_list)
            if save['price']==None:
                List.append(0)
                continue
            result.append(save['name'])
        return result
        
    def utility_value(self,utility):
        if not utility['name']: return 1
        if 'energy' in utility['stats'].keys() and ma.player_energy<-1*utility['stats']['energy'][gs.background_num]: return 1
        if 'money' in utility['stats'].keys() and gs.money<-1*utility['stats']['money'][gs.background_num]: return 1
        if 'energy' in utility['stats'].keys(): ma.player_energy+=utility['stats']['energy'][gs.background_num]
        if 'next_energy' in utility['stats'].keys(): ma.next_energy+=utility['stats']['next_energy'][gs.background_num]
        if 'money' in utility['stats'].keys(): gs.money+=utility['stats']['money'][gs.background_num]
        if 'health' in utility['stats'].keys(): gs.health+=utility['stats']['health'][gs.background_num]
        if 'strength' in utility['stats'].keys(): gs.strength+=utility['stats']['strength'][gs.background_num]
        if 'agility' in utility['stats'].keys(): gs.agility+=utility['stats']['agility'][gs.background_num]
        if 'wisdom' in utility['stats'].keys(): gs.wisdom+=utility['stats']['wisdom'][gs.background_num]
        if 'talent' in utility['stats'].keys(): gs.talent+=utility['stats']['talent'][gs.background_num]
        if 'language' in utility['stats'].keys(): gs.language+=utility['stats']['language'][gs.background_num]
        if 'luck' in utility['stats'].keys(): gs.luck+=utility['stats']['luck'][gs.background_num]
        if 'badluck' in utility['stats'].keys(): gs.badluck+=utility['stats']['badluck'][gs.background_num]
        if 'fame' in utility['stats'].keys(): gs.fame+=utility['stats']['fame'][gs.background_num]
            
    def work_value(self,work):
        if not work['name']: return 1
        if ma.player_energy<-1*work['stats']['energy'][gs.background_num]: return 1
        if 'health' in work['stats'].keys() and gs.health<work['stats']['health'][gs.background_num]: return 1
        if 'strength' in work['stats'].keys() and gs.strength<work['stats']['strength'][gs.background_num]: return 1
        if 'agility' in work['stats'].keys() and gs.agility<work['stats']['agility'][gs.background_num]: return 1
        if 'wisdom' in work['stats'].keys() and gs.wisdom<work['stats']['wisdom'][gs.background_num]: return 1
        if 'talent' in work['stats'].keys() and gs.talent<work['stats']['talent'][gs.background_num]: return 1
        if 'language' in work['stats'].keys() and gs.language<work['stats']['language'][gs.background_num]: return 1
        if 'luck' in work['stats'].keys() and gs.luck<work['stats']['luck'][gs.background_num]: return 1
        if 'badluck' in work['stats'].keys() and gs.badluck<work['stats']['badluck'][gs.background_num]: return 1
        if 'fame' in work['stats'].keys() and gs.fame<work['stats']['fame'][gs.background_num]: return 1
        earn=work['stats']['earn'][gs.background_num]
        ma.earn+=earn
        print(earn)
        
    def upgrade_value(self,upgrade):
        if upgrade=='Energy': gs.energy+=1
        elif upgrade=='Utility_board': gs.utility_num+=1
        elif upgrade=='Work_board': gs.work_num+=1
        elif upgrade=='Store_board': gs.store_num+=1
        elif upgrade=='Stats':
            gs.health+=5
            gs.strength+=2
            gs.agility+=2
            gs.wisdom+=2
            gs.talent+=2
        elif upgrade=='Luck':
            gs.luck+=3

    def event_value(self,Event):
        print('')
        if Event=='PickMoney':
            earn=randint(30+3*(gs.luck+ma.luck),30+4*(gs.luck+ma.luck))
            gs.money+=earn
            print(f'You picked money!    money...+{earn}')
        elif Event=='PickClover':
            earn=randint(3,4)
            gs.luck+=earn
            print(f'You picked clover!    luck...+{earn}')
        elif Event=='Party':
            user=''
            while not user:
                user=input('Will you join in a party? (y/n): ')
                if user not in ['y','n']:
                    user=''
            if user=='y':
                List=[randint(50,100),randint(1,3)]
                gs.money-=List[0]
                ma.next_energy+=List[1]
                print(f'You had a fun!    next_energy...+{List[1]}\n                  money...-{List[0]}')
            elif user=='n':
                print('You turned down their offer.')
        elif Event=='TakeMushroom':
            List=[1 for x in range(gs.luck+ma.luck)]
            List+=[0 for x in range(gs.badluck+ma.badluck)]
            if choice(List):
                item='Mushroom'
            else:
                item='WierdMushroom'
            gs.item.append(item)
            ev.bag(item)
            print(f'You taked a {item}!')
                
        elif Event=='DropMoney':
            if gs.luck+ma.luck<100:
                loss=randint(3*(100-(gs.luck+ma.luck)),4*(100-(gs.luck+ma.luck)))
                gs.money-=loss
                print(f'You dropped money!    money...-{loss}')
            else:
                print(f'You dropped money,but someone picked it up for you!    money...-0')
        elif Event=='Fire':
            if gs.luck+ma.luck<200:
                loss=randint(5*(200-(gs.luck+ma.luck)),6*(200-(gs.luck+ma.luck)))
                gs.money-=loss
                print(f'Your house is on fire!    money...-{loss}')
            else:
                print(f'Your house is on fire,but someone helped you turn off the fire!    money...-0')
        else:
            print('Noting happend tonight')
        print('')

    def item_value(self,item):
        if item['stats']['durability']==0: return 1
        item['stats']['durability']-=1
        if 'energy' in item['stats'].keys(): ma.next_energy+=item['stats']['energy']
        if 'health' in item['stats'].keys(): ma.next_health+=item['stats']['health']
        if 'strength' in item['stats'].keys(): ma.strength+=item['stats']['strength']
        if 'agility' in item['stats'].keys(): ma.agility+=item['stats']['agility']
        if 'wisdom' in item['stats'].keys(): ma.wisdom+=item['stats']['wisdom']
        if 'talent' in item['stats'].keys(): ma.talent+=item['stats']['talent']
        if 'language' in item['stats'].keys(): ma.language+=item['stats']['language']
        if 'luck' in item['stats'].keys(): ma.luck+=item['stats']['luck']
        if 'badluck' in item['stats'].keys(): ma.badluck+=item['stats']['badluck']
        if 'random' in item['stats'].keys():
            Random=sample(['energy','health','strength','agility','wisdom','talent','language','luck','badluck'],item['stats']['random'])
            if 'energy' in Random: ma.next_energy+=randint(-2,2)
            if 'health'in Random: ma.next_health+=randint(-2,2)
            if 'strength'in Random: ma.strength+=randint(-2,2)
            if 'agility'in Random: ma.agility+=randint(-2,2)
            if 'wisdom'in Random: ma.wisdom+=randint(-2,2)
            if 'talent'in Random: ma.talent+=randint(-2,2)
            if 'language'in Random: ma.language+=randint(-2,2)
            if 'luck'in Random: ma.luck+=randint(-2,2)
            if 'badluck'in Random: ma.badluck+=randint(-2,2)
        
                
    def tips(self,stat):
        result=0
        List=[1 for x in range(gs.luck+ma.luck)]
        List+=[0 for x in range(gs.badluck+ma.badluck)]
        luck=sample(List,3)
        for i in luck:
            if i: result+=randint(1,gs.luck+ma.luck)*stat-(gs.badluck+ma.badluck)+fame
        return result
        
    def command(self):
        user=''
        while user[:2] not in self.command_list:
            user=input('command: ')
            try:
                test=int(user[2:])
            except:
                if user=='Nextday' or user=='Stats' or user=='End':
                    return user
                user=''
                print('\nincorrect input\n')
                continue
            if user[:2] not in self.command_list or int(user[2:])<1:
                print('\nincorrect input\n')
                user=''
            elif user[:2]=='U_':
                if int(user[2:])>gs.utility_num:
                    user=''
                    print('\nincorrect input\n')
            elif user[:2]=='W_':
                if int(user[2:])>gs.work_num:
                    user=''
                    print('\nincorrect input\n')

        return user[:2],int(user[2:])-1

    def bankrupt(self,days):
        if gs.money<0:
            print(f'''
 ∧∧∧∧
<backrupt>  You survived for {days}days
 ∨∨∨∨
''')
            return 1
        

class main:
    def __init__(self):
        self.experience=0
        self.combo=0
        self.days=1
        self.player_energy=0

        self.next_energy=0
        self.next_health=0
        self.strength=0
        self.agility=0
        self.wisdom=0
        self.talent=0
        self.language=0
        self.luck=0
        self.badluck=0
        
        self.earn=0
        self.rest=False
        
    def setting(self):
        setting=gs.before_start()
        gs.setting_game(setting)
        
    def day(self):
        self.player_energy=gs.energy+self.next_energy
        self.next_energy=0
        gs.health+=self.next_health
        self.next_health=0
        if gs.health<0:
            self.rest=True
            user='Nextday'
        if not self.rest:
            user=''
        List_U=ev.choose_utility()
        List_W=ev.choose_work()
        while not user=='Nextday':
            print('')
            print('0'*20)
            print('\nutility\n')
            for i in List_U:
                print('-',end='')
                print(i['name'])
            print('\nwork\n')
            for i in List_W:
                print('-',end='')
                print(i['name'])
            print('')
            print('0'*20,end='\n\n')
            
            user=ev.command()
            if user=='Stats':
                print(f'''
energy: {self.player_energy}
money: {gs.money}
health: {gs.health}
strength: {gs.strength}+({self.strength})
agility: {gs.agility}+({self.agility})
wisdom: {gs.wisdom}+({self.wisdom})
talent: {gs.talent}+({self.talent})
language: {gs.language}+({self.language})
luck: {gs.luck}+({self.luck})
badluck: {gs.badluck}+({self.badluck})
fame: {gs.fame}
item: {gs.item}''')
            elif user=='End':
                gs.money=0
                ma.earn=0
                user='Nextday'
            if type(user)=='str':
                continue
            if user[0]==ev.command_list[0]:
                pos=ev.utility_value(List_U[user[1]])
                if pos:
                    print('not available')
                else:
                    List_U[user[1]]={'name':''}
            elif user[0]==ev.command_list[1]:
                pos=ev.work_value(List_W[user[1]])
                if pos:
                    print('not available')
                else:
                    List_W[user[1]]={'name':''}
        gs.money+=self.earn
    def store(self):
        List_S=ev.choose_item()
        run=True
        print('0'*20)
        print('')
        for _ in List_S:
            print('-',end='')
            print(_,end='...')
            for Dict in ev.item_list:
                if Dict['name']==_:
                    price=Dict['price']
                    break
            print(price)
        print('')
        print('0'*20)
        while run:
            print(f'current money...{gs.money}',end='  ')
            user=''
            while not user and not user==0:
                try:
                    user=int(input('buy... '))
                    if user<0 or user>gs.store_num:
                        print('\nincorrect input\n')
                        user=''
                except:
                    print('\nincorrect input\n')
                    user=''
            if user==0:
                break
            else:
                user-=1
                if not List_S[user]:
                    print('not available')
                    continue
                for Dict in ev.item_list:
                    if Dict['name']==List_S[user]:
                        item=Dict
                        break
                if gs.money<item['price']:
                    print('not available')
                    continue
                gs.money-=item['price']
                gs.item.append(List_S[user])
                ev.bag(List_S[user])
                List_S[user]=0
            judge=0
            for i in List_S:
                if not i:
                    judge+=1
            if judge==len(List_S):
                break

#play
while True:
    gs=game_set()
    ev=event()
    ma=main()
    ma.setting()
    ev.make_list()
    
    if not gs.type_num:
        run_list=[0]
    else:
        run_list=[0 for x in range(gs.type_num)]
        
    days=1
    for _ in run_list:
        ma.strength=0
        ma.agility=0
        ma.wisdom=0
        ma.talent=0
        ma.language=0
        ma.luck=0
        ma.badluck=0
        
        List=[]
        for i in range(len(gs.item_bag)):
            judge=ev.item_value(gs.item_bag[i])
            if judge:
                List.append(i)
        List.reverse()
        for i in List:
            gs.item.remove(gs.item_bag[i]['name'])
            del gs.item_bag[i]
            
        print('')
        print('-'*20)
        if days%5==0:
            print(days,'day',f'    tax...{days*gs.tax_mul[1]}+{gs.tax_add[1]*100}%')
        else:
            print(days,'day',f'    tax...{days*gs.tax_mul[0]}+{gs.tax_add[0]*100}%')
        print('-'*20,end='')
            
        ma.day()

        if ma.rest:
            print('\nYou are too tired to work today.')
            gs.health+=10
            if gs.health>=20:
                ma.rest=False
        else:
            gs.health+=int((ma.player_energy+1-gs.energy)/1.2)

        ev.choose_event()

        if days%5==0: 
            tax=int(days*gs.tax_mul[1]+ma.earn*gs.tax_add[1])
        else:
            tax=int(days*gs.tax_mul[0]+ma.earn*gs.tax_add[0])
        gs.money-=tax

        judge=ev.bankrupt(days)
        if judge:
            break
        
        print(f'\nmoney...-{tax}')
        ma.earn=0
        
        if days%5==0:
            ev.choose_upgrade()

        if choice([0,1]):
            ma.store()
            
        days+=1
        if not gs.type_num:
            run_list.append(0)

    if days==gs.type_num:           
        print(f'\nYou have survived for {gs.type_num} days!\n')

    user=''
    while not user:
        user=input('continue? (y/n):')
        if user not in ['y','n']:
            user=''
    if user=='y':
        pass
    elif user=='n':
        print('\nThankYou for playing')
        break
    
