"""
sheet_dct: Contains list of sheet URLs for automation
replacement_dct: Used to grab colloquial Champion names (MonkeyKing = Wukong etc)
"""

################################################
###                                          ###
###  HOW TO ADD A NEW SHEET TO YOUR NETWORK  ###
###                                          ###
###  - Duplicate 'Images' tab to new sheet   ###
###    or one you already own                ###
###                                          ###
###  - Add your Oauth2 service email as an   ###
###    editor on that new sheet              ###
###                                          ###
###  - (Opt) Add that sheet url to sheet_dct ###
###    in the dictionary below               ###
###                                          ###
###  - Now you can update the images in      ###
###    that sheet using set_images()         ###
###                                          ###
################################################

sheet_dct = {
    'url_nickname': 'url'
}

replacement_dct = {
            'TahmKench' : 'Tahm Kench',
            'MonkeyKing' : 'Wukong',
            'LeeSin' : 'Lee Sin',
            'XinZhao' : 'Xin Zhao',
            'Kaisa' : 'Kai\'Sa',
            'TwistedFate' : 'Twisted Fate',
            'AurelionSol' : 'Aurelion Sol',
            'KogMaw' : 'Kog\'Maw',
            'RekSai' : 'Rek\'Sai',
            'Chogath' : 'Cho\'Gath',
            'Khazix' : 'Kha\'Zix',
            'Velkoz' : 'Vel\'Koz',
            'DrMundo' : 'Dr. Mundo',
            'Leblanc' : 'LeBlanc',
            'MasterYi' : 'Master Yi',
            'MissFortune' : 'Miss Fortune',
            'JarvanIV' : 'Jarvan IV',
            'Belveth' : 'Bel\'Veth',
            'KSante' : 'K\'Sante'
        }
















