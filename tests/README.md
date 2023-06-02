# Unit Tests

## Create a file for enviorment variables

First create a `.env` file here with

```ini
HOST=http://127.0.0.1:8002
TIMEOUT=10
```

## Running the tests

To run one test, for example `test_archivo.py`, run:

```bash
python -m unittest tests.test_archivo
```

To run all tests, run:

```bash
python -m unittest discover tests
```
