import PySimpleGUI as sg
import csv

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
                print(newexpense)
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
    #Opens Expense Window GUI
    deleteeditor = [[sg.Text('Delete', font=("Callibri",25))],
                    [sg.Text('Select the Row to be deleted:')],
                    [sg.Listbox(values=data, size=(90,15), key='selecteddeletedata')],
                    [sg.Button("Delete"), sg.Button("Cancel")]
                     ]
    deletewindow = sg.Window("Expense", deleteeditor, size=(600,300))
    event1, values1 = deletewindow.read()
    while True:
        event, value = deletewindow.read()
        if event == sg.WIN_CLOSED:
            break
        elif event == "Delete":
            #Converting to List
            deletelist = values1['selecteddeletedata']
            stringdata = "".join(str(e) for e in deletelist)
            deletedata= stringdata.replace("'","").replace("[","").replace("]","")
        #Deleting data from csvfile
            with open(f"{filename}.csv", "r") as file:
                reader = csv.reader(file)
                with open(f"{filename}.csv", "w") as write:
                    writer = csv.writer(write)
                    for row in reader:
                        if row != deletedata:
                            writer.write(row)
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
                print("File Opened!")
                #UI UPDATE
                mainlayout = [[sg.Text('Expense Tracker', font=("Callibri",25))],
                              [sg.Text('Month', font=("Callibri", 15)), sg.InputCombo(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'], size=(50, 3), key='Month')],
                              [sg.Text('Year', font=("Callibri", 15)), sg.InputCombo(['2021', '2022'], size=(52, 3), key='Year')],
                              [sg.Button('View'), sg.Text(f"{filename}", font=("Callibri",20))],
                              [sg.Table(values=data, headings= header_list,auto_size_columns=False,col_widths=[80, 40, 10],
                                        display_row_numbers= True,justification="center", key="Table", row_height=40)],
                              [sg.Button("Add New Expense"),sg.Button("Delete Expense")]
                              ]

                window = sg.Window("$$ Expense Tracker $$", mainlayout, size=(1000,600))
                event, values = window.read()
    elif event == 'Add New Expense':
        expensewindow()
    elif event == 'Delete Expense':
        deletewindow()