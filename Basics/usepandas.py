import pandas

studentlist={"AB44":("Ishika","BCA",175),"AB35":("Hariom","B.Tech",75),"AB53":("Arya","B.Tech",19),"AB55":("Issu","BCA",94)}

records=pandas.DataFrame.from_dict(studentlist)
print(records)
