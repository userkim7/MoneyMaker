from random import randint,sample,choice

class game_set:
    def __init__(self):
        self.energy=5
        self.money=500
        self.health=50
        self.strength=3
        self.agility=3
        self.wisdom=3
        self.talent=3
        self.luck=3
        
        self.type_list=['40-days','80-days','infinity']
        self.character_list=['Alex','Bob','Emma','Genie','Lucy','Richard','Tester','_____']
        self.background_list=['village', #Lv1
                              'town','school', #Lv2
                              'farm','port','train', #Lv3
                              'webcam','club','pub', #Lv4
                              'bin', #Lv5
                              'dungeon', #Lv6
                              'downtown', #Lv7
                              'basement'] #Lv10

        self.type_num=0
        self.background_num=0

        self.utility_num=3
        self.work_num=3

    def before_start(self):
        setting=[]
        user=''
        
        while user not in self.type_list:
            user=input('choose type: ')
            if user not in self.type_list:
                print('\nincorrect input\n')
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

        if setting[0]=='40-days':
            self.type_num=40
        elif setting[0]=='80-days':
            self.type_num=80
        elif setting[0]=='infinity':
            pass

        if setting[1]=='Alex':
            pass
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
        elif setting[1]=='Genie':
            self.energy=3
            self.money=300
            self.health=30
            self.strength=2
            self.agility=2
            self.wisdom=13
            self.talent=5
            self.luck=4
        elif setting[1]=='Lucy':
            self.energy=3
            self.money=1000
            self.health=40
            self.strength=2
            self.agility=2
            self.wisdom=2
            self.talent=4
            self.luck=10
        elif setting[1]=='Richard':
            self.energy=4
            self.money=3000
            self.health=30
            self.strength=2
            self.agility=2
            self.wisdom=4
            self.talent=3
            self.luck=3
        elif setting[1]=='Tester':
            self.health=1
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

        if setting[2]=='village':
            self.background=0
        else:
            print('\nnot ready...auto choose...village')
            self.background=0

