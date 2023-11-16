import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def namepresident(files_names):
    files_names.split('_')
    files_names_part_2 = files_names[1]
    files_names_short = files_names_part_2[:2]
    if files_names_short == "Ch":
        return "Chirac"
    elif files_names_short == "Gi":
        return "Giscard d'Estaing"
    elif files_names_short == "Ho":
        return "Hollande"
    elif files_names_short == "Ma":
        return "Macron"
    elif files_names_short == "Mi":
        return "Mitterrand"

    elif files_names_short == "Sa":
        return "Sarkozy"


dico_names = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Hollande": "François",
         "Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas"}


def firstname(files):
    lastname = namepresident(files)
    return names[lastname]


def fullname(files):
    pass

