import pandas as pd
import urllib.request


excel_file = 'Plugins.xlsx'

def print_current():
    df = pd.read_excel(excel_file)
    current_list = list(df['Name'])
    return current_list

#Takes our plugin excel and turns it into a dictionary with names mapped to urls
def NamestoUrls(dp):
    name_list = []
    url_list = []

    data = pd.read_excel(excel_file)
    

    for name in data.Name:
        name_list.append(name)
    
    for url in data.URL:
        url_list.append(url)
    
    for x in range(len(name_list)):
        dp[name_list[x]] = url_list[x]
    
    
    return dp

#Test the connection of a URL to see if it is a dead link or not
def TestConnection(url):
    test_url = "https://" + str(url) + "/status"

    try:
        urllib.request.urlopen(test_url)
        return True
    except:
        return False

def url_status():
    database = {}
    status_database = {}
    NamestoUrls(database)
    
    for key in database.keys():
        if TestConnection(database[key]):
            status_database[key] = "Working"
        else:
            status_database[key] = "Broken"
    
    return status_database

#Adds a new plugin to the file and creates a new excel file with the updated info
def addPlugin(name, type, port, archive, language, test, description, endpoint, repository, docker, url):
    currentFrame = pd.read_excel(excel_file)
    last_row = currentFrame.tail(1)

    row = pd.DataFrame({
    'Name': name, 
    'Type': type, 
    'Port': int(port), 
    'Archive': archive, 
    'Language': language, 
    'Test': test, 
    'Description': description, 
    'Multi-Endpoint': endpoint,
    'Repository': repository,
    'DockerFiler': docker,
    'URL': url},
    index = [0])

    #append the row to the dataframe of the excel file that we have right now
    df = currentFrame.append(row, ignore_index=True)
    df.to_excel(excel_file, index=False)
    
#Removing a plugin (based on the given name) from the excel file and makes a new excel with the updated info
def removePlugin(name):
    df = pd.read_excel(excel_file)
    remove_list = df.index[df['Name']==name].tolist()
    if remove_list:
        df.drop(remove_list, axis=0, inplace=True)
        df.to_excel(excel_file, index=False)
        #print(name + " has been deleted!")
        return True
        
    else:
        #print("That plugin is not in the file")
        return False
        

def Main():
    print("\n")
    print("Please pick an option!")
    print("1. Add new plugin to file.")
    print("2. Remove a plugin from file.")
    print("3. Check plugin URL status.")
    print("4. Show current plugins in file.")
    print("5. Exit")
    option = input("Your choice: ")

    if option == '1':
        option_one()

    if option == '2':
        option_two()

    if option == '3':
        option_three()

    if option == '4':
        option_four()

    if option == '5':
        exit()
    

def option_one():
    print("\n")
    name = input("Name of the plugin: ")
    type = input("Type of the plugin: ")
    port = input("Port of the plugin: ")
    archive = input("Archive the plugin? (Yes/No): ")
    language = input("What language is the plugin? ")
    test = input("Test the plugin? (Yes/No): ")
    description = input("Give a description of the plugin: ")
    endpoint = input("Multi-Endpoints? (Yes/No): ")
    repository = input("Link to the repo: ")
    docker = input("Link to the dockerfile: ")
    url = input("URL of the plugin: ")

    addPlugin(name, type, port, archive, language, test, description, endpoint, repository, docker, url)

    choice = input("Print the current file? (Y/N): ")

    if choice == 'Y':
        option_four()
    else:
        Main()

def option_two():
    name = input("What is the name of the plugin to remove? ")
    removePlugin(name)

    choice = input("Print the current file? (Y/N): ")

    if choice == 'Y':
        option_four()
    else:
        Main()



def option_three():
    database = {}
    status_database = {}
    NamestoUrls(database)

    choice = input("Would you like to check a single plugin URL or all URLs? (single/all): ")
    if choice == "single":
        name = input("What is the name of the plugin? ")
        if TestConnection(database[name]):
            print("The URL is working properly.")
        else:
            print("The URL is not a valid URL.")
        
        Main()
    
    else:
        for key in database.keys():
            if TestConnection(database[key]):
                status_database[key] = "Working"
            else:
                status_database[key] = "Broken"
    

    for key in status_database.keys():
        print(key + ": " + status_database[key])
    
    choice = input("Would you like to remove the dead plugins? (Yes/No): ")
    if choice == 'Yes':
        choice_sure = input("You are about to delete plugins with invalid links. Are you sure? (Yes/No): ")
        if choice_sure == 'Yes':
            for name in status_database.keys():
                if status_database[name] == "Broken":
                    removePlugin(name)
            
        else:
            Main()
            
    Main()

    
    





def option_four():
    df = pd.read_excel(excel_file)
    print("\n")
    print(df['Name'])
    
    Main()




#First Starting Function
def StartingMain():
    print("Welcome to the Plugin Checker, please pick an option!")
    print("1. Add new plugin to file.")
    print("2. Remove a plugin from file.")
    print("3. Check plugin URL status.")
    print("4. Show current plugins in file.")
    print("5. Exit")
    option = input("Your choice: ")

    if option == '1':
        option_one()

    if option == '2':
        option_two()

    if option == '3':
        option_three()

    if option == '4':
        option_four()

    if option == '5':
        exit()

#StartingMain()
print_current()
