---
title: "Демонстрація UI компонентів"
date: 2025-01-05T15:00:00+02:00
draft: false
tags: ["ui", "дизайн", "компоненти"]
categories: ["технології"]
author: "Медоїди"
description: "Демонстрація кастомних UI компонентів сайту"
slug: "ui-demo"
---

<div class="animated-header">

# Демонстрація UI компонентів

</div>

<span class="pulse-indicator"></span>**Новий функціонал** — На цій сторінці ви можете побачити всі доступні кастомні UI компоненти.

## 📊 Карточки (Cards)

{{< card title="🎯 Інформаційна карточка" color="blue" content="Це базова карточка з інформацією. Вона підтримує markdown форматування та має **красиві анімації**." >}}

{{< card title="✅ Карточка успіху" color="green" content="Використовуйте зелену карточку для позитивної інформації, успіхів та досягнень." >}}

{{< card title="⚠️ Попередження" color="red" content="Червона карточка привертає увагу до важливої інформації або попереджень." >}}

{{< card title="🔮 Креативна карточка" color="purple" content="Фіолетова карточка ідеально підходить для творчих проектів та ідей." >}}

## 🔘 Кнопки (Buttons)

{{< button text="Базова кнопка" url="#" style="default" >}}
{{< button text="Успіх" url="#" style="success" icon="✅" >}}
{{< button text="Попередження" url="#" style="warning" icon="⚠️" >}}
{{< button text="Небезпека" url="#" style="danger" icon="❌" >}}
{{< button text="Темна тема" url="#" style="dark" icon="🌙" >}}

### Кнопки з анімацією завантаження

{{< loading-button text="Завантажити файл" loading_text="Завантаження..." style="primary" size="medium" >}}
{{< loading-button text="Зберегти" loading_text="Збереження..." style="success" size="small" >}}
{{< loading-button text="Видалити" loading_text="Видалення..." style="danger" size="large" >}}
{{< loading-button text="Оновити" loading_text="Оновлення..." style="warning" size="medium" >}}
{{< loading-button text="Експорт" loading_text="Експорт..." style="dark" size="small" >}}

## 📈 Прогрес-бари (Progress Bars)

{{< progress value="30" label="Розробка функціоналу" color="blue" >}}
{{< progress value="75" label="Дизайн сайту" color="green" >}}
{{< progress value="90" label="Контент" color="orange" >}}
{{< progress value="50" label="Тестування" color="red" >}}

## 🔄 Переключатели (Toggle Switches)

{{< toggle label="Темна тема" color="blue" size="medium" >}}
{{< toggle label="Сповіщення" color="green" size="small" checked="true" >}}
{{< toggle label="Автозбереження" color="purple" size="large" >}}
{{< toggle label="Режим розробника" color="red" size="medium" >}}
{{< toggle label="Синхронізація" color="orange" size="small" checked="true" >}}
{{< toggle color="dark" size="medium" >}}

## 🏗️ Адаптивні сітки (Grid System)

### Сітка карточок (3 колонки)
{{< grid columns="3" gap="20" style="cards" >}}

{{< grid-item title="Новини технологій" 
            image="https://via.placeholder.com/400x225/667eea/ffffff?text=Tech" 
            category="Технології" 
            date="5 січня 2025" 
            author="Медоїди" 
            excerpt="Останні новини зі світу технологій та інновацій." />}}

{{< grid-item title="Дизайн майбутнього" 
            category="Дизайн" 
            date="4 січня 2025" 
            author="Медоїди" 
            size="large" >}}
Як буде виглядати дизайн веб-сайтів у 2025 році? Тренди, які змінять індустрію.
{{< /grid-item >}}

{{< grid-item title="UI/UX тренди" 
            image="https://via.placeholder.com/400x225/56ab2f/ffffff?text=UX" 
            category="UX" 
            date="3 січня 2025" 
            author="Медоїди" 
            excerpt="Головні тренди в дизайні користувацьких інтерфейсів." />}}

{{< /grid >}}

## 🚨 Сповіщення (Alerts)

