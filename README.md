Application for sorting feedbacks to 3 categories: **positive**, **negative** and **neutral**

## Installation
```bash
pip install flask==3.1.1
python app.py
```

## Example

### POST /reviews/

#### Request - neutral
```bash
curl --location 'http://127.0.0.1:5555/reviews' \
--header 'Content-Type: application/json' \
--data '{
    "text": "segtseg"
}'
```
#### Response - neutral
```bash
{
    "created_at": "2025-07-08T17:02:59.005593",
    "id": 6,
    "sentiment": "neutral",
    "text": "segtseg"
}
```

#### Request - positive
```bash
curl --location 'http://127.0.0.1:5555/reviews' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Хороший сервис"
}'
```
#### Response - positive
```bash
{
    "created_at": "2025-07-08T17:03:45.323873",
    "id": 8,
    "sentiment": "positive",
    "text": "Хороший сервис"
}
```

#### Request - negative
```bash
curl --location 'http://127.0.0.1:5555/reviews' \
--header 'Content-Type: application/json' \
--data '{
    "text": "Плохой сервис"
}'
```
#### Response - negative
```bash
{
    "created_at": "2025-07-08T17:04:17.807016",
    "id": 9,
    "sentiment": "negative",
    "text": "Плохой сервис"
}
```

### GET /reviews/

#### Request - all
```bash
curl http://localhost:5555/reviews
```

### Response - all
```bash
[
    {
        "created_at": "2025-07-08T17:02:59.005593",
        "id": 6,
        "sentiment": "neutral",
        "text": "segtseg"
    },
    {
        "created_at": "2025-07-08T17:03:45.323873",
        "id": 8,
        "sentiment": "positive",
        "text": "Хороший сервис"
    },
    {
        "created_at": "2025-07-08T17:04:17.807016",
        "id": 9,
        "sentiment": "negative",
        "text": "Плохой сервис"
    }
]
```

#### Request - positive
```bash
curl http://localhost:5555/reviews?sentiment=positive
```

### Response - positive
```bash
[
    {
        "created_at": "2025-07-08T17:03:45.323873",
        "id": 8,
        "sentiment": "positive",
        "text": "Хороший сервис"
    }
]
```

#### Request - negative
```bash
curl http://localhost:5555/reviews?sentiment=negative
```

### Response - negative
```bash
[
    {
        "created_at": "2025-07-08T17:04:17.807016",
        "id": 9,
        "sentiment": "negative",
        "text": "Плохой сервис"
    }
]
```

#### Request - neutral
```bash
curl http://localhost:5555/reviews?sentiment=negative
```

### Response - neutral
```bash
[
    {
        "created_at": "2025-07-08T17:02:59.005593",
        "id": 6,
        "sentiment": "neutral",
        "text": "segtseg"
    }
]
```
