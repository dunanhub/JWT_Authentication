# 🔐 FastAPI JWT Authentication

## 📌 Описание

Задание 4 практики: реализация авторизации с использованием JWT токенов.  
Пользователь получает токен при успешном входе. Токен можно использовать для последующего доступа к защищённым маршрутам.

---

## 🚀 Технологии

- FastAPI
- Uvicorn
- PostgreSQL
- SQLModel
- Pydantic
- python-jose

---

## 🧩 Установка

```bash
git clone https://github.com/dunanhub/JWT_Authentication.git
cd JWT_Authentication
```

```bash
# Создание и активация виртуального окружения
python -m venv .venv
source .venv/bin/activate       # для Linux/macOS
.venv\Scripts\activate        # для Windows
```

```bash
# Установка зависимостей
pip install -r requirements.txt
```

---

## 🛠 Настройки

Создайте `.env` или переменные в конфиге:

```bash
DATABASE_URL=postgresql+asyncpg://postgres:your_password@localhost:5432/jwt_authentication
SECRET_KEY=your_secret_key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

---

## 📂 Структура проекта

```
JWT_Authentication/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   ├── routes.py
│   └── auth.py
├── .env
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 📡 Эндпоинты

- `POST /register` — регистрация пользователя
- `POST /login` — вход, получение JWT токена

---

## 🔐 JWT Генерация

Функция `create_access_token()` находится в `auth.py` и возвращает токен на основе username.

---

## 🧪 Тестирование (Postman)

1. `POST /register` с username и password → OK
2. `POST /login` → получить `access_token`
3. Проверить, что ответ содержит:

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIs...",
  "token_type": "bearer"
}
```

---

## 📄 Лицензия

Проект распространяется под лицензией MIT. Подробнее см. [LICENSE](./LICENSE).
