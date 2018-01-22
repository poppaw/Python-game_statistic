from reports import *

def print_all_reports (file_name, year, title, genre):
    print (count_games (file_name))
    print (decide (file_name, year))
    print (get_latest(file_name))
    print (count_by_genre(file_name, genre))
    try:
        print (get_line_number_by_title(file_name, title))
    except Exception:
        print ("There is not such game:", title)
    #print: place for extras
    #print




if __name__ == '__main__':
    print_all_reports ('game_stat.txt', 2000, "Counter-Strike", "First-person shooter")
    


    