class event:
    def __init__(self):
        self.utility_list=[
            ['EnergyDrink_I','EnergyDrink_I','EnergyDrink_II', 
             'Recycle','Recycle','Lemonade','Lemonade','MowLawn', 
             'Medicine_I','Medicine_II', 
             'Weight_I','Weight_I','Weight_II', 
             'Run_I','Run_I','Run_II', 
             'Read_I','Read_I','Read_II', 
             'Origami_I','Origami_I','Origami_II' 
                ]
            ]
        self.work_list=[
            ['Load_I','Load_I','Load_I','Load_II','Load_II','Load_III', 
             'Mail_I','Mail_I','Mail_I','Mail_II','Mail_II','Mail_III', 
             'Library_I','Library_I','Library_I','Library_II','Library_II','Library_III', 
             'Curve_I','Curve_I','Curve_I','Curve_II','Curve_II','Curve_III' 
                ]
            ]
        self.good_event_list=[
            ['PickMoney','PickClover','Party']
            ]
        self.bad_event_list=[
            ['DropMoney','Fire']
            ]
        self.upgrade_list=['Energy','Utility_board','Work_board','Stats','Luck']
        self.command_list=['U_','W_']

    def choose_utility(self):
        result=[]
        for _ in range(gs.utility_num):
            result.append(choice(self.utility_list[gs.background_num]))
        return result

    def choose_work(self):
        result=[]
        for _ in range(gs.work_num):
            result.append(choice(self.work_list[gs.background_num]))
        return result

    def choose_upgrade(self):
        List=[]
        for _ in range(3):
            List.append(choice(self.upgrade_list))
        print('0'*70)
        print('')
        for i in List:
            print('-',end='')
            print(i)
        print('')
        print('0'*70)
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
        List=[x for x in range(1,gs.luck+1)]
        for _ in range(100):
            List.append(0)
        for i in range(len(List)):
            if List[i]:
                Luck=[]
                for _ in range(gs.luck):
                    Luck.append(choice(self.good_event_list))
                for _ in range(gs.luck+1):
                    Luck.append(choice(self.bad_event_list))
                List[i]=choice(Luck)
        self.event_value(choice(List))        
        
    def utility_value(self,utility):
        if utility=='EnergyDrink_I':
            List=[100,1]
            if gs.money>=List[0]:
                gs.money-=List[0]
                ma.player_energy+=List[1]
                print('Gulp,glup')
                print(f'''player_energy...+{List[1]}
money...-{List[0]}''')
                return 1
        elif utility=='EnergyDrink_II':
            List=[200,2]
            if gs.money>=List[0]:
                gs.money-=List[0]
                ma.player_energy+=List[1]
                print('Gulp,glup')
                print(f'''player_energy...+{List[1]}
money...-{List[0]}''')
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
                print(f'''money...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='MowLawn':
            List=[2,350]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.money+=List[1]
                print('Grrrrrrrrrrrr')
                print(f'''money...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='Medicine_I':
            List=[200,20]
            if gs.money>=List[0]:
                gs.money-=List[0]
                gs.health+=List[1]
                print('Ow,oww')
                print(f'''health...+{List[1]}
money...-{List[0]}''')
                return 1
        elif utility=='Medicine_II':
            List=[400,50]
            if gs.money>=List[0]:
                gs.money-=List[0]
                gs.health+=List[1]
                print('Ow,oww')
                print(f'''health...+{List[1]}
money...-{List[0]}''')
                return 1
        elif utility=='Weight_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.strength+=List[1]
                print('Happp')
                print(f'''strength...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='Weight_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.strength+=List[1]
                print('Happp')
                print(f'''strength...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='Run_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.agility+=List[1]
                print('Huf,huf')
                print(f'''agility...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='Run_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.agility+=List[1]
                print('Huf,huf')
                print(f'''agility...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='Read_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.wisdom+=List[1]
                print('......')
                print(f'''wisdom...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='Read_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.wisdom+=List[1]
                print('......')
                print(f'''wisdom...+{List[1]}
energy...-{List[0]}''')
                return 1
            return 0
        elif utility=='Origami_I':
            List=[1,1]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.talent+=List[1]
                print('Scrap,scrap')
                print(f'''talent...+{List[1]}
energy...-{List[0]}''')
                return 1
        elif utility=='Origami_II':
            List=[2,2]
            if ma.player_energy>=List[0]:
                ma.player_energy-=List[0]
                gs.talent+=List[1]
                print('Scrap,scrap')
                print(f'''talent...+{List[1]}
energy...-{List[0]}''')
                return 1           
        
    def work_value(self,work):
        if work=='Load_I':
            if gs.strength>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*gs.strength/2)+self.tips(gs.strength)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Load_II':
            if gs.strength>=7 and ma.player_energy>=2:
                ma.player_energy-=2
                earn=round(gs.health*gs.strength/1.7)+self.tips(gs.strength)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Load_III':
            if gs.strength>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*gs.strength/1.4)+self.tips(gs.strength)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Mail_I':
            if gs.agility>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*gs.agility/2)+self.tips(gs.agility)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Mail_II':
            if gs.agility>=7 and ma.player_energy>=2:
                ma.player_energy-=2
                earn=round(gs.health*gs.agility/1.7)+self.tips(gs.agility)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Mail_III':
            if gs.agility>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*gs.agility/1.4)+self.tips(gs.agility)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Library_I':
            if gs.wisdom>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*gs.wisdom/2)+self.tips(gs.wisdom)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Library_II':
            if gs.wisdom>=7 and ma.player_energy>=2:
                ma.player_energy-=1
                earn=round(gs.health*gs.wisdom/1.7)+self.tips(gs.wisdom)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Library_III':
            if gs.wisdom>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*gs.wisdom/1.4)+self.tips(gs.wisdom)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Curve_I':
            if gs.talent>=3 and ma.player_energy>=1:
                ma.player_energy-=1
                earn=round(gs.health*gs.talent/2)+self.tips(gs.talent)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Curve_II':
            if gs.talent>=7 and ma.player_energy>=2:
                ma.player_energy-=2
                earn=round(gs.health*gs.talent/1.7)+self.tips(gs.talent)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
        elif work=='Curve_III':
            if gs.talent>=13 and ma.player_energy>=3:
                ma.player_energy-=3
                earn=round(gs.health*gs.talent/1.4)+self.tips(gs.talent)
                gs.money+=earn
                print(f'money...+{earn}')
                return 1
            
    def upgrade_value(self,upgrade):
        if upgrade=='Energy':
            gs.energy+=1
        elif upgrade=='Utility_board':
            gs.utility_num+=1
        elif upgrade=='Work_board':
            gs.work_num+=1
        elif upgrade=='Stats':
            gs.health+=5
            gs.strength+=2
            gs.agility+=2
            gs.wisdom+=2
            gs.talent+=2
        elif upgrade=='Luck':
            gs.luck+=3

    def event_value(self,Event):
        if Event=='PickMoney':
            earn=randint(30*gs.luck,31*gs.luck)
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
                print(f'''You had a fun!    next_energy...+{List[1]}
                  money...-{List[0]}''')
            elif user=='n':
                print('You turned down their offer.')
        elif Event=='DropMoney':
            if gs.luck<100:
                loss=randint(3*(100-gs.luck),4*(100-gs.luck))
                gs.money-=loss
                print(f'You dropped money!    money...-{loss}')
            else:
                print(f'You dropped money,but someone picked it up for you!    money...-0')
        elif Event=='Fire':
            if gs.luck<200:
                loss=randint(5*(200-gs.luck),6*(200-gs.luck))
                gs.money-=loss
                print(f'Your house is on fire!    money...-{loss}')
            else:
                print(f'Your house is on fire,but someone helped you turn off the fire!    money...-0')
                
    def tips(self,stat):
        result=0
        if gs.luck<100:
            List=[int(gs.luck/x) for x in range(1,101)]
        else:
            List=[x for x in range(1,101)]
        luck=sample(List,3)
        for i in luck:
            if i:
                result+=randint(1,gs.luck)*stat
        return result
        
    def command(self):
        user=''
        while user[:2] not in self.command_list:
            user=input('command: ')
            try:
                test=int(user[2:])
            except:
                if user=='NextDay' or user=='Stats' or user=='End':
                    return user
                user=''
                print('\nincorrect input\n')
                continue
            if user[:2] not in self.command_list or int(user[2:])<1:
                print('\nincorrect input\n')
                user=''
            elif user[:2]=='U_':
                if int(user[2:])>ma.utility_num:
                    user=''
                    print('\nincorrect input\n')
            elif user[:2]=='W_':
                if int(user[2:])>ma.work_num:
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
        self.utility_num=3
        self.work_num=3
        self.rest=False
        
    def help(self):
        user=''
        while not user:
            user=input('help? (y/n): ')
            if user not in ['y','n']:
                print('\nincorrect input\n')
                user=''
                
        if user=='y':
            print('''
Type:gamemode

40-days:survive for 40 days

80-days:survive for 80 days

infinity:test your luck


character:different stats

Alex the normal
just as defalut
energy...5   money..500
health..50   strength.3
agility..3   wisdom...3
talent...3   luck.....3

Bob the strong
strong but foolish
energy...7   money..500
health.100   strength.7
agility..7   wisdom..-3
talent...0   luck.....1

Emma the energetic
energetic but unlucky
energy..13   money..200
health..70   strength.5
agility..5   wisdom...2
talent...2   luck.....0

Genie the smart
smart but weak
energy...3   money..300
health..30   strength.2
agility..2   wisdom..13
talent...5   luck.....4

Lucy the lucky
lucky but weak
energy...3   money.1000
health..40   strength.2
agility..2   wisdom...2
talent...4   luck....10

Richard the rich
rich but weak
energy...4   money.3000
health..30   strength.2
agility..2   wisdom...4
talent...3   luck....3


background:level(1~7) (# means not ready)

recommended for beginner
    village(Lv1):cosy and relaxing

    #town(Lv2):busy but peaceful

    #school(Lv2):nice and famed school

recommended for normal player
    #farm(Lv3):animal lover

    #port(Lv3):out to sea

    #train(Lv3):no way to get off

    #webcam(Lv4):attention please

    #club(Lv4):dance time

    #pub(Lv4):drick until morning

recommended for expert
    #bin(Lv5):deliquent school

    #dungeon(Lv6):another world

not recommended
    #downtown(Lv7):dark and the darkest town

    #basement(Lv10):DO NOT ENTER


''')
            
    def setting(self):
        setting=gs.before_start()
        gs.setting_game(setting)
        
    def day(self):
        if gs.health<0:
            self.rest=True
            user='NextDay'
        else:
            user=''
        List_U=ev.choose_utility()
        List_W=ev.choose_work()
        self.player_energy=gs.energy+self.next_energy
        self.next_energy=0
        while not user=='NextDay':
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
            print('0'*20)
            print('')
            
            user=ev.command()
            if user=='Stats':
                print(f'''
energy: {self.player_energy}
money: {gs.money}
health: {gs.health}
strength: {gs.strength}
agility: {gs.agility}
wisdom: {gs.wisdom}
talent: {gs.talent}
luck: {gs.luck}''')
            elif user=='End':
                gs.money=0
                user='NextDay'
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

#play
while True:
    gs=game_set()
    ev=event()
    ma=main()
    ma.help()
    ma.setting()
    run_list=[]
    if not gs.type_num:
        run_list.append(0)
    else:
        for _ in range(gs.type_num):
            run_list.append(0)
    days=1
    for _ in run_list:
        if days%5==0:
            tax=days*100
        else:
            tax=days*10    
        print('')
        print('-'*20)
        print(days,'day',f'    tax...{tax}')
        print('-'*20,end='')
            
        ma.day()

        if ma.rest:
            print('\nYou are too tired to work today.')
            gs.health+=10
            if gs.health>=20:
                ma.rest=False
        else:
            gs.health+=int((ma.player_energy+1-gs.energy)/2)
              
        gs.money-=tax
        print(f'\nmoney...-{tax}')
        judge=ev.bankrupt(days)
        if judge:
            break
        if days%5==0:
            ev.choose_upgrade()

        days+=1
        if not gs.type_num:
            run_list.append(0)

    if days==gs.type_num:           
        print(f'''
You have survived for {gs.type_num} days! 
''')

    user=''
    while not user:
        user=input('continue? (y/n):')
        if user not in ['y','n']:
            user=''

    if user=='y':
        pass
    elif user=='n':
        print('ThankYou for playing')
        break
    
