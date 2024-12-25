import seaborn as sb
import matplotlib.pyplot as plt
import pandas as pd

data={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "total":[17,10,21,23,24,25,26,8]
}

data2={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "tip":[1,4,3,2,7,3,5,6]
}

data3={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "smoker":[1,4,3,2,7,3,5,6]
}

data4={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "time":[1,4,3,2,7,3,5,6]
}

data5={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "size":[1,4,3,2,7,3,5,6]
}

data6={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "gender":[1,4,3,2,7,3,5,6]
}

data7={
    "name":["mitsi","viarrah","jessica","miko","jack","raf","cade","sam"],
    "day":[1,4,3,2,7,3,5,6]
}

myd=pd.DataFrame(data)
myd2=pd.DataFrame(data2)
myd3=pd.DataFrame(data3)
myd4=pd.DataFrame(data4)
myd5=pd.DataFrame(data5)
myd6=pd.DataFrame(data6)
myd7=pd.DataFrame(data7)

#print(myd)

plt.figure(figsize=(8,5))
sb.scatterplot(x="name",y="total",data=myd,palette="pastel")
plt.title("names & total bills")
plt.xlabel("names")
plt.ylabel("total bills")
plt.show()

plt.figure(figsize=(8,5))
sb.scatterplot(x="name",y="tip",data=myd2,palette="pastel")
plt.title("names & tip")
plt.xlabel("names")
plt.ylabel("tip")
plt.show()

plt.figure(figsize=(8,5))
sb.scatterplot(x="name",y="size",data=myd5,palette="pastel")
plt.title("names & size")
plt.xlabel("names")
plt.ylabel("size")
plt.show()


plt.figure(figsize=(8,5))
df = sb.load_dataset('tips')
sb.pairplot(df, hue ='sex')
plt.xlabel("names")
plt.ylabel("gender")
plt.show()

plt.figure(figsize=(8,5))
plt.pie(myd7["day"],labels=myd7["name"],startangle=140,colors=sb.color_palette("bright"))
plt.title("name & day")
plt.show()

