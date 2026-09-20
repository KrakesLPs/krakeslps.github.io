import os # default module
import requests
import json

def getAllSeasonInfo(name):
    AllSeasonInfo = requests.get("https://api.mcsrranked.com/users/"+name+"/seasons")
    AllSeasonInfoJSON = AllSeasonInfo.json()
    if AllSeasonInfoJSON['status'] != 'success':
        print("Season Info Request Failed" + AllSeasonInfoJSON['status'] + AllSeasonInfoJSON['data'])
        return
    return AllSeasonInfoJSON

def getUserInfo(name):
    userInfo = requests.get("https://api.mcsrranked.com/users/"+name)
    userInfoJSON = userInfo.json()
    if userInfoJSON['status'] != 'success':
        print("Season Info Request Failed" + userInfoJSON['status'] + userInfoJSON['data'])
        return
    return userInfoJSON


cwd = os.getcwd()
MidOffs1Players_Named = ["Sneegsnag","BadBoyHalo","Wolfeei","Jonnaay","jojosolos","BrryHrry","BaboAbe","Derapchu","AntVenom","JumperWho","hannahxxrose","Woogiex","aimsey","CaptainSparklez","sunnieryans","rhiga"] #sunnieryans is DandelionRyan
MidOffs2Players_Named = ["ItzMasayoshi","Beauti","Seapeekay","5uppps","Pangi","Roscumber","TheRealSquiddo","maxggs_","LukeyTV","sylvee_","ish13c","sleepai","JackManifoldTV","cubfan135","SB737"] #Beauti is hollsbeauti, im ignoring that weirdo sykkuno, only ever played his matches anyway so no stats to speak of
MidOffs3Players_Named = ["LexieMariex","Juicy_Craft","Bitzel","melinks","GoodTimeWithScar","superrtf","Demenishki","GlipyGlorp","falsesymmetry","saparata","Evbo_","p4perback","fatchudlolcow","soupforeloise","NominalGravy","billzo_"] #fatchudlolcow is ludwig, glipyglorp is Dtowncat/Pili
MidOffsLivePlayers_Named = ["SandwichLord_"]
MidOffs4Players_Named = ["DuncanMassink", "TheobaldTheBird", "KingSammelot", "Etoiles", "GeminiTay", "ghostiefruit", "Grian", "Ph1LzA", "JeremyFrieser", "ashswagg", "Shandrea", "Cambam010", "bekyamon", "TeanaKitten", "saucebxss", "MewZe"] #saucebxss is katieb
MidOffsPlayers_Named = MidOffs1Players_Named + MidOffs2Players_Named + MidOffs3Players_Named + MidOffsLivePlayers_Named + MidOffs4Players_Named

MidOffs1Players_uuid = ["7c59923124d348bd936cd81560d567a0","26bdff37fec848f1980f66bf69ee751c","2a932fbde2454dcf89679ae596f22fb1","9ae689ef618144899e25d9ad39812035","d96b2fdf3ffd42d1a1ed3b26b3d5e173","7bfc146016f0428a9fd8b82b663a2a2c",
                        "d81d8db4443d4cafb19d90a377a6df02","68ec42a99c3d4538afe574cc9d8e06b6","0c063bfd3521413da76650be1d71f00e","41251c16bbf74ef1a1818bd5c6fc9a1d","5237b4b75eed421da43f0e4968e69207","37a1e4a827bd4eee9f5ba258a11e53df",
                        "dd25fe9f186546678fe9eacb18d01d31","5f820c3958834392b1743125ac05e38c","adcd683f23e44bddbe5ecc3ec9fe67ab","504a61571e82458aaf4490c87d8e81e7"]
