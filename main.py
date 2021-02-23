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
                print(emojiler[y]["id"],emojiler[y]["emoji"],emojiler[y]["adet"])

