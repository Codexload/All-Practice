#---------------------------------------------------------Diclaring A Dictionary----------------------------------------------------------
dic = {"Name" : "Tanjimul Hisham", "Age" : "17", "Hight" : "5.10'", "Fathers Name" : "Sakhawat Hossen", "Mothers Name" : "Kamrun Nahar"}
#------------------------------------------------------------Normal Operations-----------------------------------------------------------
print(dic["Hight"])
print("Name" in dic)
print("Fathers Name" not in dic)
print(list(dic.keys()))
print(list(dic.values()))
print(list(dic.items()))
print(dic.keys())
print(dic.get("Age"))
print(dic.get("old_age", "None"))
#---------------------------------------------------------Loops----------------------------------------------------------
for i in dic.keys():
    print(i)
for a in dic.values():
    print(a)
for b in dic.items():
    print(b)
massage = "Well Hello There This Is\nTanjimul Hisham\nEthical Hacker, Cyber Security Specialist, Devloper"
dic = {}
for charecter in massage.lower():
    dic.setdefault(charecter, 0)
    dic[charecter] = dic[charecter] + 1
print(dic)
#---------------------------------------------------------Condition----------------------------------------------------------
if "Hobby" not in dic:
    dic["Hobby"] = "Coding"
