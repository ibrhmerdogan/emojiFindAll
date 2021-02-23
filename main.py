import mysqlClass
import emojiClass


aciklamalar = mysqlClass._SelectData()
for i in aciklamalar:
        qText = i[0]
        id = i[1]
        if qText is not None:
            listeler = emojiClass._emojiList(str(qText))
            emojiler = emojiClass._emojiCounter(listeler,id)
            for y in range(len(emojiler)):
                İnsID =emojiler[y]["id"]
                Emoji = emojiler[y]["emoji"]
                Adet = emojiler[y]["adet"]
                print(İnsID, Emoji, Adet)
                mysqlClass._AddData(İnsID, Emoji, Adet)
