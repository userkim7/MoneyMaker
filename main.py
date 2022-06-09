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
        self.character_list=['Alex','Arina','Bob','Emma','Fred','Genie','Lucid','Lucy','Randy','Reco','Richard','Sonic','Stella','Steve','Winne','Tester','_____']
        self.background_list=['Village', #Lv1
                              'Town','School', #Lv2
                              'Farm','Port','Train', #Lv3
                              'Webcam','Club','Pub', #Lv4
                              'Bin', #Lv5
                              'Dungeon','Spaceshuttle', #Lv6
                              'Downtown', #Lv7
                              'Basement'] #Lv10
        self.level=''
        
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

        while user not in self.character_list:
            user=input('choose character: ')
            if user not in self.character_list:
                print('\nincorrect input\n')
        setting.append(user)

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

        if setting[1]=='Alex':
            pass
        elif setting[1]=='Arina':
            self.energy=3
            self.money=100
            self.health=10
            self.strength=-99
            self.agility=-99
            self.wisdom=0
            self.talent=99
            self.luck=5
            self.item.append('Scissor')
        elif setting[1]=='Bob':
            self.energy=7
            self.money=500
            self.health=100
            self.strength=7
            self.agility=7
            self.wisdom=-3
            self.talent=0
            self.luck=1
        elif setting[1]=='Emma':
            self.energy=13
            self.money=200
            self.health=70
            self.strength=5
            self.agility=5
            self.wisdom=2
            self.talent=2
            self.luck=0
        elif setting[1]=='Fred':
            self.energy=7
            self.money=300
            self.health=70
            self.strength=8
            self.agility=5
            self.wisdom=1
            self.talent=5
            self.luck=3
        elif setting[1]=='Genie':
            self.energy=3
            self.money=300
            self.health=30
            self.strength=2
            self.agility=2
            self.wisdom=13
            self.talent=5
            self.luck=4
        elif setting[1]=='Lucid':
            self.energy=0
            self.money=1000
            self.health=100
            self.strength=-99
            self.agility=-99
            self.wisdom=-99
            self.talent=-99
            self.luck=999
        elif setting[1]=='Lucy':
            self.energy=3
            self.money=1000
            self.health=40
            self.strength=2
            self.agility=2
            self.wisdom=2
            self.talent=4
            self.luck=10
        elif setting[1]=='Randy':
            self.energy=randint(1,9)
            self.money=randint(100,900)
            self.health=randint(10,90)
            self.strength=randint(1,5)
            self.agility=randint(1,5)
            self.wisdom=randint(1,5)
            self.talent=randint(1,5)
            self.language=randint(1,5)
            self.luck=randint(1,5)
            self.badluck=randint(1,5)
            self.item.append('WierdMushroom')
        elif setting[1]=='Reco':
            self.energy=1
            self.money=1000
            self.health=10
            self.strength=-99
            self.agility=-99
            self.wisdom=999
            self.talent=0
            self.luck=0
        elif setting[1]=='Richard':
            self.energy=4
            self.money=3000
            self.health=30
            self.strength=2
            self.agility=2
            self.wisdom=4
            self.talent=3
            self.luck=3
        elif setting[1]=='Sonic':
            self.energy=5
            self.money=300
            self.health=70
            self.strength=2
            self.agility=13
            self.wisdom=-2
            self.talent=5
            self.luck=3
        elif setting[1]=='Stella':
            self.energy=8
            self.money=700
            self.health=60
            self.strength=5
            self.agility=4
            self.wisdom=3
            self.talent=2
            self.luck=1
        elif setting[1]=='Steve':
            self.energy=5
            self.money=300
            self.health=30
            self.strength=2
            self.agility=4
            self.wisdom=7
            self.talent=3
            self.luck=0
            self.badluck=5
            self.item.append('Glasses')
        elif setting[1]=='Winne':
            self.energy=20
            self.money=10000
            self.health=10
            self.strength=10
            self.agility=10
            self.wisdom=10
            self.talent=10
            self.luck=10
            self.item.append('Cheater`s Hat')
        elif setting[1]=='Tester':
            self.money=1
        elif setting[1]=='_____':
            try:
                user=int(input('code: ')) #1590
            except:
                pass
            if user==1590: 
                self.energy=999
                self.money=99999
                self.health=9999
                self.strength=999
                self.agility=999
                self.wisdom=999
                self.talent=999
                self.luck=999

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
                        {'name':'lover','stats':{'durability':7,'luck':7,'badluck':-7},'price':3333}
                        ]
        self.command_list=['U_','W_']

    def bag(self,item):
        for Dict in self.item_list:
            if Dict['name']==item:
                gs.item_bag.append(deepcopy(Dict))
                break
    
    def make_list(self):
        if gs.background_num==0:
            for _ in range(5): self.utility_list+=['Recycle'] #5
            for _ in range(4): self.utility_list+=['EnergyDrink_I','Lemonade','Weight_I','Run_I','Read_I','Origami_I'] #4
            for _ in range(3): self.utility_list+=['Medicine_I'] #3
            for _ in range(2): self.utility_list+=['EnergyDrink_II','MowLawn','Weight_II','Run_II','Read_II','Origami_II','GoodNight','MakeBed'] #2
            self.utility_list+=['Medicine_II'] #1

            for _ in range(5): self.work_list+=['Load_I','Mail_I','Library_I','Curve_I'] #5
            for _ in range(4): self.work_list+=[] #4
            for _ in range(3): self.work_list+=['Load_II','Mail_II','Library_II','Curve_II'] #3
            for _ in range(2): self.work_list+=[] #2
            self.work_list+=['Load_III','Mail_III','Library_III','Curve_III'] #1
            
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
        if utility=='EnergyDrink_I':
            List=[100,1]
            if gs.money>=List[0]:
                gs.money-=List[0]
                ma.player_energy+=List[1]
                print('Gulp,glup')
                print(f'energy...+{List[1]}\nmoney...-{List[0]}')
                return 1
        elif utility=='EnergyDrink_II':
            List=[200,2]
            if gs.money>=List[0]:
                gs.money-=List[0]
                ma.player_energy+=List[1]
                print('Gulp,glup')
                print(f'energy...+{List[1]}\nmoney...-{List[0]}')
                return 1
        elif utility=='Recycle':
            List=[50]
            gs.money+=List[0]
            print('Tang,tang')
            print(f'money...+{List[0]}')
            return 1
        elif utility=='Lemonade':
            List=[1,150]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.money+=List[1]
                print('Sweet Lemonade!')
                print(f'money...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='MowLawn':
            List=[2,350]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.money+=List[1]
                print('Grrrrrrrrrrrr')
                print(f'money...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='Medicine_I':
            List=[200,10]
            if gs.money>=List[0]:
                gs.money-=List[0]
                gs.health+=List[1]
                print('Ow,oww')
                print(f'health...+{List[1]}\nmoney...-{List[0]}')
                return 1
        elif utility=='Medicine_II':
            List=[400,25]
            if gs.money>=List[0]:
                gs.money-=List[0]
                gs.health+=List[1]
                print('Ow,oww')
                print(f'health...+{List[1]}\nmoney...-{List[0]}')
                return 1
        elif utility=='Weight_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.strength+=List[1]
                print('Happp')
                print(f'strength...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='Weight_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.strength+=List[1]
                print('Happp')
                print(f'strength...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='Run_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.agility+=List[1]
                print('Huf,huf')
                print(f'agility...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='Run_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.agility+=List[1]
                print('Huf,huf')
                print(f'agility...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='Read_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.wisdom+=List[1]
                print('......')
                print(f'wisdom...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='Read_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.wisdom+=List[1]
                print('......')
                print(f'wisdom...+{List[1]}\nenergy...-{List[0]}')
                return 1
            return 0
        elif utility=='Origami_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.talent+=List[1]
                print('Scrap,scrap')
                print(f'talent...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='Origami_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.talent+=List[1]
                print('Scrap,scrap')
                print(f'talent...+{List[1]}\nenergy...-{List[0]}')
                return 1
        elif utility=='GoodNight':
            List=[1]
            ma.next_energy+=List[0]
            print('Good Night!')
            print(f'next_energy...+{List[0]}')
            return 1
        elif utility=='MakeBed':
            List=[1,2]
            ma.player_energy-=List[0]
            ma.next_energy+=List[1]
            print('Making bed!')
            print(f'next_energy...+{List[1]}\nenergy...-{List[0]}')
            return 1
            
    def work_value(self,work):
        if work=='Load_I':
            if gs.strength+ma.strength>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*(gs.strength+ma.strength)/8)+self.tips(gs.strength+ma.strength)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Load_II':
            if gs.strength+ma.strength>=7 and ma.player_energy>=2:
                ma.player_energy-=2
                earn=round(gs.health*(gs.strength+ma.strength)/3.2)+self.tips(gs.strength+ma.strength)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Load_III':
            if gs.strength+ma.strength>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*(gs.strength+ma.strength)/1.4)+self.tips(gs.strength+ma.strength)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Mail_I':
            if gs.agility+ma.agility>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*(gs.agility+ma.agility)/8)+self.tips(gs.agility+ma.agility)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Mail_II':
            if gs.agility+ma.agility>=7 and ma.player_energy>=2:
                ma.player_energy-=2
                earn=round(gs.health*(gs.agility+ma.agility)/3.2)+self.tips(gs.agility+ma.agility)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Mail_III':
            if gs.agility+ma.agility>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*(gs.agility+ma.agility)/1.4)+self.tips(gs.agility+ma.agility)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Library_I':
            if gs.wisdom+ma.wisdom>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*(gs.wisdom+ma.wisdom)/8)+self.tips(gs.wisdom+ma.wisdom)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Library_II':
            if gs.wisdom+ma.wisdom>=7 and ma.player_energy>=2:
                ma.player_energy-=1
                earn=round(gs.health*(gs.wisdom+ma.wisdom)/3.2)+self.tips(gs.wisdom+ma.wisdom)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Library_III':
            if gs.wisdom+ma.wisdom>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*(gs.wisdom+ma.wisdom)/1.4)+self.tips(gs.wisdom+ma.wisdom)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Curve_I':
            if gs.talent+ma.talent>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*(gs.talent+ma.talent)/8)+self.tips(gs.talent+ma.talent)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Curve_II':
            if gs.talent+ma.talent>=7 and ma.player_energy>=2:
                ma.player_energy-=2
                earn=round(gs.health*(gs.talent+ma.talent)/3.2)+self.tips(gs.talent+ma.talent)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
        elif work=='Curve_III':
            if gs.talent+ma.talent>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*(gs.talent+ma.talent)/1.4)+self.tips(gs.talent+ma.talent)
                ma.earn+=earn
                print(f'earn...+{earn}')
                return 1
            
    def upgrade_value(self,upgrade):
        if upgrade=='Energy':
            gs.energy+=1
        elif upgrade=='Utility_board':
            gs.utility_num+=1
        elif upgrade=='Work_board':
            gs.work_num+=1
        elif upgrade=='Store_board':
            gs.store_num+=1
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
        if item['stats']['durability']==0:
            return 1
        item['stats']['durability']-=1
        if 'energy' in item['stats'].keys():
            ma.next_energy+=item['stats']['energy']
        if 'health' in item['stats'].keys():
            ma.next_health+=item['stats']['health']
        if 'strength' in item['stats'].keys():
            ma.strength+=item['stats']['strength']
        if 'agility' in item['stats'].keys():
            ma.agility+=item['stats']['agility']
        if 'wisdom' in item['stats'].keys():
            ma.wisdom+=item['stats']['wisdom']
        if 'talent' in item['stats'].keys():
            ma.talent+=item['stats']['talent']
        if 'language' in item['stats'].keys():
            ma.language+=item['stats']['language']
        if 'luck' in item['stats'].keys():
            ma.luck+=item['stats']['luck']
        if 'badluck' in item['stats'].keys():
            ma.badluck+=item['stats']['badluck']
        if 'random' in item['stats'].keys():
            Random=sample(['energy','health','strength','agility','wisdom','talent','language','luck','badluck'],item['stats']['random'])
            if 'energy' in Random:
                ma.next_energy+=randint(-2,2)
            if 'health'in Random:
                ma.next_health+=randint(-2,2)
            if 'strength'in Random:
                ma.strength+=randint(-2,2)
            if 'agility'in Random:
                ma.agility+=randint(-2,2)
            if 'wisdom'in Random:
                ma.wisdom+=randint(-2,2)
            if 'talent'in Random:
                ma.talent+=randint(-2,2)
            if 'language'in Random:
                ma.language+=randint(-2,2)
            if 'luck'in Random:
                ma.luck+=randint(-2,2)
            if 'badluck'in Random:
                ma.badluck+=randint(-2,2)
        
                
    def tips(self,stat):
        result=0
        if gs.luck<100:
            List=[int((gs.luck+ma.luck)/x) for x in range(1,101)]
        else:
            List=[x for x in range(1,101)]
        luck=sample(List,3)
        for i in luck:
            if i:
                result+=randint(1,gs.luck+ma.luck)*stat
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
                print(i)
            print('\nwork\n')
            for i in List_W:
                print('-',end='')
                print(i)
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
                    List_U[user[1]]=''
                else:
                    print('not available')
            elif user[0]==ev.command_list[1]:
                pos=ev.work_value(List_W[user[1]])
                if pos:
                    List_W[user[1]]=''
                else:
                    print('not available')
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
    
