from reports import *


def export_all_reports (file_name, year, title, genre):
    file = open('games_reports_output.txt','w')
    file.write(str(count_games (file_name))+'\n')
    file.write(str(decide (file_name, year))+'\n')
    file.write(str(get_latest(file_name))+'\n')
    file.write(str(count_by_genre(file_name, genre))+'\n')
    try:
        file.write(str(get_line_number_by_title(file_name, title))+'\n')
    except:
        file.write("There is not such game")
    
    file.close()


#followind doesn't work. Why??? :)
#import sys
#from printing import print_all_reports
#def export_all_reports (file_name, year, title, genre):
    #sys.stdout = open('games_reports_output.txt','w')
    #print_all_reports (file_name, year, title, genre)





if __name__ == '__main__':
    export_all_reports ('game_stat.txt', 2000, "Counter-Strike", "First-person shooter")
