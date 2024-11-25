import re
import subprocess


def normalize(text: str):
    text = text.strip().replace("-", " ")
    text = text.replace("'", " ")
    text = text.replace("&", "and")
    text = text.title()
    text = text.replace(".", "")
    text = text.replace(",", "")
    text = text.replace(" ", "")
    text = text.replace("/", "")
    text = text.replace("[", "").replace("]", "").replace("\"", "")
    nums = set(re.findall(r"[0-9]+", text))
    if nums:
        for num in nums:
            text = text.replace(num, " "+num)
    text = "".join((" " + char if char.isupper() else char for char in text))
    text = text.replace("( ", " (")

    return text.strip()


def write_sets(actor_dict, movie_dict):
    try:
        actors = open("actors.txt", 'w')
        movies = open("movies.txt", 'w')
        actor2movie = open("actor2movie.txt", 'w')
        movie2actor = open("movie2actor.txt", 'w')

        print("[", file=actors)
        print("[", file=movies)
        print("[", file=actor2movie)
        print("[", file=movie2actor)

        for actor, movie in actor_dict.items():
            print(f"\t[\"{actor}\"],", file=actors)
            print(f"\t[\"{actor}\", \"{movie}\"],", file=actor2movie)

        for movie, actor in movie_dict.items():
            print(f"\t[\"{movie}\"],", file=movies)
            print(f"\t[\"{movie}\", \"{actor}\"],", file=movie2actor)

        print("]", file=actors)
        print("]", file=movies)
        print("]", file=actor2movie)
        print("]", file=movie2actor)

        print("succes")

    except:
        print("an error occurred with a file")
    finally:
        actors.close()
        movies.close()
        actor2movie.close()
        movie2actor.close()


def read_imdb_data(filename, actor_dict, movie_dict):
    nums = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    with open(filename, 'r') as f:
        for actor in f.read().split("\n\n"):
            ##print(actor.lower())
            # check if its an actor
            if "actor" not in actor.lower() and "actress" not in actor.lower():
                continue

            actor = actor.split("\n")
            if len(actor) <= 2:
                continue

            # find name
            for line in actor:
                if line.startswith(nums):
                    name = line.split(". ", 1)[-1]
                    break
            if not name:
                continue
            name = normalize(name)

            # find movie
            movie = actor[-1][::-1].split("( ", 1)[-1][::-1]
            if not movie:
                continue
            movie = normalize(movie)

            if name not in actor_dict or movie not in movie_dict:
                print("new")

            if name not in actor_dict:
                actor_dict[name] = movie
            if movie not in movie_dict:
                movie_dict[movie] = name


    return actor_dict, movie_dict


def previous_data(filename):
    dictionary = {}
    with open(filename, 'r') as file:
        for line in file:
            if "," not in line:
                continue
            first, second = line.split(",", 1)
            first = normalize(first)
            second = normalize(second)
            dictionary[first] = second
    #print(len(dictionary))
    return dictionary


def main():

    actor_dict = previous_data("maps/actor2movie.map")
    movie_dict = previous_data("maps/movie2actor.map")
    actor_dict, movie_dict = read_imdb_data("imdb_data.txt", actor_dict, movie_dict)
    write_sets(actor_dict, movie_dict)            

main()