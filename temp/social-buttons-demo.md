---
title: "Демо: Плоские соціальні кнопки з логотипами"
date: 2024-01-15T12:00:00+02:00
draft: false
tags: ["ui", "demo", "social", "buttons", "flat"]
categories: ["Статті"]
description: "Демонстрація плоских соціальних кнопок з користувацькими SVG логотипами"
---

# Плоские соціальні кнопки з логотипами

Оновлена версія соціальних кнопок з плоским дизайном та підтримкою користувацьких SVG логотипів.

## Основні особливості

- **Плоский дизайн** без 3D ефектів
- **Користувацькі логотипи** для YouTube, Telegram, Patreon
- **Простий shimmer ефект** при наведенні
- **Адаптивні розміри** для всіх пристроїв
- **Брендові кольори** при hover

## Демонстрація

### З користувацькими логотипами
{{< social-buttons platforms="youtube,telegram,patreon" size="medium" >}}

### Змішаний набір (іконки + логотипи)
{{< social-buttons platforms="facebook,telegram,youtube,twitter,instagram" size="medium" >}}

### Великі кнопки
{{< social-buttons platforms="youtube,telegram,patreon" size="large" columns="3" >}}

### Малі кнопки
{{< social-buttons platforms="facebook,telegram,youtube,twitter,instagram,patreon" size="small" >}}

### Повний набір
{{< social-buttons platforms="facebook,telegram,youtube,twitter,instagram,linkedin,tiktok,discord,spotify,whatsapp,patreon" size="medium" >}}

## Параметри використання

### Базове використання
```markdown
{{< social-buttons >}}
```

### З вибором платформ
```markdown
{{< social-buttons platforms="youtube,telegram,patreon" >}}
```

### З налаштуванням розміру
```markdown
{{< social-buttons platforms="youtube,telegram" size="large" >}}
```

### З фіксованою кількістю колонок
```markdown
{{< social-buttons platforms="youtube,telegram,patreon" columns="3" >}}
```

## Доступні платформи

| Платформа | Тип | Колір | Примітка |
|-----------|-----|-------|----------|
| Facebook | FontAwesome | #1877f2 | Іконка |
| Telegram | SVG логотип | #0088cc | Користувацький |
| YouTube | SVG логотип | #ff0000 | Користувацький |
| Twitter | FontAwesome | #1da1f2 | Іконка |
| Instagram | FontAwesome | #e4405f | Іконка |
| LinkedIn | FontAwesome | #0077b5 | Іконка |
| TikTok | FontAwesome | #000000 | Іконка |
| Discord | FontAwesome | #5865f2 | Іконка |
| Spotify | FontAwesome | #1db954 | Іконка |
| WhatsApp | FontAwesome | #25d366 | Іконка |
| Patreon | SVG логотип | #ff424d | Користувацький |

## Розміри кнопок

- **small**: 50x50px - тільки іконки/логотипи
- **medium**: 70x70px - іконки/логотипи (рекомендовано)
- **large**: 90x90px - великі іконки/логотипи

## Додавання власних логотипів

Щоб додати власний логотип:

1. Помістіть SVG файл у папку `static/images/social/`
2. Додайте платформу в shortcode з параметром `customLogo`
3. Логотип автоматично стане білим на темному фоні

### Приклад структури:
```
static/
  images/
    social/
      telegram.svg
      Youtube.svg
      patreon.svg
```

## Стилі

- **Фон**: Темно-сірий (#1a1a1a)
- **Границя**: Сіра (#333)
- **Hover**: Змінюється на брендовий колір
- **Логотипи**: Автоматично стають білими
- **Анімація**: Плавне масштабування та shimmer

## Адаптивність

- **Десктоп**: Повний розмір кнопок
- **Планшет**: Зменшені відступи
- **Мобільний**: Компактні розміри

Всі ефекти оптимізовані для швидкості та працюють плавно на всіх пристроях. 