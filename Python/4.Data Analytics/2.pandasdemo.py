

import pandas as p

#Series
# creation in different ways
#
l1 = ["dghsj","hjdsd","gvhj","hgbb","rdjh","dfgvf"]
s1 = p.Series(l1)
print("s1 -> \n",s1)
#
t1 = ("dgr","tfhyvg","fhg")
s2 = p.Series(t1)
print("s2 -> \n",s2)
#
dic1 = {"Name":"dgr","Age":45}
s3 = p.Series(dic1)
print("s3 -> \n",s3)


# accessing
print("s1 -> \n", s1)
print(s1.loc[2])
print(s1.loc[1:])
print(s1.loc[1:3])
print(s1.loc[0::2])
#print(s1.loc[-3:])
print(s1.iloc[0])
# #
# # custom index
s4 = p.Series(l1,index=["a","b","c","d","e","f"])
print("s4 -> \n",s4)
print(s4.loc["b"])
print(s4.loc["a":"d"])
print(s4.iloc[-2:])

# conditions
l2 = [56,34,54,32,65,57]
s5 = p.Series(l2)
print("S5 -> \n", s5)
print(s5[s5>50])
print(s1[s1>"g"])


# dataframes
# dataframes
dic2 = {"Name":["tyd","hudfsk","uisfd"],
        "Age":[45,43,65]}
s6 = p.DataFrame(dic2)
print("s6 -> \n", s6)

dic2["Salary"] = [34245,65778,87965]
s7 = p.DataFrame(dic2)
print("s7 -> \n", s7)

dic2.update({"Desg":["hr","dev","testing"],
                "Address":["hyd","delhi","mumbai"]})
s8 = p.DataFrame(dic2)
print("s8 -> \n", s8)

new_row = p.DataFrame([{"Name":"uygf","Age":78,"Salary":56234,"Desg":"hr","Address":"hyd"}],index=["a"])
print(s8)
print(p.concat([s8,new_row]))

# excel
df9 = p.read_excel(r'C:\Users\nares\Downloads\SQLEXAM-254.xlsx')
print("df9 -> \n", df9)
#print("df9 ->\n", df9.to_string())
print(df9["name"])
print(df9["name"].to_string())
print(df9[["name","marks","feedback"]])
#print(df9[["name","marks","feedback"]].to_string())
print(df9.head(20))
print(df9.head(20).to_string())
print(df9.tail(15))
print(df9.tail(15).to_string())

print(df9.loc[4])
print(df9.loc[5:17].to_string())
print(df9.loc[5:17:3].to_string())

print(df9)

df10 = p.read_excel(r"C:\Users\nares\Downloads\SQLEXAM-254.xlsx", index_col="global_id")
print("df10 -> \n", df10)
print(df10.loc["CV019086"])
print(df10.iloc[23])


# n1 = int(input("Enter a number: "))
#
# try:
#     print(n1," row data -> \n",df10.iloc[n1])
# except IndexError:
#     print("Index ",n1, " row data not found")


print(df10.info())
print(df10.describe())

# Aggregate Functions
# on whole data set
print("Sum of Values \n",df10.sum(numeric_only=True))
print("Avg of values \n",df10.mean(numeric_only=True))
print("min of values \n",df10.min(numeric_only=True))
print("max of values \n",df10.max(numeric_only=True))
print("count of values in each column \n",df10.count())

# on specific columns
print("Sum of marks -> \n",df10["marks"].sum())
print("max of marks -> \n",df10["marks"].max())
print("min of marks -> \n",df10["marks"].min())
print("Avg of marks -> \n",df10["marks"].mean())
print("Count of marks -> \n",df10["marks"].count())
print("median of marks -> \n",df10["marks"].median())
print("cummilative sum of marks -> \n",df10["marks"].cumsum().to_string())
print("cummilative product of marks -> \n",df10["marks"].cumprod().to_string())


gp1 = df10.groupby("marks")
print(gp1["phone"].max())


# conditions
print("df10 -> \n",df10)
print( df10[(df10["marks"]>10) & (df10["marks"]<100)])
print( df10[(df10["marks"]==30) | (df10["feedback"]=="ok")] )


# Steps for Data preprocessing
# 1 Removing unwanted columns
print(df10.drop(columns=["email"]).to_string())
print(df10.drop(columns=["email","phone","feedback"]).to_string())

