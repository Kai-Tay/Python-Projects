import PySimpleGUI as sg
import csv
import pandas as pd

def expensewindow():
    #Opens Expense Window GUI
    expenseeditor = [[sg.Text('Expense Tracker', font=("Callibri",25))],
                     [sg.Text('Description'),sg.InputText(key="Desc")],
                     [sg.Text('Category'),sg.InputText(key="Cat")],
                     [sg.Text('Expense'),sg.InputText(key="Exp")],
                     [sg.Button("Add"), sg.Button("Cancel")]
                     ]
    expensewindow = sg.Window("Expense", expenseeditor, size=(600,300))
    event1, values1 = expensewindow.read()
    while True:
        event, value = expensewindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Add":
            if values1["Desc"] == "" or values1["Cat"] == "" or values1["Exp"] == "":
                expensewindow.close()
                error = [[sg.Button("Error! Try Again!", font=("Callibri",20), button_color=("red"), )]]
                errorwindow = sg.Window("Error", error, size=(200,50))
                errorwindow.read()
                errorwindow.close()
            else:
                #Appending Data
                newexpense = [values1["Desc"], values1["Cat"],values1["Exp"]]
                with open(f"{filename}.csv", "a") as file:
                    write = csv.writer(file)
                    write.writerow(newexpense)
                    expensewindow.close()
                    success = [[sg.Button("Done! Press view to refresh the table!", font=("Callibri",10), button_color=("green"), )]]
                    successwindow = sg.Window("Success!", success, size=(220,50))
                    successwindow.read()
                    successwindow.close()
        elif event == "Cancel":
            expensewindow.close()

def deletewindow():
    #Checks Number Of Rows for GUI Slider
    opencsv = open(f"{filename}.csv")
    number_of_rows = len(list(opencsv)) - 1
    #Opens Expense Window GUI
    deleteeditor = [[sg.Text('Delete', font=("Callibri",25))],
                    [sg.Text('Choose the Row to be deleted:',font=("Callibri",15))],
                    [sg.Slider(range=(0,number_of_rows), size=(90,15),orientation= "h", key='selecteddeletedata')],
                    [sg.Button("Delete"), sg.Button("Cancel")]
                     ]
    deletewindow = sg.Window("Expense", deleteeditor, size=(600,300))
    event1, values1 = deletewindow.read()
    while True:
        event, value = deletewindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Delete":
            #Open Csv file in Pandas and Selects Row
            df = pd.read_csv(f"{filename}.csv",header = None,)
            selected_row = int(values1["selecteddeletedata"])
            #Deletes Selected Row in Pandas
            df.drop([selected_row], inplace=True)
            df.to_csv(f"{filename}.csv", header = None, index_label = None, index = False)
            deletewindow.close()
        elif event == "Cancel":
           deletewindow.close()

#MAINGUI
sg.theme("Reddit")
data = [["Select A Month & Year to View Data"]]
header_list = ["Desc","Category","Expense"]

mainlayout = [[sg.Text('Expense Tracker', font=("Callibri",25))],
              [sg.Text('Month', font=("Callibri", 15)), sg.InputCombo(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], size=(50, 3), key='Month')],
              [sg.Text('Year', font=("Callibri", 15)), sg.InputCombo(['2021', '2022'], size=(52, 100), key='Year')],
              [sg.Button('View')],
              [sg.Table(values=data, headings= header_list,auto_size_columns=False,col_widths=[80, 40, 10],
                        display_row_numbers= True,justification="center", key="Table", row_height=40)],
              [sg.Button("Add New Expense"),sg.Button("Delete Expense")]
          ]

window = sg.Window("$$ Expense Tracker $$", mainlayout, size=(1000,600))
event, values = window.read()

#MAINGUIBUTTONMAPPING
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'View':
        filename = values["Month"]+values["Year"]
        if values["Month"]=="" or values["Year"]=="":
            error = [[sg.Button("Error! Try Again!", font=("Callibri",20), button_color=("red"), )]]
            errorwindow = sg.Window("Error", error, size=(200,50))

            event, values = errorwindow.read()
            errorwindow.close()
        else:
            window.close()
            print(f"{filename}.csv")
            open(f"{filename}.csv", "a")
            with open(f"{filename}.csv", "r") as file:
                reader = csv.reader(file)
                data = list(reader)
                column_names = ["Description","Category","Expense"]
                df = pd.read_csv(f"{filename}.csv",names = column_names)
                total_expenditure = df["Expense"].sum(axis = 0)
                #UI UPDATE
                mainlayout = [[sg.Text('Expense Tracker', font=("Callibri",25))],
                              [sg.Text('Month', font=("Callibri", 15)), sg.InputCombo(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], size=(50, 3), key='Month')],
                              [sg.Text('Year', font=("Callibri", 15)), sg.InputCombo(['2021', '2022'], size=(52, 3), key='Year')],
                              [sg.Button('View'), sg.Text(f"{filename}", font=("Callibri",20))],
                              [sg.Table(values=data, headings= header_list,auto_size_columns=False,col_widths=[80, 40, 10],
                                        display_row_numbers= True,justification="center", key="Table", row_height=40)],
                              [sg.Button("Add New Expense"),sg.Button("Delete Expense"), sg.Text(f"Total Expenditure = {total_expenditure}", font=("Callibri", 15))]
                              ]

                window = sg.Window("$$ Expense Tracker $$", mainlayout, size=(1000,600))
                event, values = window.read()
    elif event == 'Add New Expense':
        expensewindow()
    elif event == 'Delete Expense':
        deletewindow()