MidOffs2Players_uuid = ["378c2b5f7d20495d92c136c56de7e859","91f70d7395194dd1a7e4b54d067cb849","be0cfbc2f626483580c3924268faf27b","0f5e0db013a04125a97ae9f8e872d521","4f549297db6349bd87d6db4c4333c776","4556db48862c433aa3d746a79eaa2468",
                        "d4bb44317daf4642bb14a1f8fe9ae101","6e1bbd903af14831b9efffaf23b8c19a","a1a44a93e8dd4529813bc457e9ebe468","aec14d1e14e843cb89ed80d81153bc56","28d048bd0fc54283ade3f9b3e7676cd4","f9cac06540f24421af2c051ed943dc23",
                        "91a5123aa3944e50a5af2006a341c8ab","88e2afec6f2e4a34a96ade61730bd3ca","98c0bece0232485e8e86fa604d78e62f"] #im ignoring sykkuno that weirdo, only ever played his matches anyway so no stats to speak of
MidOffs3Players_uuid = ["7ed4675ef67a4cb99cb3e3035dec7ff1","33353d80e4e1469fbcc1856003e5842a","c105bf11c0ee497abeb28a131a33e9f1","222c354fdfd549528f20451fa44ee002","cae9554c31be47e2ba2b4b8867adacc5","9ecc82c552af443193f19e9b296ff534",
                        "b6288ed7bba246bf97e69f89a80ddcdf","030ffa300eba4fb2921d61ea56304a2c","87d915486f18491fa2677833caa5d7d8","296d434fe7814d449b66469eab9d9bfe","c08ad74bad0b44b58d1b594d790edfb3","fcce8c0a7da54c059c48047b6b84bc42",
                        "e44f4cdce63341e7aff36071ac1107d4","db7ecf6f52b643eaa764d8362c45e5f8","d66c301e2485434ebe7cf9c5e8adcfe8","0638d540576e42c0baaddea5805c7e43"]
MidOffsLivePlayers_uuid = ["1e2bf44f122f4960a62d7da9609f52e7"]
MidOffs4Players_uuid = ["eb0d84ae8c124ffbb13a2f7c47cd98de","1b423bc029d14595a83d4c8670fcbda4","c1456a6a9ac7467da86f6c4b02300560","ea2ff7e97f4345efa6e7493c656eaabf","5a1839d2cecc4c85aa08b346f9f772a1","8c3d406f950e4761a7f10cf3202be59b", 
                        "5f8eb73b25be4c5aa50fd27d65e30ca0","84555089add149b1a26d8021270a40f0","975e0f7987b4407b97b06cfa8d80cc1a","909b156ff022491bbd0adf41cb88041d","18ef65d48dc04bb689fa682edbd31132","8eb3fb13acc447819c226013ff3a60f7", 
                        "2bbb5709ebd448388cd7466efc42db11","57d77b5a531c4c22a42450190976b369","16bcd4be2799494ebdf8ff4916b1a627","7cbbd43c9ccd470c89973b516b160f74"]
MidOffsPlayers_uuid = MidOffs1Players_uuid + MidOffs2Players_uuid + MidOffs3Players_uuid + MidOffsLivePlayers_uuid + MidOffs4Players_uuid

#Every new Season I need the new UUIDs for all the players
def getUUIDsForNames(Names):
    for Player in Names:
        userInfo = getUserInfo(Player)
        print(Player +" "+ userInfo['data']["uuid"])
        print("\"" + userInfo["data"]["uuid"] + "\",")

#Data for MidOffs Particapants
def PlayerScraping():
    for Player in MidOffsPlayers_uuid:
        seasonInfo = getAllSeasonInfo(Player)
        with open(cwd + "/bigdata/" + Player + "SeasonInfo.json", "w+") as f:
            json.dump(seasonInfo, f)
        userInfo = getUserInfo(Player)
        with open(cwd + "/bigdata/" + Player + "userInfo.json", "w+") as f:
            json.dump(userInfo, f)

#Data for myself
def KrakeScraping():
    krakeSeasonInfo = getAllSeasonInfo("Krake")
    with open(cwd + "/MyData/" + "Krake" + "SeasonInfo.json", "w+") as f:
        json.dump(krakeSeasonInfo, f)
    krakeUserInfo = getUserInfo("Krake")
    with open(cwd + "/MyData/" + "Krake" + "UserInfo.json", "w+") as f:
        json.dump(krakeUserInfo, f)