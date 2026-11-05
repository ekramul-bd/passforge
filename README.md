# PassForge 🔐

**PassForge** is a simple, secure, and lightweight command-line tool built with Python to generate strong passwords and check password strength.

It uses Python's standard library only. No external dependencies, no tracking — everything runs locally on your machine.

## ✨ Features

- 🔑 Generate strong random passwords with customizable length and character types.
- 📊 Check password strength (Weak / Fair / Strong / Very Strong).
- 🚫 Exclude ambiguous characters such as `l`, `1`, `I`, `O`, and `0` for easier typing.
- 🔒 Uses Python's `secrets` module for cryptographically secure randomness.
- 📁 Simple single-file design using `passforge.py`.
- 🧪 Includes automated tests with pytest.

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/ekramul-bd/passforge.git
cd passforge
```

Install the project:

```bash
pip install -e .
```

## 💻 Usage

### 🔑 Generate a Password

Generate a password with the default length of 16 characters:

```bash
passforge generate
```

Generate a 24-character password:

```bash
passforge generate --length 24
```

Generate a password without symbols:

```bash
passforge generate --no-symbols
```

Avoid ambiguous characters:

```bash
passforge generate --no-ambiguous
```

### 📊 Check Password Strength

Check the strength of a password:

```bash
passforge check "myP@ssw0rd123"
```

Example output:

```text
Strength: STRONG (score 75/100)
```

### ▶️ Run Without Installing

You can also run PassForge directly using Python:

```bash
python passforge.py generate
python passforge.py check "myP@ssw0rd123"
```

## 📈 How Password Strength Is Scored

PassForge evaluates passwords using a scoring system out of 100 points.

| Factor | Points |
|---|---:|
| Length (8+, 12+, 16+, 20+ characters) | Up to 40 |
| Lowercase and uppercase letters | 20 |
| Digits | 15 |
| Symbols | 15 |
| Length bonus (20+ characters) | 10 |

### Strength Levels

| Score | Strength |
|---|---|
| 0–40 | Weak |
| 41–60 | Fair |
| 61–80 | Strong |
| 81–100 | Very Strong |

## 🧪 Running Tests

PassForge includes automated tests to verify its functionality.

Run the test suite using:

```bash
python -m pytest test_passforge.py -v
```

## 📂 Project Structure

```text
passforge/
│
├── passforge.py
├── test_passforge.py
├── pyproject.toml
├── README.md
├── LICENSE
└── .gitignore
```

## 📄 License

**MIT License**

Copyright © 2026 **Ekramul Islam (ekramul-bd)**.

PassForge is open-source software licensed under the MIT License. You are free to use, copy, modify, merge, publish, distribute, sublicense, and sell copies of the software, subject to the terms and conditions of the MIT License.

The software is provided "AS IS", without warranty of any kind, express or implied.

For the complete license terms, please see the [LICENSE](LICENSE) file.

---

**Made with ❤️ by [ekramul-bd](https://github.com/ekramul-bd)**