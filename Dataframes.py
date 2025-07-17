import pandas as pa
rishta_profile ={
    "name":["Ali","Sara","Urwa","Hareem","Moiz"],
    "Gender":["M","F","F","F","M"],
    "Age":[29,24,23,22,28],
    "caste":["Syed","Siddiqui","Qureshi","Syed","Malik"],
    "Preferred_area":["Nazimabad","Gulshan","Defence","Shahra-e-faisal","Gulistan-e-johar"],
    "Profession":["Doctor","Designer","Textile_Engineer","Teacher","CA"],
    "No_of_sibling":[2,3,0,5,4]
}
df_rprofile =pa.DataFrame(rishta_profile)


print(df_rprofile[df_rprofile["caste"] == "Khan"])
print(df_rprofile[df_rprofile["No_of_sibling"]>2])
print(df_rprofile[df_rprofile["Preferred_area"]=="Defence"])
print(df_rprofile[(df_rprofile["Gender"]=="F") & (df_rprofile["Preferred_area"] == "Nazimabad")])
#Add column
df_rprofile["Marital_status"]=["Divorce","Single","Single","Single","Divorce"]
df_rprofile["Nationality"]="Pakistani"
#Remove
del df_rprofile["Profession"]
print(df_rprofile)