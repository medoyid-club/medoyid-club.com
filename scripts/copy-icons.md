# Инструкция по использованию скрипта copy-icons.ps1

Скрипт предназначен для поиска и копирования SVG-иконок из репозитория Tabler Icons (filled/outline) в папку static/icons вашего Hugo-проекта по ключевым словам.

## Запуск

Откройте PowerShell в папке `medoyid-club` и выполните:

```
pwsh scripts/copy-icons.ps1 -Keywords "home,news,video" -Style outline -Exact:$false -Limit 2
```

## Аргументы
- `-Keywords` — список ключевых слов (можно строкой через запятую или массивом через пробел)
- `-Style` — стиль иконок: outline, filled, all (по умолчанию all)
- `-Exact` — точное совпадение имени файла (true/false, по умолчанию false)
- `-Limit` — максимальное количество файлов на ключ (0 — без лимита)

## Примеры

**Искать по всем стилям, нестрого, без лимита:**
```
pwsh scripts/copy-icons.ps1 -Keywords home news video
```
или
```
pwsh scripts/copy-icons.ps1 -Keywords "home,news,video"
```

**Только outline, только точные совпадения, по одному на ключ:**
```
pwsh scripts/copy-icons.ps1 -Keywords "home,news,video" -Style outline -Exact:$true -Limit 1
```

## Примечания
- Скрипт ищет иконки рекурсивно в подпапках filled и outline.
- Если не найдено ни одной иконки по ключу, будет выведено предупреждение.
- Можно использовать для массовой замены эмодзи на SVG-иконки. 