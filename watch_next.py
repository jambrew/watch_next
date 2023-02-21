# A program that reads a text file of movies with descriptions, and recommends
# something for a 'Planet Hulk'-watching movie fan to watch next.

# Imports the spacy module and loads the medium English dictionary as a variable
import spacy
nlp = spacy.load('en_core_web_md')


# A function that takes current movie description as a parameter and returns the closest movie from the list
def find_next_movie_to_watch(current_movie_description):
    
    # Reads the movies text file and creates a list
    list_of_other_movies = []

    with open('movies.txt', 'r', encoding='utf-8') as f:
        # First make a list
        list_of_other_movies = [line.strip().split(':') for line in f]

    # Loop through the movies comparing similarity with the description of the Hulk movie
    for movie in list_of_other_movies:
        similarity = nlp(movie[1]).similarity(description_to_compare)
        movie.append(similarity)

    # Store the closest match in a variable
    closest_match = max(list_of_other_movies, key=lambda x: x[2])

    return closest_match


# Stores our target movie  as a list, and the description as an nlp doc object
current_movie = ["Planet Hulk",
                 "Will he save their world or destroy it? When the Hulk becomes \
        too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him \
        into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land \
        on the planet Sakaar where he is sold into slavery and trained as a gladiator."]

description_to_compare = nlp(current_movie[1])

closest_match = find_next_movie_to_watch(description_to_compare)

# Basic loop to split over multiple lines based on where a new sentence starts,
# printing out the next movie suggestion
print(f'\nIf you liked {current_movie[0]}, we think you\'ll love {closest_match[0].strip()}. Here\'s a description for you:\n')
for count, character in enumerate(closest_match[1], start=1):
    if character == ".":
        print(f'{character}\n', end='')
    else:
        print(character, end='')

print(f'\n Enjoy your next movie!')
