import pandas as pd
import ast
import xlsxwriter

df = pd.read_csv('file3.csv', nrows=10)
emails_column = df.loc[:,"emails"]
# print(emails_column)
values = pd.Series(emails_column)
email_list = values.tolist()
# print(email_list)

# Get the first value of the email list
# print(ast.literal_eval(email_list[1])[0])


# for i in range(0, len(ast.literal_eval(email_list[1]))):
#     if((ast.literal_eval(email_list[1])[i])['type'] == 'personal'):

# Email list with the email type "personal"
for emails in email_list:
    for i in range(0, len(ast.literal_eval(emails))):
        if(ast.literal_eval(emails)[i]['type']) == 'personal':
            personal_emails = ast.literal_eval(emails)[i]
            print(personal_emails)  

            # workbook = xlsxwriter.Workbook('demo.xlsx')
            # worksheet = workbook.add_worksheet()
            # for value in personal_emails.values():

            #     worksheet.write_string()
            # workbook.close()


            
            # for customer in email_list.tolist():
            #     print(personal_emails.values())[0]