# 2 Dealing with duplicate data
# identifying duplicate values
print(df10.duplicated())
print(df10.duplicated().sum())
print(df10.duplicated("marks").to_string())
print(df10.duplicated("marks").sum())

# removing duplicate rows
print(df10.drop_duplicates().to_string())
print(df10.drop_duplicates("roll_no").to_string())
print(df10.dropna(subset=["marks"]).to_string())
print(df10.dropna(subset=["feedback"]).to_string())
print(df10.dropna(subset=["marks","feedback"]).to_string())
print(df10.fillna({"feedback":"Write the Exam"}).to_string())
print(df10.fillna({"feedback":"Write the Exam","marks":-25}).to_string())
print(df10["marks"].mean())
print(df10.fillna({"marks":df10["marks"].mean()}).to_string())
print(df10.fillna(method="ffill").to_string()) # lag
print(df10.fillna(method="bfill").to_string()) # lead
df11 = df10.fillna({"marks":df10["marks"].mean()})
print(df11.fillna(method="bfill").to_string())
# alternate way
print(df10.fillna({"marks":df10["marks"].mean()}).ffill().to_string())


# 3.handling null values

print(df10.isnull())
print(df10["marks"].isnull())
print(df10["feedback"].isnull().sum())


# 4. fixing inconsistent data

print("df10 -> \n",df10.to_string())
print(df10["feedback"].replace({'IMPRove':'Improve'}).to_string())
print(df10["feedback"].replace({'IMPRove':'Improve','gooD':'good'}).to_string())


#  5. bringing data into one single format
print(df10["feedback"].str.lower().to_string())
print(df10["feedback"].str.upper().to_string())
print(df10[["name","feedback"]].apply(lambda x:x.str.upper()).to_string())


# 6 change datatype
print(df10["phone"].astype(str).to_string())


# Merge dataframes

dict3 = {"Eid":[101,102,103,104],
         "Ename":["ghfd","fghbh","ftgty","hfg"],
         "Dept_id":[1,2,1,6]}

dict4 = {"Dept_id":[1,2,3,4,5],
         "Dept_Name":["hr","sde","testing","devops","analyst"]}

df12 = p.DataFrame(dict3)
print("df12 -> \n",df12)
df13 = p.DataFrame(dict4)
print("df13 -> \n",df13)


print(p.merge(df12,df13,on="Dept_id"))
print(p.merge(left = df12,right = df13,on="Dept_id", how = "left"))
print(p.merge(left = df12,right = df13,on="Dept_id", how = "right"))
print(p.merge(df12, df13, how = "cross"))
print(p.merge(left = df12,right = df13,on="Dept_id", how = "outer"))

dict5 = {"Eid":[101,102,103,104],
         "Ename":["ghfd","fghbh","ftgty","hfg"],
         "Dept_id":[1,2,1,6]}

dict6 = {"Department_id":[1,2,3,4,5],
         "Dept_Name":["hr","sde","testing","devops","analyst"]}

df14 = p.DataFrame(dict5)
print("df14 -> \n",df14)
df15 = p.DataFrame(dict6)
print("df15 -> \n",df15)

print(p.merge(left=df14,right=df15,left_on="Dept_id",right_on="Department_id",how="inner"))


# comapring DataFrames

dic7 = {"Dept_Id":[32,45,65,56],
        "Department_Name":["hr","sde","devops","sr"]}
#print("df7 -> \n",dic7)
df16 = p.DataFrame(dic7)
print("df16 -> \n",df16)

dic8 = {"Dept_Id":[1,45,3,56],
        "Department_Name":["hr","sde","analyst","devops"]}
#print("df8 -> \n",dic8)
df17 = p.DataFrame(dic8)
print("df17 -> \n",df17)

print("comparing DataFrames -> \n",df16.compare(df17))


# concating dataframes

dict9 = {"Eid":[101,102,103,104],
         "Dept_id":[1,67,45,78]}
#print("df9 -> \n",df16)
df18 = p.DataFrame(dict9)
print("df18 -> \n",df18)

print("concatenating DataFrames \n",p.concat([df17,df18]))


# pivoting DataFrames

print("df14 -> \n",df14)
print(df14.pivot(index="Dept_id", columns="Ename", values="Eid"))

