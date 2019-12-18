# -*- coding: utf-8 -*-
"""
 
This file contains functions and data structures useful to the Python for ML
class but not worth coding in real time. Trace on your own time!
"""
from typing import Set

def clean_writers(writers:Set, delim = "&") -> Set:
    """
    this function removes special characters from the list of authors and
    returns a list of authors such that multiple authors are separated with a
    '&'
    param:: a set of writers
    returns:: a set of all writers with special characters and 
              extra characters removed
    """
    replace_pairs=[("\xa0"," "),("\u200a:"," "),("and","&"),("Story by ","")]
    for old_symbol, new_symbol in replace_pairs :
        writers= [writer.replace(old_symbol, new_symbol) for writer in writers]
    all_writers=set([])
    for writer in writers:
        temp=writer.split(delim)
        temp=[w.strip() for w in temp]
        all_writers.update(temp)
    return all_writers

def get_writers_one_hot(writers_df):
    """
    Converts the writers column into a one-hot encoding. Takes into account that
    there could be several writers in the writers column.
    param:: writers df --> the writers column
    returns:: one hot encoding of writers
    """
    writers= set(writers_df)
    writers_df=writers_df.to_frame()
    writers= clean_writers(writers)
    for writer in writers:
        writers_df[f"Writer_{writer}"]=0
    for i, row in writers_df.iterrows():
      for writer in writers:
            if writer in row["Writer"]:
                writers_df.at[i, f"Writer_{writer}"] = 1
    writers_df.drop(["Writer"],axis=1, inplace=True)
    return writers_df

