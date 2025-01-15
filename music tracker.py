
SONGS_FILE = "songs.txt"
LIKES_FILE = "likes.txt"
DISLIKES_FILE = "dislikes.txt"

def initialize_files():
    open(SONGS_FILE, 'a').close()  
    open(LIKES_FILE, 'a').close()  
    open(DISLIKES_FILE, 'a').close()  

def add_song(song, artist):
    with open(SONGS_FILE, 'a') as f:
        f.write(f"{song},{artist}\n")

def get_most_listened():
    song_count = {}
    artist_count = {}

    with open(SONGS_FILE, 'r') as f:
        for line in f:
            
            parts = line.split(',')
            if len(parts) < 2:
                continue  
            song = parts[0]
            artist = parts[1].rstrip('\n')  

            
            if song in song_count:
                song_count[song] += 1
            else:
                song_count[song] = 1
           
            
            if artist in artist_count:
                artist_count[artist] += 1
            else:
                artist_count[artist] = 1

    
    sorted_songs = sorted(song_count.items(), key=lambda x: x[1], reverse=True)
    sorted_artists = sorted(artist_count.items(), key=lambda x: x[1], reverse=True)

    return sorted_songs, sorted_artists

def like_dislike_song(song, action):
    if action == 'like':
        with open(LIKES_FILE, 'a') as f:
            f.write(f"{song}\n")
    elif action == 'dislike':
        with open(DISLIKES_FILE, 'a') as f:
            f.write(f"{song}\n")

def view_likes():
    print("\nLiked Songs:")
    print("Song Name                     ")
    print("-" * 30)
    with open(LIKES_FILE, 'r') as f:
        for line in f:
            song = line[:-1]  
            print(f"{song:<30}")

def view_dislikes():
    print("\nDisliked Songs:")
    print("Song Name                     ")
    print("-" * 30)
    with open(DISLIKES_FILE, 'r') as f:
        for line in f:
            song = line[:-1]  
            print(f"{song:<30}")

def show_top_songs_and_artists():
    sorted_songs, sorted_artists = get_most_listened()


    print("\nTop Artists:")
    print("Artist Name                   Count")
    print("-" * 42)
    for artist, count in sorted_artists:
        print(f"{artist:<30} {count:<10}")

def main():
    initialize_files()

    while True:
        print("\n1. Add a song")
        print("2. Show top artists")
        print("3. Like a song")
        print("4. Dislike a song")
        print("5. View liked songs")
        print("6. View disliked songs")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            song = input("Enter song name: ")
            artist = input("Enter artist name: ")
            add_song(song, artist)
            print(f"Added '{song}' by {artist}.")

        elif choice == '2':
            show_top_songs_and_artists()

        elif choice == '3':
            song = input("Enter song name to like: ")
            like_dislike_song(song, 'like')
            print(f"You liked '{song}'.")

        elif choice == '4':
            song = input("Enter song name to dislike: ")
            like_dislike_song(song, 'dislike')
            print(f"You disliked '{song}'.")

        elif choice == '5':
            view_likes()

        elif choice == '6':
            view_dislikes()

        elif choice == '7':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
