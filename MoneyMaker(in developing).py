import random
import copy
import os
import time
import msvcrt

#□■▣▩▦◈⊙Ξ▤▥▧▨⛋⚿☒◆◇◎●▲△▼▽☖☗⛉⛊☰☱☲☳☴☵☶☷▀▁▂▃▄▅▆▇█▉▊▋▌▍▎✪
#┻┣┫┏┓╋┃
'''
☗
┃
☗
┣ ┓
☗ ☖
┣ ┓
☖ ☗
┏ ╋ ┓
☗ ☖ ☖

{'name':'Randy','stats':{'energy':randint(1,9),'money':randint(100,900),'health':randint(10,90),'str':randint(1,5),'agi':randint(1,5),'wis':randint(1,5),'tal':randint(1,5),'luck':randint(1,5),'fame':0,'item':['WierdMushroom']}},
'''
##################################################
class Function:
    def __init__(self):
        self.stats_show=False
        
    def list(self,Str,List,Check):
        Name=[Dict['name'] for Dict in List]
        Description=[]
        if 'description' in List[0]: Description=[Dict['description'] for Dict in List]
        
        run=True
        user=0
        
        while run:
            if self.stats_show: self.stats()
            print('\n'+Str)
            for Num in range(len(Name)):
                if Num==user:
                    if Check[Num]!='▩':
                        print('▣'+Name[Num])
                        if Description: print('ㄴ'+Description[Num])
                    else:
                        print('▦'+Name[Num])
                        print('ㄴNot available!')
                else: print(Check[Num]+Name[Num])
            key=msvcrt.getch()
            if key=='\xe0': key=msvcrt.getch()
            elif key==b'\r':
                if Check[user]!='▩': run=False
            if key==b'H' and user>0: user-=1
            elif key==b'P' and user<len(Name)-1: user+=1
            os.system('cls')

        return user

    def bar(self,Str,Num):
        Stat=str(Num)
        if Num<0: Num=0
        if Str=='Energy ': print(Str+'■'*player.energy_left+'□'*(player.energy-player.energy_left))
        elif Str=='Money  ': print(Str+'█'*(Num//140)+['','▎','▍','▌','▋','▊','▉'][int(Num%140/20)]+Stat)
        elif Str=='Health ': print(Str+'█'*(Num//14)+['','▎','▍','▌','▋','▊','▉'][int(Num%14/2)]+Stat)
        else: print(Str+'█'*(Num//7)+['','▎','▍','▌','▋','▊','▉'][Num%7]+Stat)

    def stats(self):
        print(player.name+', '+game.map+'\n'+'-'*20)
        self.bar('Energy ',0)
        self.bar('Money  ',player.money)
        self.bar('Health ',player.health)
        self.bar('Str  ',player.str)
        self.bar('Agi  ',player.agi)
        self.bar('Wis  ',player.wis)
        self.bar('Tal  ',player.tal)
        self.bar('Luck ',player.luck)
        self.bar('Fame ',player.fame)
        print('Bag '+str([Item['name'] for Item in player.bag]))

    def description_bar(self,Str,Num):
        Stat=str(Num)
        if Num<0: Num=0
        if Str=='Energy ': return Str+'■'*Num
        elif Str=='Money  ': return Str+'█'*(Num//140)+['','▎','▍','▌','▋','▊','▉'][int(Num%140/20)]+Stat
        elif Str=='Health ': return Str+'█'*(Num//14)+['','▎','▍','▌','▋','▊','▉'][int(Num%14/2)]+Stat
        else: return Str+'█'*(Num//7)+['','▎','▍','▌','▋','▊','▉'][Num%7]+Stat

    def character_description(self,Stats):
        return f'''{self.description_bar('Energy ',Stats['energy'])}
  {self.description_bar('Money  ',Stats['money'])}
  {self.description_bar('Health ',Stats['health'])}
  {self.description_bar('Str  ',Stats['str'])}
  {self.description_bar('Agi  ',Stats['agi'])}
  {self.description_bar('Wis  ',Stats['wis'])}
  {self.description_bar('Tal  ',Stats['tal'])}
  {self.description_bar('Luck ',Stats['luck'])}
  {self.description_bar('Fame ',Stats['fame'])}
  {'Bag '+str(Stats['item'])}'''


class Setting:
    def __init__(self):
        self.map_list=[{'name':'Village','usable':'□','description':'✪ soft and easy','list':[[0,4],[1,4],[2,4],[3,4],[4,3],[5,3],[6,3],[7,3],[8,4],[9,2],[10,5],[11,3],[12,1],[13,3],[14,2],[15,3],[16,1],[17,2],[18,2]]},
                       {'name':'Town','usable':'▩','description':'✪✪'},
                       {'name':'School','usable':'▩','description':'✪✪'},
                       {'name':'Farm','usable':'▩','description':'✪✪✪'},
                       {'name':'Port','usable':'▩','description':'✪✪✪'},
                       {'name':'Train','usable':'▩','description':'✪✪✪'},
                       {'name':'Streaming','usable':'▩','description':'✪✪✪✪'},
                       {'name':'Club','usable':'▩','description':'✪✪✪✪'},
                       {'name':'Pub','usable':'▩','description':'✪✪✪✪'},
                       {'name':'Bin','usable':'▩','description':'✪✪✪✪✪'},
                       {'name':'Lab','usable':'▩','description':'✪✪✪✪✪'},
                       {'name':'Dungeon','usable':'▩','description':'✪✪✪✪✪✪✪'},
                       {'name':'Spacestation','usable':'▩','description':'✪✪✪✪✪✪✪'},
                       {'name':'Downtown','usable':'▩','description':'✪✪✪✪✪✪✪'},
                       {'name':'Basement','usable':'▩','description':'✪✪✪✪✪✪✪✪✪✪✪'},
                       {'name':'Hell','usable':'▩','description':'✪✪✪✪✪✪✪✪✪✪✪'}
                       ]
        self.map={}

        self.character_list=[{'name':'Alex','usable':'□','stats':{'energy':5,'money':500,'health':50,'str':3,'agi':3,'wis':3,'tal':3,'luck':3,'fame':0,'item':[]}},
                             {'name':'Bob','usable':'□','stats':{'energy':7,'money':500,'health':100,'str':7,'agi':7,'wis':-3,'tal':0,'luck':1,'fame':0,'item':[]}},
                             {'name':'Lucy','usable':'□','stats':{'energy':3,'money':1000,'health':40,'str':2,'agi':2,'wis':2,'tal':4,'luck':10,'fame':0,'item':[]}},
                             {'name':'Richard','usable':'□','stats':{'energy':4,'money':3000,'health':30,'str':2,'agi':2,'wis':4,'tal':3,'luck':3,'fame':0,'item':[]}},
                             {'name':'Arina','usable':'□','stats':{'energy':3,'money':100,'health':10,'str':-99,'agi':-99,'wis':0,'tal':99,'luck':5,'fame':0,'item':['Scissor']}},
                             {'name':'Emma','usable':'□','stats':{'energy':13,'money':200,'health':70,'str':5,'agi':5,'wis':2,'tal':2,'luck':0,'fame':0,'item':[]}},
                             {'name':'Fred','usable':'□','stats':{'energy':7,'money':300,'health':70,'str':8,'agi':5,'wis':1,'tal':5,'luck':3,'fame':0,'item':[]}},
                             {'name':'Genie','usable':'□','stats':{'energy':3,'money':300,'health':30,'str':2,'agi':2,'wis':13,'tal':5,'luck':4,'fame':0,'item':[]}},
                             {'name':'Lucid','usable':'□','stats':{'energy':0,'money':1000,'health':100,'str':-99,'agi':-99,'wis':-99,'tal':-99,'luck':999,'fame':0,'item':[]}},
                             {'name':'Reco','usable':'□','stats':{'energy':1,'money':1000,'health':10,'str':-99,'agi':-99,'wis':999,'tal':0,'luck':0,'fame':0,'item':[]}},
                             {'name':'Sonic','usable':'□','stats':{'energy':5,'money':300,'health':70,'str':2,'agi':13,'wis':-2,'tal':5,'luck':3,'fame':0,'item':[]}},
                             {'name':'Stella','usable':'□','stats':{'energy':8,'money':700,'health':60,'str':5,'agi':4,'wis':3,'tal':2,'luck':1,'fame':0,'item':[]}},
                             {'name':'Steve','usable':'□','stats':{'energy':5,'money':300,'health':30,'str':2,'agi':4,'wis':7,'tal':3,'luck':0,'fame':0,'item':['Glasses']}},
                             {'name':'Winne','usable':'□','stats':{'energy':20,'money':5000,'health':10,'str':10,'agi':10,'wis':10,'tal':10,'luck':10,'fame':10,'item':['Cheater`s Hat','Linger']}},
                             {'name':'Tester','usable':'▩','stats':{'energy':3,'money':200,'health':30,'str':0,'agi':3,'wis':3,'tal':3,'luck':3,'fame':0,'item':[]}},
                             ]
        for Character in self.character_list: Character['description']=function.character_description(Character['stats'])
        self.character={}
        
    def choose_map(self):
        Check=[Map['usable'] for Map in self.map_list]
        Num=function.list('Choose Your Map\n',self.map_list,Check)
        self.map=copy.deepcopy(self.map_list[Num])
        game.map=self.map_list[Num]['name']

    def choose_character(self):
        Check=[Character['usable'] for Character in self.character_list]
        Num=function.list('Choose Your Character\n',self.character_list,Check)
        self.character=copy.deepcopy(self.character_list[Num])
        player.name=self.character_list[Num]['name']

    def set_character(self):
        player.energy=self.character['stats']['energy']
        player.energy_left=self.character['stats']['energy']
        player.money=self.character['stats']['money']
        player.health=self.character['stats']['health']
        player.str=self.character['stats']['str']
        player.agi=self.character['stats']['agi']
        player.wis=self.character['stats']['wis']
        player.tal=self.character['stats']['tal']
        player.luck=self.character['stats']['luck']
        player.fame=self.character['stats']['fame']
        #player.bag+=self.character['stats']['item']

    def set_utility(self):
        for List in self.map['list']:
            for _ in range(List[1]):
                game.utility_list.append(event.utility_list[List[0]])
        

class Main:
    def __init__(self):
        self.gem=0


class Game:
    def __init__(self):
        self.map=''

        self.utility_list=[]
        
        self.total_earn=0
        self.utility_num=3
        self.work_num=3
        self.store_num=3

    def list_utility(self):
        List=copy.deepcopy(event.set_utility())
        Check=['□','□','□']
        Num=function.list('Utility\n',List,Check)


class Event:
    def __init__(self):
        self.item_list=[{},
                        ]
        self.event_list=[{},
                         ]
        self.utility_list=[{'name':'Weight_I','stats':{'energy':-1,'strength':1}}, 
                           {'name':'Run_I','stats':{'energy':-1,'agility':1}},
                           {'name':'Read_I','stats':{'energy':-1,'wisdom':1}},
                           {'name':'Origami_I','stats':{'energy':-1,'talent':1}},
                           {'name':'Weight_II','stats':{'energy':-2,'strength':2}},
                           {'name':'Run_II','stats':{'energy':-2,'agility':2}},
                           {'name':'Read_II','stats':{'energy':-2,'wisdom':2}},
                           {'name':'Origami_II','stats':{'energy':-2,'talent':2}},
                           {'name':'EnergyDrink_I','stats':{'energy':1,'money':-20}},
                           {'name':'EnergyDrink_II','stats':{'energy':2,'money':-40}},
                           {'name':'Recycle','stats':{'money':50}},
                           {'name':'Lemonade','stats':{'energy':-1,'money':150}},
                           {'name':'MowLawn','stats':{'energy':-2,'money':350}},
                           {'name':'GoodNight','stats':{'next_energy':1}},
                           {'name':'MakeBed','stats':{'energy':-1,'next_energy':2}},
                           {'name':'Medicine_I','stats':{'money':-80,'health':10}},
                           {'name':'Medicine_II','stats':{'money':-160,'health':25}},
                           {'name':'Volunteer','stats':{'energy':-1,'money':-40,'fame':1}},
                           {'name':'Steal','stats':{'energy':-1,'money':300,'fame':-1}},
                           ]
        self.work_list=[{},
                        ]

    def set_utility(self):
        return random.sample(game.utility_list,game.utility_num)


class Player:
    def __init__(self):
        self.name=''
        
        self.energy=0
        self.energy_left=0
        self.money=0
        self.health=0
        self.str=0
        self.agi=0
        self.wis=0
        self.tal=0
        self.luck=0
        self.fame=0
        self.bag=[]
        
##################################################
function=Function()
main=Main()

setting=Setting()
game=Game()
event=Event()
player=Player()


###
setting.choose_map()
setting.choose_character()
setting.set_utility()
game.list_utility()
time.sleep(5)