class NamesToReplace():
    """ 
    this holds a list of names and their replacement names. 
    The names are listed in the pairs(old_name, new_name)
    To loop through this list, use the code:
    for old_name, new_name in <object of type NamesToReplace>.names:
"""
    def __init__(self):
        self.names=[('missandei', 'mereen missandei'),
               ('alliser', 'alliser thorne'),
               ('alliser thorn','alliser thorne'), 
               ('alliser throne','alliser thorne'),
               ('alliser', 'alliser thorne'),
               ('robin', 'robin arryn'),
               ('tanner', 'karl tanner'),
               ('beric', 'beric dondarrion'),
               ('priestess', 'red priestess'),
               ('hodor', 'hodor luwin'),
               ('watch brother', 'nights watch brother'),
               ('owner', 'slave owner'),
               ('ersei', 'cersei'),
               ('yohn', 'yohn royce'),
               ('sandor', 'sandor clegane'),
               ('lollys', 'lollys stokeworth'),
               ('kraznys', 'kraznys mo nakloz'),
               ('lysa', 'lysa arryn'),
               ('mordane', 'septa mordane'),
               ('buyer', 'slave buyer'),
               ('olenna', 'lady olenna'),
               ('red priest', 'red priestess'),
               ('drogo', 'khal drogo'),
               ('roose', 'roose bolton'),
               ('yarwyck', 'othell yarwyck'),
               ('yarwick', 'othell yarwick'),
               ('janos', 'janos slunt'),
               ('aemon', 'maester aemon'),
               ('pie', 'hot pie'),
               ('sparrow', 'high sparrow'),
               ('wolkan', 'maester wolkan'),
               ('bron', 'bronn'),
               ('meryn', 'meryn trant'),
               ('maester pycell', 'maester pycelle'),
               ('robett', 'robett glover'),
               ('illyrio', 'illyrio mopatis'),
               ('pycelle', 'maester pycelle'),
               ('jora', 'jorah'),
               ('walder', 'walder frey'),
               ('barristan', 'barristan selmy'),
               ('worm', 'grey worm'),
               ('pycell', 'maester pycelle'),
               ('mord', 'septa mordane'),
               ('a young melara', 'melara'),
               ('knight of house frey', 'knight'),
               ('knight of house bracken', 'knight'),
               ('knight of house whent', 'knight'),
               ('vale knight', 'knight'),
               ('army closed in loras', 'loras'),
               ('its starting to tickler', 'tickler'),
               ('thenn warg', 'warg'),
               ('davos sighs davos', 'davos'),
               ('davo davos', 'davos'),
               ('blackwater bay davos', 'davos'),
               ('night davos', 'davos'),
               ('voices outside', 'voice'),
               ('male voice', 'voice'),
               ('a voice', 'voice'),
               ('all together', 'together'),
               ('nights watch brother', 'nights watch'),
               ('quarantine rooms marwyn', 'marwyn'),
               ('thronekhal drogo', 'khal drogo'),
               ('i just couldnt qhorin', 'qhorin'),
               ('kingsguard septa mordane', 'septa mordane'),
               ('theon theon', 'theon'),
               ('why would theon roose', 'theon'),
               ('and then theon', 'theon'),
               ('sraw theon', 'theon'),
               ('third time bronn', 'bronn'),
               ('brand', 'bran'),
               ('brans voice', 'bran'),
               ('qyburns', 'qyburn'),
               ('dungeons qyburn', 'qyburn'),
               ('jaimes quarters jaime', 'jaime'),
               ('yaras ship nymeria', 'nymeria'),
               ('night watch stable boy', 'boy'),
               ('stable boy', 'boy'),
               ('vile thin man', 'thin man'),
               ('sansa master of arms', 'sansa'),
               ('so sansa', 'sansa'),
               ('and so xaro', 'xaro'),
               ('but talisa', 'talisa'),
               ('shhh talisa', 'talisa'),
               ('steward of house', 'steward'),
               ('dothraki woman', 'woman'),
               ('lhazareen woman', 'woman'),
               ('yaras ship nymeria', 'yara'),
               ('ings road brienne', 'brienne'),
               ('streets euron', 'euron'),
               ('wine merchant', 'merchant'),
               ('grand maester pycelle', 'maester pycelle'),
               ('elder meereen slave', 'meereen slave'),
               ('bring me lancel', 'lancel'),
               ('i lancel', 'lancel'),
               ('captains quarters ellaria', 'ellaria'),
               ('ser jorah', 'jorah'),
               ('wildling elder', 'wildling'),
               ('and remember littlefinger', 'littlefinger'),
               ('day podrick', 'podrick'),
               ('frey soldier', 'soldier'),
               ('wounded soldier', 'soldier'),
               ('unphased melisandre', 'melisandre'),
               ('oh stannis', 'stannis'),
               ('stannis dwarf', 'stannis'),
               ('manservant', 'man'),
               ('thin man', 'man'),
               ('old man', 'man'),
               ('young man', 'man'),
               ('bolton bannerman', 'man'),
               ('frey man', 'man'),
               ('watchman', 'man'),
               ('dying man', 'man'),
               ('go man', 'man'),
               ('head man', 'man'),
               ('robb robb', 'robb'),
               ('she robb', 'robb'),
               ('robb dwarf', 'robb'),
               ('i cant lose robb', 'robb'),
               ('too much robb', 'robb'),
               ('ingsgua meryn trant', 'meryn trant'),
               ('ned', 'ned stark'),
               ('blonde prostitute', 'prostitute'),
               ('head prostitute', 'prostitute'),
               ('black haired prostitute', 'prostitute'),
               ('it sounded margaery', 'margaery'),
               ('medicine margaery', 'margaery'),
               ('joffrey dwarf', 'joffrey'),
               ('king joffrey', 'joffrey'),
               ('the crowd laughs joffrey', 'joffrey'),
               ('please joffrey', 'joffrey'),
               ('ll be safe gilly', 'gilly'),
               ('guard captain', 'captain'),
               ('of dorne captain', 'captain'),
               ('kings guard', 'guard'),
               ('frey guard', 'guard'),
               ('kingsguard', 'guard'),
               ('not guard', 'guard'),
               ('bolton guard', 'guard'),
               ('yohn royce', 'john royce'),
               ('lord royce', 'john royce'),
               ('thr young rodrik', 'rodrik cassal'),
               ('a younger melara', 'melara'),
               ('young ned', 'ned'),
               ('quaithe', 'quaith'),
               ('watchmen', 'men'),
               ('bannermen', 'men'),
               ('frey men', 'men'),
               ('moles town whore', 'whore'),
               ('but shae', 'shae'),
               ('we pray shae', 'shae'),
               ('young lyanna', 'lyanna'),
               ('well catelyn', 'catelyn'),
               ('our orders catelyn', 'catelyn'),
               ('but catelyn', 'catelyn'),
               ('luwin', 'maester luwin'),
               ('ros', 'roslin'),
               ('dany','daenerys'),
               ('ayra', 'arya'),
               ('brinenne', 'brienne'),
               ('catelyin','catelyn'),
               ('cersel', 'cersei'),
               ('cersie', 'cersei'),
               ('daerneys','daenerys'),
               ('dav os', 'davos'),
               ('doloroud edd','dolorous edd'),
               ('dolrous edd','dolorous edd',),
               ('darrio', 'dario'),
               ('ed', 'eddark'),
               ('edd','eddark'),
               ('eddision','eddison tollett'),
               ('eddison','eddison tollett'),
               ('father arya', 'arya'),
               ('ill arya', 'arya'),
               ('grand maester pyrcelle','maester pycelle'),
               ('great hall jon', 'jon'),
               ('greyworm', 'grey worm'),
               ('hodor luwin','hodor'),
               ('young hodor', 'hodor'),
               ('gold cloack','gold cloak'),
               ('jaime', 'jamie'),
               ('jofffrey','joffrey'),
               ('kings quarters jon', 'jon'),
               ('maryn trant','meryn trant'),
               ('melisdandre','melisandre'),
               ('mountian', 'mountain'),
               ('mhaegan', 'mhaegen'),
               ('mosador','mossador',),
               ('othell yarwyck','othell yarwick'),
               ('pyat pree','pyatt pree',),
               ('ramsey','ramsay'),
               ('rickon','rikon'),
               ('rodrick cassel','rodrik cassal'),
               ('rodrik','rodrik cassal'),
               ('roz','roslin'),
               ('sallador','salladhor'),
               ('twyin','tywin'),
               ('tyriom', 'tyrion'),
               ('tyron', 'tyrion'),
               ('t daario','daario naharis'),
               ('daaerio', 'darrio naharis'),
               ('daario','daario naharis'),
               ('walkways jon', 'jon'),
               ('and grenn', 'grenn'),
               ('janos slynt', 'janos slunt'),
               ('allister','alliser thorne'),
               ('melisdandre','melisandre'),
               ('waldery frey', 'walder frey'),
               ('ser barristan','barristan selmy'),
               ('ser alliser','alliser thorne'),
               ('hizdahr', 'hizdahr zo loraq'),
               ('lorren', 'black lorren'),
               ('john', 'john royce'),
               ('maid', 'handmaiden'),
               ('karl', 'karl tanner'),
               ('waif', 'beat waif'),
               ('nakloz', 'kraznys mo nakloz'),
               ('walda', 'lady walda'),
               ('rickard', 'rickard kar'),
               ('cassel', 'jory cassel'),
               ('council room tycho','tycho'),
               ('anguy', 'fat anguy'),
               ('lock him up dagmer','dagmer' ),
               ('lommy', 'lommy greenhands'),
               ('kar', 'rickard kar'),
               ('lord kar', 'rickard kar'),
               ('loboda loboda', 'loboda'),
               ('aerson','aeron'),
               ('rakharo','rhakaro',)
               ]