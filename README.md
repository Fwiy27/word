# keyboard

Fun Word Library

Library Name: word

## Functions

```
w = word.Word(words_file_location: str)
```

| function (with word object) | description                                           | args            |
| --------------------------- | ----------------------------------------------------- | --------------- |
| `reset_words()`             | Reset Words Used                                      | `None`          |
| `reset_letters()`           | Resets Letters Used                                   | `None`          |
| `get_word()`                | Returns random word with syllable in it               | syllable[`str`] |
| `get_best_word()`           | Returns word that uses most letters not already used  | syllable[`str`] |
| `choose_word()`             | Removes word from words list and updates letters used | word[`str]      |

## Build

### Manually

1. Create Virtual Environement

```
python -m venv venv
```

2. Activate Virtual Environment

```
source ./venv/bin/activate
```

3. Update wheel and setuptools

```
pip install -U wheel setuptools
```

4. Build kbd

```
python -m setup bdist_wheel
```

5. Remove unnecessary files

```
rm -rf word.egg-info;rm -rf build;
```

6. Use wheel

- Built Wheel will be in dist/word\*.whl

### Makefile

1. Run make build

```
make build
```

2. Use wheel

- Built Wheel will be in dist/word\*.whl
