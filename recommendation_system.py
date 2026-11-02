import difflib

MOVIES = [
    {"title": "The Shawshank Redemption", "genres": ["drama"], "description": "Hope friendship prison drama"},
    {"title": "The Dark Knight", "genres": ["action", "crime", "drama"], "description": "Batman superhero crime thriller"},
    {"title": "Inception", "genres": ["sci-fi", "action", "thriller"], "description": "Dreams mind-bending science fiction"},
    {"title": "Interstellar", "genres": ["sci-fi", "drama", "adventure"], "description": "Space exploration family science fiction"},
    {"title": "The Avengers", "genres": ["action", "sci-fi", "adventure"], "description": "Superheroes team action adventure"},
    {"title": "Toy Story", "genres": ["animation", "comedy", "family"], "description": "Animated toys friendship family"},
    {"title": "Finding Nemo", "genres": ["animation", "adventure", "family"], "description": "Animated ocean fish adventure"},
    {"title": "The Hangover", "genres": ["comedy"], "description": "Funny friends chaotic comedy"},
    {"title": "The Conjuring", "genres": ["horror", "thriller"], "description": "Haunted house supernatural horror"},
    {"title": "Get Out", "genres": ["horror", "thriller", "mystery"], "description": "Psychological horror mystery suspense"},
    {"title": "Pride and Prejudice", "genres": ["romance", "drama"], "description": "Romantic period drama relationships"},
    {"title": "La La Land", "genres": ["romance", "drama", "music"], "description": "Musical romance dreams jazz"},
    {"title": "The Martian", "genres": ["sci-fi", "adventure", "comedy"], "description": "Mars survival space science humor"},
    {"title": "Knives Out", "genres": ["mystery", "comedy", "crime"], "description": "Detective murder mystery investigation"},
    {"title": "Jumanji: Welcome to the Jungle", "genres": ["adventure", "comedy", "action"], "description": "Game jungle adventure humor"}
]

def normalize(text):
    return text.lower().strip()

def recommend_movies(preferences, watched, limit=5):
    preferences = [normalize(item) for item in preferences]
    watched = {normalize(item) for item in watched}
    scored = []

    for movie in MOVIES:
        if normalize(movie["title"]) in watched:
            continue

        genres = set(movie["genres"])
        matched_genres = genres.intersection(preferences)
        genre_score = len(matched_genres) / max(len(preferences), 1)

        preference_text = " ".join(preferences)
        description_score = difflib.SequenceMatcher(
            None, preference_text, movie["description"].lower()
        ).ratio()

        score = genre_score * 0.85 + description_score * 0.15

        if matched_genres:
            scored.append((score, movie, matched_genres))

    scored.sort(key=lambda item: item[0], reverse=True)
    return scored[:limit]

def show_movies():
    print("\nAvailable movie genres:")
    genres = sorted({genre for movie in MOVIES for genre in movie["genres"]})
    print(", ".join(genres))

    print("\nMovies in the dataset:")
    for movie in MOVIES:
        print(f"- {movie['title']} ({', '.join(movie['genres'])})")

def main():
    print("=" * 48)
    print("MOVIE RECOMMENDATION SYSTEM")
    print("Content-based recommendation")
    print("=" * 48)

    show_movies()

    raw_preferences = input(
        "\nEnter genres you like, separated by commas: "
    ).strip()

    preferences = [item.strip() for item in raw_preferences.split(",") if item.strip()]
    available_genres = {genre for movie in MOVIES for genre in movie["genres"]}
    preferences = [genre for genre in preferences if genre.lower() in available_genres]

    if not preferences:
        print("No matching genres found. Please run the program again and enter listed genres.")
        return

    raw_watched = input(
        "Enter movies you have already watched (comma-separated), or press Enter: "
    ).strip()
    watched = [item.strip() for item in raw_watched.split(",") if item.strip()]

    try:
        limit = int(input("How many recommendations do you want? (1-10): ").strip())
        limit = max(1, min(limit, 10))
    except ValueError:
        limit = 5

    recommendations = recommend_movies(preferences, watched, limit)

    print("\nRecommended movies for you:")
    if not recommendations:
        print("No recommendations found. Try different genres.")
        return

    for rank, (score, movie, matched_genres) in enumerate(recommendations, start=1):
        print(f"{rank}. {movie['title']}")
        print(f"   Genres: {', '.join(movie['genres'])}")
        print(f"   Match: {', '.join(sorted(matched_genres))}")
        print(f"   Recommendation score: {score * 100:.1f}%")

if __name__ == "__main__":
    main()
