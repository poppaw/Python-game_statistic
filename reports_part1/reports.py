#1 removes '\n' signs from end of each lines -> list of strings (each game as string)
def read_file_lines_make_list (file_name):
    games_list = open (file_name).readlines()
    for i in range(len(games_list)):
        games_list[i] = games_list[i].strip()
    return games_list


#2
# transforms str. of each line to separate list of values -> lists in main list (each game as list)
def values_to_list(file_name):           
    games_list = read_file_lines_make_list (file_name)
    games = []
    for i in range(len(games_list)):
        games.append(games_list[i].split('\t'))
    return games


#3    
def count_games (file_name):
    games_list = read_file_lines_make_list (file_name)
    counter = len (games_list)
    return counter
       

#4
def decide (file_name, year):
    games_list = read_file_lines_make_list (file_name)
    for line in games_list:
        if str(year) in line:
            return True
    return False
   

#5   
def get_latest(file_name):
    games = values_to_list(file_name)
    dates = []
    for i in games:
        dates.append(i[2])
    #sorting alghoritm for dates
    i = 1
    while i < len(dates):
        j = 0
        while j<= len(dates) - 2:
            if dates[j] > dates[j+1]:
                temp = dates[j+1]
                dates [j+1] = dates[j]
                dates[j] = temp
            j+=1
        i += 1
        
    for i in games:
        if i[2] == dates[-1]:
            return i[0]
                

#6
def count_by_genre(file_name, genre):
    games_list = open (file_name).readlines()
    counter = 0
    for i in games_list:
        if genre in i:
            counter +=1
    return counter


#7
def get_line_number_by_title(file_name, title):
    games_list = open (file_name).readlines()

    for line in games_list:
        if title+'\t' in line in line:
            return games_list.index(line) + 1
        
    raise Exception ('ValueError: No index with such title')


#8
def list_titles(file_name):
    games = values_to_list(file_name)
    titles = []
    for i in games:
        titles.append(i[0])   
    return titles
    

def sort_abc (file_name):
    titles = list_titles(file_name)
    i = 1
    while i < len(titles):
        j = 0
        while j<= len(titles) - 2:
            if titles[j] > titles[j+1]:
                temp = titles[j+1]
                titles [j+1] = titles[j]
                titles[j] = temp
            j+=1
        i += 1     
    return titles


#9
def list_genres (file_name):
    games = values_to_list(file_name)
    genres = []
    for i in games:
        if str(i[3]) not in genres:
            genres.append(i[3])     
    return genres


def get_genres(file_name):
    genres = list_genres(file_name)
    i = 1
    while i < len(genres):
        j = 0
        while j<= len(genres) - 2:
            if genres[j] > genres[j+1]:
                temp = genres[j+1]
                genres [j+1] = genres[j]
                genres[j] = temp
            j+=1
        i += 1
    print (genres)
    return genres
    
    
