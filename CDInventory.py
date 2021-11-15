#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# NWoodward, 2021-Nov-14, Modify inner data type list->dict, add del + load functionality
#------------------------------------------#

# Declare variabls

strChoice = '' # User input
lstTbl = []  # list of dictionaries to hold data
dicRow = {}  # dictionary of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    # 1. Display menu allowing the user to choose:
    print('\n[l] Load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
    print('[d] Delete CD from Inventory\n[s] Save Inventory to file\n[x] Exit')
    strChoice = input('l, a, i, d, s or x: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'x':
        # 6. Exit the program if the user chooses so
        break
    if strChoice == 'l': # no elif necessary, as this code is only reached if strChoice is not 'exit'
        # 1. Load existing data
        print('Loading CD\'s from the CD Inventory\n')
        lstTbl = []
        objFile = open(strFileName, 'r')
        for row in objFile:
            lstRow = row.strip().split(',')
            dicRow = {'ID': int(lstRow[0]), 'CD Title': lstRow[1], 'Artist': lstRow[2]}
            lstTbl.append(dicRow)
        objFile.close()
    elif strChoice == 'a':  
        # 2. Add data to the table (2D data structure) each time the user wants to add data
        strID = input('Enter an ID number: ')
        strTitle = input('Enter the CD\'s Title: ')
        strArtist = input('Enter the Artist\'s Name: ')
        intID = int(strID)
        dicRow = {'ID': intID,'CD Title': strTitle,'Artist': strArtist}
        lstTbl.append(dicRow)
    elif strChoice == 'i':
        # 3. Display the current data to the user each time the user wants to display the data
        print('ID, CD Title, Artist')
        for row in lstTbl:
            print(row['ID'],row['CD Title'],row['Artist'], sep=', ')
    elif strChoice == 'd':
        # 4. Delete an entry
        badCD = int(input('Enter the ID of the CD you would like to delete: '))
        for i in range(len(lstTbl)):
            if lstTbl[i]['ID'] == badCD:
                del lstTbl[i]
                break
    elif strChoice == 's':
        # 5. Save the data to a text file CDInventory.txt if the user chooses so
        objFile = open(strFileName, 'w')
        for row in lstTbl:
            strRow = ''
            idnum = str(row['ID'])
            title = row['CD Title']
            artist = row['Artist']
            strRow = idnum + ', ' + title + ', '+ artist + '\n'
            objFile.write(strRow)
        objFile.close()
    else:
        print('Please choose either l, a, i, d, s or x!')

