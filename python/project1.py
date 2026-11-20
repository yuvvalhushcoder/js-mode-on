"""
AI Recommendation Logic (Project 3)
Matches a user's interests against item attributes using Jaccard similarity.

Similarity = (shared tags) / (all distinct tags across both sets)
A score of 100% means the item's tags and the user's interests are identical.
"""

# ---- 1. Item catalogue: each movie has a set of descriptive tags ----
MOVIES = {
    "Inception":            {"sci-fi", "thriller", "action", "mind-bending"},
    "The Dark Knight":      {"action", "crime", "thriller", "superhero"},
    "Interstellar":         {"sci-fi", "drama", "space", "mind-bending"},
    "The Matrix":           {"sci-fi", "action", "mind-bending"},
    "Avengers: Endgame":    {"action", "superhero", "sci-fi", "adventure"},
    "The Notebook":         {"romance", "drama"},
    "La La Land":           {"romance", "musical", "drama"},
    "Superbad":             {"comedy", "teen"},
    "The Hangover":         {"comedy", "adventure"},
    "Get Out":              {"horror", "thriller", "mystery"},
    "A Quiet Place":        {"horror", "thriller", "sci-fi"},
    "Knives Out":           {"mystery", "comedy", "crime"},
    "Spirited Away":        {"animation", "fantasy", "adventure"},
    "Toy Story":            {"animation", "comedy", "adventure"},
    "3 Idiots":             {"comedy", "drama", "teen"},
    "Dangal":               {"drama", "sports", "biography"},
}


def all_interests(catalogue):
    """Collect every unique tag so we can show the user their options."""
    tags = set()
    for item_tags in catalogue.values():
        tags |= item_tags
    return sorted(tags)


def similarity(user_interests, item_tags):
    """Jaccard similarity between two sets, returned as a percentage."""
    union = user_interests | item_tags
    if not union:
        return 0.0
    return len(user_interests & item_tags) / len(union) * 100


def recommend(user_interests, catalogue, top_n=5):
    """Score every item and return the best matches (score > 0 only)."""
    results = []
    for title, tags in catalogue.items():
        score = similarity(user_interests, tags)
        if score > 0:
            matched = sorted(user_interests & tags)
            results.append((title, score, matched))
    # Highest score first; ties broken alphabetically for stable output
    results.sort(key=lambda r: (-r[1], r[0]))
    return results[:top_n]


def get_user_interests(valid_tags):
    """Ask for comma-separated interests and keep only valid ones."""
    print("Available interests:")
    print("  " + ", ".join(valid_tags))
    while True:
        raw = input("\nEnter your interests (comma-separated): ")
        chosen = {t.strip().lower() for t in raw.split(",") if t.strip()}
        valid = chosen & set(valid_tags)
        unknown = chosen - set(valid_tags)
        if unknown:
            print(f"Ignored unknown interests: {', '.join(sorted(unknown))}")
        if valid:
            return valid
        print("Please enter at least one valid interest.")


def main():
    print("=== Movie Recommendation Engine ===\n")
    interests = get_user_interests(all_interests(MOVIES))
    recs = recommend(interests, MOVIES)

    print(f"\nYour interests: {', '.join(sorted(interests))}")
    print("\nTop recommendations for you:")
    print("-" * 50)
    for rank, (title, score, matched) in enumerate(recs, start=1):
        print(f"{rank}. {title}  ({score:.0f}% match)")
        print(f"   Matched on: {', '.join(matched)}")


if __name__ == "__main__":
    main()