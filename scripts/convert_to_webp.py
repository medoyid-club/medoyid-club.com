from PIL import Image
import os

source_folder = r'D:\work\medoyid-club\temp_media\foto_repo'
target_folder = r'D:\work\medoyid-club\temp_media\members_image'

os.makedirs(target_folder, exist_ok=True)

input_extensions = ('.jpg', '.jpeg', '.png')

for filename in os.listdir(source_folder):
    if filename.lower().endswith(input_extensions):
        input_path = os.path.join(source_folder, filename)
        base_name = os.path.splitext(filename)[0]
        output_path = os.path.join(target_folder, base_name + '.webp')

        # Пропускаем, если файл уже существует
        if os.path.exists(output_path):
            print(f"⏭ Уже конвертирован: {filename}")
            continue

        try:
            img = Image.open(input_path).convert("RGB")
            img.save(output_path, format='WEBP', quality=80, method=6)
            print(f"✓ Конвертирован: {filename} → {base_name}.webp")
        except Exception as e:
            print(f"❌ Ошибка с файлом {filename}: {e}")