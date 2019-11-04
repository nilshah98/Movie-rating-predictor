import csv

def process(filename):
    attributes = [  "imdb_score",
                    "num_critic_for_reviews",
                    "duration",
                    "director_facebook_likes",
                    "actor_3_facebook_likes",
                    "cast_total_facebook_likes",
                    "movie_facebook_likes",
                    "num_voted_users",
                    "budget",
                    "gross",
                ]

    attributes_index = [-1 for i in range(len(attributes))]
    data = []
    with open(filename) as movie_db:
        movie_data = csv.reader(movie_db, delimiter= ',')
        line_count = 0
        for row in movie_data:
            # getting attribute_index in the order that attributes are
            if line_count == 0:
                for i in range(len(row)):
                    try:
                        index = attributes.index(row[i])
                    except:
                        index = -1
                    if index >= 0:
                        attributes_index[index] = i
                line_count += 1
            else:
                entry = []
                for i in attributes_index:
                    entry.append(row[i])
                data.append(entry)
                line_count += 1

    # Checking number of empty rows for each attribute -
    empty = [0 for i in range(len(attributes_index))]
    total = [0 for i in range(len(attributes_index))]

    for row in data:
        for i in range(len(row)):
            if row[i] == '' or row[i] == '0':
                empty[i] += 1
            else:
                if row[i].isdigit():
                    total[i] += int(row[i])

    # Finding mean on basis of remaining data
    mean = []
    for i in range(len(total)):
        mean.append(total[i]//(len(data) - empty[i]))

    # cleaning data by substituting mean and splitting genres
    for row in data:
        # substituting mean for missing or 0 numerical data
        for i in range(len(row)):
            if row[i] == '' or row[i] == '0':
                row[i] = mean[i]

        # converting numerical data to int or float from string
        for i in range(len(row)):
            row[i] = int(round(float(row[i])))

    # writing new csv
    with open('movie_metadata_filtered_aftercsv.csv','w') as findata:
        findata = csv.writer(findata, delimiter=',')
        findata.writerow(attributes)
        for i in data:
            findata.writerow(i)
            print(i)

def main():
    process('movie_metadata.csv')

if __name__ == "__main__":
    main()