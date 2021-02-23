import demoji
import json
def _emojiSymbolList(emojiText):
    emojilist  = demoji.findall(emojiText)
    for i in emojilist.items():
        y = 0
        emoji = i[0]
        y = y+1
        if i[1].find(":")>0 :
            emejiT =i[1][0:i[1].find(":")]
        else:
            emejiT = i[1]
        print(emoji,emejiT)
def _emojiList(emojiText):
    emojListesi = []
    emojilist  = demoji.findall_list(emojiText)
    for i in emojilist:
        if i.find(":")>0 :
            emejiT =i[0:i.find(":")]
        else:
            emejiT = i
        emojListesi.append(emejiT)
    return emojListesi

#print(_emojiList(tweet))
#print(list(set(_emojiList(tweet))))

def _emojiCounter(listeler, id):
    uniqueList = list(set(listeler))
    listAdet = []

    for i in uniqueList:
        z=0
        index = 0
        for j in listeler:
            if i==j:
               z=z+1
            index = index + 1

        thisdict = {
            "id" : id,
            "emoji": i,
            "adet": z
        }
        listAdet.append(thisdict)
    return  listAdet

