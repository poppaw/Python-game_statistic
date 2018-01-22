from reports import *


def export_all_reports (file_name, year, title, genre):
    collected = collect_returns(file_name, title)
    file = open('games_reports2_output.txt','w')
    for i in collected:
        file.write(str(i)+'\n')
         
    file.close()


#followind doesn't work. Why??? :)
#import sys
#from printing import print_all_reports
#def export_all_reports (file_name, year, title, genre):
    #sys.stdout = open('games_reports_output.txt','w')
    #print_all_reports (file_name, year, title, genre)





if __name__ == '__main__':
    export_all_reports ('game_stat.txt', 2000, "Counter-Strike", "First-person shooter")
