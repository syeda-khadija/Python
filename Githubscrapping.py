import pandas
import os.path
from pydriller import Repository

url = input("Please Enter Repository Link : ")
committername,committeremail,date , projectname ,commitmsg =[],[],[],[],[]
print(f"Fetching{url}")
for a in Repository(url).traverse_commits():
     committername.append(a.author.name)
     committeremail.append(a.author.email)
     date.append(a.committer_date)
     projectname.append(a.project_name)
     commitmsg.append(a.msg)
print("Fetching Completed")
github_dict={
    "Project_name" :projectname,
    "Name" : committername,
    "Email" :committeremail,
    "Message" : commitmsg,
    "Date" :date
}
github_df =pandas.DataFrame(github_dict)
filename =input("Enter filename:")
if os.path.exists(f"{filename}.csv"):
     print(f"{filename} already exist ,please choose different name")
else:
     github_df.to_csv(f"{filename}.csv",index=False)
     print("File created successfully")