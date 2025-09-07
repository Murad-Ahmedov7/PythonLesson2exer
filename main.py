import pandas as pd
from functools import  reduce
df=pd.read_excel("day2_dataset_map_filter_reduce (1).xlsx")
df["Skills"] = df["Skills"].str.split(", ")
data_list=df.to_dict(orient="records")

# print(data_list)

# 1) Map: 'Name' sütununu hamısını böyük hərflərə çevirərək yeni siyahı yaradın.

upper_Names=list(map(lambda x:x["Name"].upper(),data_list))
print(upper_Names)

#
# # 2) Map: 'SalaryAZN' dəyərlərini 10% artımla (round) yeni siyahıda göstərin.
#
increased_salary=list(map(lambda s:{**s,"SalaryAZN":round(s["SalaryAZN"]*1.1)},data_list))
print(increased_salary)
#
# # 3) Filter: Yalnız 'City' = 'Baku' olan əməkdaşları seçin (sətir siyahısı).
#
city_Baku=list(filter(lambda c:c['City']=="Baku",data_list))
print(city_Baku)
#
#
# # 4) Filter: 'Age' >= 30 və 'Department' = 'Engineering' olanları çıxarın.
#
filtered_employees=list(filter(lambda e:e['Age']>30 and e['Department']=='Engineering',data_list))
print(filtered_employees)
#
# #5) Filter: 'Remote' = True və 'Performance' >= 80 olan sətirləri seçin.

filtered_Performance=list(filter(lambda e:e['Remote']==True and e['Performance']>=80,data_list))
print(filtered_Performance)
#
#
# # 6) Reduce: Bütün 'SalaryAZN' toplamını hesablayın.
#
sum_of_salaries=reduce(lambda a,b:a+b["SalaryAZN"],data_list,0)
print(sum_of_salaries)
#
# #7) Reduce: 'SalaryAZN' üzrə maksimumu və minimumu tapın.
#
max_salary = max(data_list, key=lambda x: x["SalaryAZN"])
print(max_salary)
#
min_salary=min(data_list, key=lambda x: x["SalaryAZN"])

print(min_salary)

#8) Map+Filter: 'Skills' içində 'python' olan əməkdaşların adlarını böyük hərflərlə qaytarın.
#
all_skills=list(map(lambda x:x["Skills"],filter(lambda x:x["Skills"]=="python",data_list)))

python_names = list(
    map(lambda x: { **x,"Name":x["Name"].upper()}, filter(lambda l: "python" in l["Skills"], data_list))
)

print(python_names)


# 9) Map: 'JoinDate' dəyərlərini 'YYYY-MM' formatına salın.

from datetime import datetime

Join_Date=list(
    map(lambda x: {**x,"JoinDate":datetime.strptime(x["JoinDate"],"%Y-%m-%d").strftime("%Y-%m")},data_list)
)
print(Join_Date)

# 10) Filter+Reduce: 'City' = 'Baku' olanların 'SalaryAZN' cəmini hesablayın.

city_baku_salaries=reduce( lambda x,y:x+y["SalaryAZN"],filter(lambda x:x['City']=="Baku",data_list),0)
print(city_baku_salaries)
#
#
# # 11) Map: 'Performance' balına görə kateqoriya təyin edin: 1-59='Low', 60-79='Medium', 80-100='High'.
#
performance_category=list(map(lambda x: {**x, "PerformanceCategory": "high" if x["Performance"]>=80 else "medium" if 79>=x["Performance"]>=60 else "low"},data_list))
print(performance_category)

# #12) Filter: 'Skills' içində 'django' VƏ 'docker' olan sətirləri çıxarın.
#
selected_skills=list(filter(lambda x: "django" in x["Skills"] and "docker" in x["Skills"],data_list))
print(selected_skills)


# # 13) Map: 'Age' → gələn il üçün yaş (Age+1) siyahısını yaradın.
#
new_age=list(map(lambda x: x["Age"]+1,data_list))
print(new_age)


# 14) Filter+Map: 'Department' = 'Data' olanların maaşını 15% artırıb yeni siyahı yaradın.

department_data=(filter(lambda x : x["Department"]=='Data', data_list))

increased_salaries=list(map(lambda x : round(x["SalaryAZN"]*1.15,2), department_data))

print(increased_salaries)

# 15) Bonus: 'Engineering' şöbəsində 'python' bilənlərin orta maaşını hesablayın.


filter_engineering=list(filter(lambda x :x["Department"]=="Engineering" and "python" in x["Skills"], data_list))

average_salary=reduce( lambda x,y:x+y["SalaryAZN"]/len(filter_engineering),filter_engineering,0)

print(average_salary)