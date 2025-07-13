import os
import shutil

social_media_map = {
    "YouTube": "youtube",
    "Telegram": "telegram",
    "Facebook": "facebook",
    "Patreon": "patreon",
    "Instagram": "instagram",
    "TikTok": "tiktok",
    "threads": "threads",
    "LinkedIn": "linkedin"
}

source_icon_dir = "D:/work/medoyid-club/temp_media/tabler-icons-main/icons/outline"
dest_icon_dir = "D:/work/medoyid-club/layouts/partials/icons"

# Create destination directory if it doesn't exist
os.makedirs(dest_icon_dir, exist_ok=True)

for social_key, icon_name_suffix in social_media_map.items():
    icon_filename = f"brand-{icon_name_suffix}.svg"
    source_path = os.path.join(source_icon_dir, icon_filename)
    dest_path = os.path.join(dest_icon_dir, icon_filename)

    if os.path.exists(source_path):
        try:
            shutil.copy2(source_path, dest_path)
            print(f"Successfully copied {icon_filename} to {dest_icon_dir}")
        except Exception as e:
            print(f"Error copying {icon_filename}: {e}")
    else:
        print(f"Icon {icon_filename} not found in {source_icon_dir}")

print("Icon copying process completed.")