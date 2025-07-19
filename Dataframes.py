import pandas as pa
import lxml
from openpyxl.workbook import Workbook
#     "name":["Ali","Sara","Urwa","Hareem","Moiz"],
#     "Gender":["M","F","F","F","M"],
#     "Age":[29,24,23,22,28],
#     "caste":["Syed","Siddiqui","Qureshi","Syed","Malik"],
#     "Preferred_area":["Nazimabad","Gulshan","Defence","Shahra-e-faisal","Gulistan-e-johar"],
#     "Profession":["Doctor","Designer","Textile_Engineer","Teacher","CA"],
#     "No_of_sibling":[2,3,0,5,4]
# }
# df_rprofile =pa.DataFrame(rishta_profile)
#
#
# print(df_rprofile[df_rprofile["caste"] == "Khan"])
# print(df_rprofile[df_rprofile["No_of_sibling"]>2])
# print(df_rprofile[df_rprofile["Preferred_area"]=="Defence"])
# print(df_rprofile[(df_rprofile["Gender"]=="F") & (df_rprofile["Preferred_area"] == "Nazimabad")])
# #Add column
# df_rprofile["Marital_status"]=["Divorce","Single","Single","Single","Divorce"]
# df_rprofile["Nationality"]="Pakistani"
# #Remove
# del df_rprofile["Profession"]
# print(df_rprofile)

dishes={
    "Food_name":["Biryani","Zinger","Shawarma","Mutton-Karhai","Nihari","Pizza"],
    "Price":[250,500,400,1500,700,2000],
    "Category":["Desi","Fat-food","Fast-food","Desi","Desi","Italian"],
    "Main_ingredient":["Rice","Chicken","Chicken","Mutton","beef","Pita-bread"],
    "Quantity":[10,25,35,8,10,25],
    "Status":["avaliable","avaliable","unavaliable","avaliable","unavaliable","avaliable"],
}
df_dishess=pa.DataFrame(dishes)
df_dishess["Country"]="Pakistani"
df_dishess["Sale_price"]=[200,400,300,1200,500,1500]
print(df_dishess[df_dishess["Price"]>500])
print(df_dishess[(df_dishess["Status"]=="avaliable") & (df_dishess["Category"] == "Fast-food")])
print(df_dishess[df_dishess["Food_name"] == "Biryani"])
print(df_dishess[(df_dishess["Status"]=="avaliable") & (df_dishess["Price"]>1500)])
choice =input("Enter c - CSV\nx- Xml\nj - JSON\ne - EXCEL")
if (choice.lower() == "c"):
    df_dishess.to_csv("MYCSVFILE.csv",Index=False)
elif (choice.lower() == "e"):
    df_dishess.to_xml("MYXMLFILE.xml")
elif (choice.lower() == "j"):
    df_dishess.to_json("MYJSONFILE.js")
elif (choice.lower() == "e"):
    df_dishess.to_excel("MYEXCELFILE.xslx")
else:
    print("Invalid Input")
print(df_dishess)