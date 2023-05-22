import ast
import pandas as pd

df = pd.read_csv('file3.csv')
email_list = df['emails'].values.tolist()

no_of_emails = []
for i in email_list:
    if 'personal' in i:
        no_of_emails.append(i.count('personal'))

    else:
        print('None')

count = 0
pmail = []
for i,j in enumerate(email_list):
    b = email_list[i].split(',')
    for i,j in enumerate(b):
        if 'personal' in j:
            pmail.append(b[i-1].split(':')[1])
            count += 1

count = 0
k = 0

for i in no_of_emails:
    email = ''
    for j in range(0,i):
        if i > 1:
            email = email + pmail[k] + ', '
        else:
            email = email + pmail[k] 
        k = k + 1
    df.loc[df.index[count], 'Personal_Email'] = email
    count += 1


df.to_csv("new_file3")