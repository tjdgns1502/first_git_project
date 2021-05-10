import matplotlib.pyplot as plt
import matplotlib
from urllib.request import urlopen
from bs4 import BeautifulSoup

html=urlopen("https://www.busan.go.kr/environment/ahfinedust")

soup=BeautifulSoup(html,"lxml")
#print(soup)

ultrafinedust_table=soup.find_all('table',{"class":"tableMt"})
print(len(ultrafinedust_table))
print(type(ultrafinedust_table))
print(type(ultrafinedust_table[0]))

ultrafinedust_table_tbody=ultrafinedust_table[3].find_all("tbody")
#print(len(ultrafinedust_table_tbody))

ultrafinedust_table_tbody_row=ultrafinedust_table_tbody[0].find_all("tr")
#print(ultrafinedust_table_tbody_row[0])
#print(len(ultrafinedust_table_tbody_row))

month_ultradust_info=[]

td=ultrafinedust_table_tbody_row[0].find_all("td")
print(td)

for content in td:
    print(content.get_text(), end=', ')
    month_ultradust_info.append(content.get_text())
print("")

month_list=['1월','2월','3월','4월','5월','6월','7월','8월','9월','10월','11월','12월']
del month_ultradust_info[0]
month_ultradust_info=[int (i) for i in month_ultradust_info]

print(month_list)
print(month_ultradust_info)

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font',family='Malgun Gothic')

x=range(len(month_list))

fig, ax1=plt.subplots()
ax1.set_title('월별 초미세먼지/미세먼지 농도 자료')
ax1.bar(x,month_ultradust_info,color='gray')
ax1.set_ylim(9,23)
ax1.set_xlabel("2020년")
ax1.set_ylabel("농도(단위:㎍/㎥)")

ax1.set_xticks(x)
ax1.set_xticklabels(month_list)
plt.show()