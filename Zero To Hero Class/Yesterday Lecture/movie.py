import json
import os

def add_movie(watchlist, name, *args, **kwargs):
    # Add a new movie and return updated list
    if not name or not name.strip():
        print("Movie name cannot be empty")
        return watchlist
    movie_id = max([movie["id"] for movie in watchlist], default=0) + 1
    new_movie = {
        "id": movie_id, 
        "name": name.strip().title(), 
        "watched": False
    }
    return watchlist + [new_movie]

def view_movies(
        watchlist, show_watched_only=False, 
        show_unwatched_only=False
):
    # Return filtered watchlist for display
    filtered_list = watchlist
    if show_watched_only:
        filtered_list = [movie for movie in watchlist if movie["watched"]]
    elif show_unwatched_only:
        filtered_list = [movie for movie in watchlist if not movie["watched"]]
    return filtered_list

def mark_watched(watchlist, movie_id):
    # Mark movie as watched
    for movie in watchlist:
        if movie["id"] == movie_id:
            movie["watched"] = True
            return watchlist
        print(f"Movie with ID {movie_id} not found")
    return watchlist

def delete_movie(watchlist, movie_id):
    # Delete movie from watchlist
    new_list = [movie for movie in watchlist if movie["id"] != movie_id]
    if len(new_list) == len(watchlist):
        print(f"Movie with ID {movie_id} not found")
    return new_list

def save_watchlist(watchlist, filename="watchlist.json"):
    # Save watchlist to file
    with open(filename, 'w') as f:
        json.dump(watchlist, f)

def load_watchlist(filename="watchlist.json"):
    # Load watchlist from file
    try:
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return json.load(f)
        return []
    except json.JSONDecodeError:
        print("Error loading watchlist file. Starting with empty watchlist.")
        return []

# Main program
watchlist = load_watchlist()
while True:
    print("\nMovie Watchlist Menu:")
    print("1. Add Movie")
    print("2. View All Movies")
    print("3. View Watched Movies")
    print("4. View Unwatched Movies")
    print("5. Mark Movie as Watched")
    print("6. Delete Movie")
    print("7. Exit")
    
    choice = input("Enter choice (1-7): ")
    
    if choice == "1":
        name = input("Enter movie name: ").strip().trip
        watchlist = add_movie(watchlist, name)
        save_watchlist(watchlist)
        print("Movie added!")
    
    elif choice == "2":
        movies = view_movies(watchlist)
        if not movies:
            print("No movies in watchlist!")
        else:
            for movie in movies:
                status = "Watched" if movie["watched"] else "Unwatched"
                print(f"ID: {movie['id']}, Movie: {movie['name']} ({status})")
    
    elif choice == "3":
        movies = view_movies(watchlist, show_watched_only=True)
        if not movies:
            print("No watched movies in watchlist!")
        else:
            for movie in movies:
                print(f"ID: {movie['id']}, Movie: {movie['name']} (Watched)")
    
    elif choice == "4":
        movies = view_movies(watchlist, show_unwatched_only=True)
        if not movies:
            print("No unwatched movies in watchlist!")
        else:
            for movie in movies:
                print(f"ID: {movie['id']}, Movie: {movie['name']} (Unwatched)")
    
    elif choice == "5":
        try:
            movie_id = int(input("Enter movie ID to mark as watched: "))
            watchlist = mark_watched(watchlist, movie_id)
            save_watchlist(watchlist)
            print("Movie marked as watched!")
        except ValueError:
            print("Please enter a valid number")
    
    elif choice == "6":
        try:
            movie_id = int(input("Enter movie ID to delete: "))
            watchlist = delete_movie(watchlist, movie_id)
            save_watchlist(watchlist)
            print("Movie deleted!")
        except ValueError:
            print("Please enter a valid number")
    
    elif choice == "7":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice. Please enter a number between 1 and 7.")