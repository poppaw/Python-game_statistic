from reports import *

def print_all_reports (file_name, year, title, genre):
    collected = collect_returns(file_name, title)
    for i in collected:
        print (i)



if __name__ == '__main__':
    file_name = 'game_stat.txt'
    year = 2000
    title = "Counter-Strike"
    genre = "First-person shooter"
    print_all_reports (file_name, year, title, genre)
    


    
