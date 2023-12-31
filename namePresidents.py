import os


def list_of_files(directory, extension):
    files_names = []
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            files_names.append(filename)
    return files_names


def name_president(files_names):
    files_names_part_2 = (files_names.split('_'))[1]
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


print(name_president('Nomination_Chirac1.txt'))


dico_names = {"Chirac": "Jacques", "Giscard d'Estaing": "Valéry", "Hollande": "François",
              "Macron": "Emmanuel", "Mitterrand": "François", "Sarkozy": "Nicolas"}


def firstname(files):
    lastname = namepresident(files)
    return dico_names[lastname]


def fullname(files):
    pass
