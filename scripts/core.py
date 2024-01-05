import os
from pathlib import Path
import pandas as pd
import warnings

from urllib.request import urlopen, Request
import json

pd.options.mode.chained_assignment = None  # default='warn'
warnings.simplefilter(action='ignore', category=FutureWarning)

service_file = os.path.join(os.path.dirname(Path.cwd()), 'JSONs\\unique-epigram-337119-5b7bc9cfd665.json')

###############
### CDragon ###
###############

def json_extract(obj, key):
    """Nested json extract function

    Args:
        obj (dict): Dictionary you're searching through
        key (str): Key you're looking for

    Returns:
        list: Returns a list of every dictionary value at key
    """    
    arr = []

    def extract(obj, arr, key):

        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

def get_item_ids():
    """Pulls all item IDs from Cdragon and returns them as a dataframe.

    Returns:
        item_ids (dataframe): Dataframe of item IDs.
    """    

    response = urlopen(Request('https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/items.json', headers={'User-Agent': 'Mozilla'}))

    data_json = json.loads(response.read())

    icon_path = json_extract(data_json, 'iconPath')
    path_name = []
    for path in icon_path:
        path_name.append(path.split('/lol-game-data/assets/ASSETS/Items/Icons2D/')[1].lower())

    item_ids = pd.DataFrame({
        'id': json_extract(data_json, 'id'),
        'name': json_extract(data_json, 'name'),
        'path_name': path_name
    })

    return item_ids

def get_perk_ids(addPaths=False):
    """Pulls all perk IDs from Cdragon and returns them as a dictionary (or dataframe with image strings).

    Args:
        addPaths: If True, will instead return a 3-Column DataFrame containing image strings for each perk.

    Returns:
        perk_ids (dictionary): Dictionary of perk IDs.
        perk_ids (dataframe): Dataframe of perk IDs containing image strings for each perk.
    """

    perk_req = urlopen(Request('https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perks.json', headers={'User-Agent': 'Mozilla'}))
    style_req = urlopen(Request('https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/perkstyles.json', headers={'User-Agent': 'Mozilla'}))

    perk_json = json.loads(perk_req.read())
    style_json = json.loads(style_req.read())

    if addPaths:
        perk_ids = pd.DataFrame({
            'id': json_extract(perk_json, 'id'),
            'name': json_extract(perk_json, 'name'),
            'path_name': json_extract(perk_json, 'iconPath')
        })

        style_ids = pd.DataFrame({
            'id': json_extract(style_json, 'id')[0::5],
            'name': json_extract(style_json, 'name'),
            'path_name': json_extract(style_json, 'iconPath')
        })        

        for i in range(len(perk_ids)):
            perk_ids['path_name'][i] = (perk_ids['path_name'][i].split('/lol-game-data/assets/v1/perk-images/')[1].lower())

        for i in range(len(style_ids)):
            style_ids['path_name'][i] = (style_ids['path_name'][i].split('/lol-game-data/assets/v1/perk-images/')[1].lower())

        perks = pd.concat([perk_ids, style_ids]).reset_index(drop=True)
    else:
        perk_ids = json_extract(perk_json, 'id')
        perk_names = json_extract(perk_json, 'name')

        perk_ids.extend(json_extract(style_json, 'id'))
        perk_names.extend(json_extract(style_json, 'name'))

        perks = dict(map(lambda i,j : (int(i),j) , perk_ids,perk_names))

    return perks

def get_champion_ids():
    """Pulls all champion IDs from Cdragon and returns them as a dataframe.

    Returns:
        champion_ids (dataframe): Dataframe of champion IDs.
    """
    
    response = urlopen(Request('https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-summary.json', headers={'User-Agent': 'Mozilla'}))

    data_json = json.loads(response.read())

    champion_ids = pd.DataFrame({
        'id': json_extract(data_json, 'id'),
        'name': json_extract(data_json, 'name'),
        'alias': json_extract(data_json, 'alias')
    })
    
    champion_ids['link_head'] = "https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/"
    champion_ids['link_tail'] = ".png"


    champion_ids['img'] = champion_ids['link_head'] + champion_ids['id'].astype(str) + champion_ids['link_tail']

    champion_ids.drop(columns=['link_head', 'link_tail'], inplace=True)

    champion_ids = champion_ids[1:].sort_values('name').reset_index(drop=True)

    return champion_ids

def get_summoner_spell_ids():
    """Pulls all summoner spell IDs from Cdragon and returns them as a dataframe.

    Returns:
        summoner_spell_ids (dataframe): Dataframe of summoner spell IDs.
    """
    response = urlopen(Request('https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/summoner-spells.json', headers={'User-Agent': 'Mozilla'}))

    summoner_spell_json = json.loads(response.read())

    icon_path = json_extract(summoner_spell_json, 'iconPath')
    path_name = []
    for path in icon_path:
        path_name.append(path.split('/lol-game-data/assets/')[1].lower())

    summoner_spell_ids = pd.DataFrame({
        'id': json_extract(summoner_spell_json, 'id'),
        'name': json_extract(summoner_spell_json, 'name'),
        'path_name': path_name
    })

    return summoner_spell_ids
