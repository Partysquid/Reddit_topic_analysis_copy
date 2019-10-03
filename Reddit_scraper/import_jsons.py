import os

reddit_array=["leagueoflegends","LoLeventVoDs","summonerschool"]
other = ['SwainMains', 'JhinMains', 'JarvanIVMains', 'RenektonMains', 'DrMundoMains', 'EzrealMains', 'IreliaMains', 'MalphiteMains', 'Illaoi', 'MorganaMains', 'GalioMains', 'SyndraMains', 'EvelynnMains', 'GragasMains', 'ViktorMains', 'WukongMains', 'XayahMains', 'KennenMains', 'LissandraMains', 'Sivir', 'BardMains', ' CaitlynMains', 'VladimirMains', 'VolibearMains', 'UrgotMains', 'RekSaiMains', 'LeeSinMains', 'VarusMains', 'TheSecretWeapon', 'LeagueofJinx', 'LucianMains', 'ThreshMains', 'TwitchMains', 'TeemoTalk', 'MordekaiserMains', 'RivenMains', 'XerathMains', 'Lux', 'OriannaMains', 'DianaMains', 'ZoeMains', 'HeimerdingerMains', 'YorickMains', 'TristanaMains', 'RumbleMains', 'DirtySionMains', 'ZileanMains', 'Kindred', 'VeigarMains', 'CassiopeiaMains', 'SonaMains', 'GarenMains', 'GnarMains', 'TwistedFateMains', 'GravesMains', 'Aurelion_Sol_Mains', 'ShyvanaMains', 'NocturneMains', 'ZyraMains', 'MissFortuneMains', 'LeonaMains', 'RengarMains', 'AzirMains', 'Shen', 'TaliyahMains', 'FiddlesticksMains', 'HecarimMains', 'JayceMains', 'KatarinaMains', 'FioraMains', 'KalistaMains', 'RyzeMains', 'AsheMains', 'EkkoMains', 'ChoGathMains', 'Kog_Mains', 'MasterYiMains', 'UdyrMains', 'ornnmains', 'PantheonMains', 'TrundleMains', 'OlafMains', 'RakanMains', 'NidaleeMains', 'SorakaMains', 'KarmaMains', 'KassadinMains', 'YasuoMains', 'QuinnMains', 'CamilleMains', 'TaricMains', 'RammusMains', 'Velkoz', 'KaisaMains', 'KayleMains', 'JaxMains', 'AniviaMains', 'BlitzcrankMains', 'MalzaharMains', 'WarwickMains', 'ShacoMains', 'GangplankMains', 'AkaliMains', 'Alistar', 'SkarnerMains', 'LuluMains', 'AhriMains', 'NasusMains', 'DariusMains', 'IvernMains', 'AmumuMains', 'Draven', 'TahmKenchMains', 'ViMains', 'SejuaniMains', 'BrandMains', 'AatroxMains', 'NamiMains', 'VayneMains', 'CorkiMains', 'TalonMains', 'MaokaiMains', 'ZiggsMains', 'NunuMains', 'KhaZixMains', 'SingedMains', 'EliseMains', 'LeblancMains', 'XinZhaoMains', 'FizzMains', 'Janna', 'KarthusMains', 'BraumMains', 'ZedMains', 'PoppyMains', 'KaynMains', 'TryndamereMains', 'NautilusMains']
reddit_array = reddit_array+other

for i in range(0,len(reddit_array)):
	reddit_array[i] = "Reddit"  + reddit_array[i]

reddit_array.append("Champions")
reddit_array.append("Items")

for k in reddit_array:
	os.system("")
