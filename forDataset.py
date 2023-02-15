import csv   
import pandas as pd

# username = input("Enter your username : ")
# password = input("Enter your password : ")

# with open('usersdata.csv', 'r') as f:
#     rd = csv.reader(f)
#     mylist = list(rd)
    
# mylist[i][2] = score

# with open('usersdata.csv', 'w', newline='') as f:
#     w = csv.writer(f)
#     w.writerows(mylist) 
    
    # w.writerow(["username", "password", "points"])
    # w.writerow([username, password,5000])

df = pd.read_csv('usersdata.csv')
print(len(df))
print(df["Points"][])