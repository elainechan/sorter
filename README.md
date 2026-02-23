# Package Sorter

Sorts packages into **STANDARD**, **SPECIAL**, or **REJECTED** based on dimensions and mass.

## Rules
- **Bulky**: volume ≥ 1,000,000 cm^3 or any dimension >= 150 cm
- **Heavy**: mass >= 20 kg
- **STANDARD**: neither bulky nor heavy
- **SPECIAL**: bulky or heavy (not both)
- **REJECTED**: both bulky and heavy

## Tech Stack
- **Python** - main language
- **FastAPI** - REST API
- **Pydantic** - request validation
- **Pytest** - test coverage

## Install
```bash
pip install -r requirements.txt
```

## Run
```bash
fastapi dev main.py
```

Interact with OpenAPI UI at `http://localhost:8000/docs`

Example Request in Command Line
```bash
curl -X 'POST' \
  'http://localhost:8000/sort' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "length": 1,
  "width": 1,
  "height": 1,
  "mass": 1
}'
```

## Test

```bash
pytest tests.py -v
```
