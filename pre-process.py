import csv

attributes = [  "imdb_score",
                "num_critic_for_reviews",
                "duration",
                "director_facebook_likes",
                "actor_1_facebook_likes",
                "actor_2_facebook_likes",
                "actor_3_facebook_likes",
                "budget",
                "movie_facebook_likes",
                "gross"
            ]

attributes_index = [-1 for i in range(len(attributes))]
data = []
with open('movie_metadata.csv', encoding='utf-8') as movie_db:
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

print(empty)
print(total)
print(len(data))

# Finding mean on basis of remaining data
mean = []
for i in range(len(total)):
    mean.append(total[i]//(len(data) - empty[i]))

print(mean)

# cleaning data by substituting mean and splitting genres
# genres = []
for row in data:

    # substituting mean for missing or 0 numerical data
    for i in range(len(row)):
        if row[i] == '' or row[i] == '0':
            row[i] = mean[i]

    # converting numerical data to int or float from string
    # genre = row.pop()
    for i in range(len(row)):
        try:
            row[i] = int(row[i])
        except:
            row[i] = float(row[i])

    # replacing genres by their index in the global genre list
    # genre = genre.split("|")
    # for i in genre:
    #     if i not in genres:
    #         genres.append(i)
    # for i in range(len(genre)):
    #     genre[i] = genres.index(genre[i])
    # row.append(genre)
    print(row)

# print(genres)
