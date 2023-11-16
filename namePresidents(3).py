import os
def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def namepresident(files):



names = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Hollande": "François",
         "Macron": "Emmanuel", "Mitterrand": "François","Sarkozy": "Nicolas"}


def firstname(files):
    lastname = namepresident(files)
    return names[lastname]


def fullname(files):
    pass
