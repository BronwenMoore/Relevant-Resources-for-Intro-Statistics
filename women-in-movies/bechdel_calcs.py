import csv



def goThroughDecades():
	beginning_year = 1891
	while beginning_year <= 2011:
		get_decade(beginning_year, beginning_year+9)
		beginning_year += 10


def get_decade(beginning_year, end_year):
	year_key = 1
	pass_key = 4
	rating_key = 3
	all_movies_num = 0
	pass_movies_num = 0
	two_women_movies_num = 0

	with open('bachdel.csv') as csv_file:
    		csv_reader = csv.reader(csv_file, delimiter=',')
    		line_count = 0
    		for row in csv_reader:
        		if line_count == 0:
            			line_count += 1
	    			continue
			year = int(row[year_key])
			if(year >= beginning_year and year <= end_year):
	    			all_movies_num += 1
 	    			if(int(row[pass_key]) == 1):
	    				pass_movies_num += 1
 	    			if(int(row[rating_key]) <= 1):
	    				two_women_movies_num += 1
       			line_count += 1
		print(str(beginning_year) + " - " + str(end_year))
		print("\t# of movies: \t\t\t\t\t\t" + str(all_movies_num))
		print("\t# of movies that passed: \t\t\t\t" + str(pass_movies_num))
		print("\t% of movies that passed: \t\t\t\t" + str((pass_movies_num*1.0)/all_movies_num))
		print("\t# of movies without a conversation between 2 women: \t" + str(two_women_movies_num))
		print("\t% movies without a conversation between 2 women: \t" + str((two_women_movies_num*1.0)/all_movies_num))


goThroughDecades()
