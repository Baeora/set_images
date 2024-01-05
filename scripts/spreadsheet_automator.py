from core import *
import pygsheets

def set_images(url=None):
    champs = get_champion_ids().replace({'Renata Glasc':'Renata'})
    items = get_item_ids()
    runes = get_perk_ids(addPaths=True)
    summoner_spells = get_summoner_spell_ids()

    gc = pygsheets.authorize(service_account_file=service_file)
    sh = gc.open_by_url(url)
    
    images = sh.worksheet('title','Images')

    images.clear(start='B3', end='B579')
    images.clear(start='D3', end='E579')
    images.clear(start='F3', end='F900')
    images.clear(start='H3', end='J900')
    images.clear(start='L3', end='O900')
    images.clear(start='Q3', end='R900')

    images.set_dataframe(pd.DataFrame(champs['id']), 'D3', copy_head=False)
    images.set_dataframe(pd.DataFrame(champs['name']), 'B3', copy_head=False)
    images.set_dataframe(pd.DataFrame(items['id']), 'J3', copy_head=False)
    images.set_dataframe(pd.DataFrame(items['name']), 'L3', copy_head=False)
    images.set_dataframe(pd.DataFrame(items['path_name']), 'M3', copy_head=False)
    images.set_dataframe(pd.DataFrame(runes['id']), 'O3', copy_head=False)
    images.set_dataframe(pd.DataFrame(runes['name']), 'Q3', copy_head=False)
    images.set_dataframe(pd.DataFrame(runes['path_name']), 'R3', copy_head=False)
    images.set_dataframe(pd.DataFrame(summoner_spells['id']), 'F3', copy_head=False)
    images.set_dataframe(pd.DataFrame(summoner_spells['name']), 'H3', copy_head=False)
    images.set_dataframe(pd.DataFrame(summoner_spells['path_name']), 'I3', copy_head=False)