{{< alert type="info" title="Інформація" >}}
Це інформаційне сповіщення з важливою інформацією для користувачів.
{{< /alert >}}

{{< alert type="success" title="Успіх!" >}}
Операція виконана успішно! Всі дані збережено.
{{< /alert >}}

{{< alert type="warning" title="Увага!" >}}
Будь ласка, перевірте введені дані перед продовженням.
{{< /alert >}}

{{< alert type="danger" title="Помилка!" >}}
Сталася помилка. Спробуйте ще раз або зверніться до підтримки.
{{< /alert >}}

## 🎨 Додаткові стилі

### Анімований заголовок
<div class="animated-header">
<h3>Цей заголовок має анімований градієнт</h3>
</div>

### Кастомна цитата
<div class="custom-quote">
Красиві UI компоненти роблять сайт більш привабливим та зручним для користувачів. Вони покращують користувацький досвід та створюють позитивне враження.
</div>

### Анімовані теги
<div>
<a href="#" class="animated-tag">Дизайн</a>
<a href="#" class="animated-tag">UI/UX</a>
<a href="#" class="animated-tag">Веб-розробка</a>
<a href="#" class="animated-tag">Hugo</a>
<a href="#" class="animated-tag">CSS</a>
</div>

## 🔧 Як використовувати

### Карточки
```markdown
{{</* card title="Заголовок" color="blue" content="Ваш контент тут" */>}}
```

### Кнопки
```markdown
{{</* button text="Текст кнопки" url="https://example.com" style="success" icon="✅" */>}}
```

### Кнопки завантаження
```markdown
{{</* loading-button text="Завантажити" loading_text="Завантаження..." style="primary" size="medium" */>}}
```

### Прогрес-бари
```markdown
{{</* progress value="75" label="Назва прогресу" color="green" */>}}
```

### Переключатели
```markdown
{{</* toggle label="Назва" color="blue" size="medium" checked="true" */>}}
```

### Адаптивні сітки
```markdown
{{</* grid columns="3" gap="20" style="cards" */>}}
  {{</* grid-item title="Заголовок" image="image.jpg" category="Категорія" */>}}
  Контент тут
  {{</* /grid-item */>}}
{{</* /grid */>}}
```

### Сповіщення
```markdown
{{</* alert type="info" title="Заголовок" */>}}
Ваш контент тут
{{</* /alert */>}}
```

## 📚 Параметри

### Карточки
- `title` - заголовок карточки
- `color` - колір (blue, green, red, purple, orange, dark)
- `content` - вміст карточки (підтримує markdown)

### Кнопки
- `text` - текст кнопки
- `url` - посилання
- `style` - стиль (default, success, danger, warning, dark)
- `icon` - іконка (емодзі)

### Кнопки завантаження
- `text` - текст кнопки
- `loading_text` - текст під час завантаження
- `style` - стиль (primary, success, danger, warning, dark)
- `size` - розмір (small, medium, large)
- `id` - унікальний ідентифікатор

### Прогрес-бари
- `value` - значення прогресу (10, 20, 30, ..., 100)
- `label` - назва прогресу
- `color` - колір (blue, green, red, orange)

### Переключатели
- `label` - підпис переключателя
- `color` - колір (blue, green, red, purple, orange, dark)
- `size` - розмір (small, medium, large)
- `checked` - початковий стан (true/false)
- `id` - унікальний ідентифікатор

### Адаптивні сітки
**Параметри сітки:**
- `columns` - кількість колонок (1-6, auto)
- `gap` - відстань між елементами (10, 15, 20, 25, 30, 40)
- `style` - стиль сітки (cards, minimal, modern)

**Параметри елементів:**
- `title` - заголовок
- `image` - зображення
- `category` - категорія
- `date` - дата
- `author` - автор
- `url` - посилання
- `excerpt` - короткий опис
- `size` - розмір (normal, small, large, wide, tall)

### Сповіщення
- `type` - тип (info, success, warning, danger)
- `title` - заголовок сповіщення

---

*Всі компоненти адаптовані для світлої та темної тем* 