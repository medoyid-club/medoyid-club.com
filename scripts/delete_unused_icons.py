import os

files_to_delete = [
    "activity-heartbeat.svg", "address-book-off.svg", "adjustments-heart.svg",
    "adjustments-question.svg", "adjustments-star.svg", "arrow-roundabout-left.svg",
    "arrow-roundabout-right.svg", "article-off.svg", "basket-question.svg",
    "basket-star.svg", "bookmark-ai.svg", "bookmark-edit.svg", "books-off.svg",
    "brand-apple-news.svg", "brand-google-home.svg", "brand-steam.svg",
    "brand-teams.svg", "brand-youtube-kids.svg", "crown-off.svg", "crown.svg",
    "diamond-off.svg", "help-circle.svg", "help-hexagon.svg", "home-2.svg",
    "home-bitcoin.svg", "home-bolt.svg", "home-cancel.svg", "home-check.svg",
    "home-cog.svg", "home-dollar.svg", "home-dot.svg", "home-down.svg",
    "home-eco.svg", "home-edit.svg", "home-exclamation.svg", "home-hand.svg",
    "home-heart.svg", "home-infinity.svg", "home-link.svg", "home-minus.svg",
    "home-move.svg", "home-off.svg", "home-plus.svg", "home-question.svg",
    "home-ribbon.svg", "home-search.svg", "home-share.svg", "home-shield.svg",
    "home-signal.svg", "home-spark.svg", "home-star.svg", "home-stats.svg",
    "home-up.svg", "home-x.svg", "home.svg", "info-circle.svg",
    "library-minus.svg", "library-photo.svg", "news-off.svg",
    "physotherapist.svg", "premium-rights.svg", "smart-home-off.svg",
    "smart-home.svg", "thumb-down-off.svg", "thumb-down.svg", "users-minus.svg",
    "video-minus.svg"
]

icons_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'static', 'icons')

for filename in files_to_delete:
    file_path = os.path.join(icons_dir, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted: {filename}")
    else:
        print(f"Not found: {filename}")

print("\nCleanup complete.")
