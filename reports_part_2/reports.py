#removes '\n' signs from end of each lines -> list of strings\(each game as string)
def read_file_lines_make_list (file_name):
    games_list = open (file_name).readlines()
    for i in range(len(games_list)):
        games_list[i] = games_list[i].strip()
    return games_list


# transforms str. of each line to separate list of values -> lists in main list (each game as list)
def values_to_list(file_name):           
    games_list = read_file_lines_make_list (file_name)
    games = []
    for i in range(len(games_list)):
        games.append(games_list[i].split('\t'))
    for i in games:
        i[1] = float(i[1])
        i[2] = int (i[2])
    return games


#Makes list of sold
def list_amounts (file_name):
    games = values_to_list(file_name)
    amounts = []
    for i in games:
        amounts.append(i[1])
    return amounts
    

#part2.1
def get_most_played(file_name):
    games = values_to_list(file_name)
    amounts = list_amounts (file_name)
    #sorting alghoritm for amounts
    i = 1
    while i < len(amounts):
        j = 0
        while j<= len(amounts) - 2:
            if amounts[j] > amounts[j+1]:
                temp = amounts[j+1]
                amounts [j+1] = amounts[j]
                amounts[j] = temp
            j+=1
        i += 1
        
    for i in games:
        if i[1] == amounts[-1]:
            return i[0]
        
        
#part2.2
def sum_sold (file_name):
    amounts = list_amounts (file_name)
    total_sold = sum (amounts)
    return total_sold


#part2.3
def get_selling_avg(file_name):
    amounts = list_amounts (file_name)
    total_sold = sum_sold(file_name)
    average_selling = total_sold / len(amounts)
    return average_selling


#part2.4  dictionary necessery doesn't work yet
'''def count_longest_title(file_name):
    games = values_to_list(file_name)
    length = {}
    for i in games:
        len(i[0])'''


#part2.5
def get_date_avg (file_name):
    games = values_to_list(file_name)
    dates = []
    for i in games:
        dates.append(i[2])
    averege_date = round (sum(dates) / len(dates))
    return averege_date


#part2.6
def get_game(file_name, title):
    games = values_to_list(file_name)
    for i in games:
        if i [0] == title:
            return i


def collect_returns(file_name, title):
    collected = []
    collected.append(get_most_played(file_name))
    collected.append (sum_sold (file_name))
    collected.append (get_selling_avg(file_name))
    #collected.append (count_longest_title(file_name))
    collected.append (get_date_avg (file_name))
    collected.append (get_game(file_name, title))
    return collected


    

def main(file_name, title):
    get_most_played(file_name)
    sum_sold (file_name)
    get_selling_avg(file_name)
    #count_longest_title(file_name))
    get_date_avg (file_name)
    get_game(file_name, title)
    collect_returns(file_name, title)




if __name__ == '__main__':
    file_name ='game_stat.txt'
    title = "Counter-Strike"
    main(file_name, title)




    





