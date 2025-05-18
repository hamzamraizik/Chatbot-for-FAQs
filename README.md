# Computer Store FAQ Chatbot

This is a command-line chatbot that answers frequently asked questions (FAQs) about an e-commerce website selling computers. It uses Python, NLTK, and scikit-learn for natural language processing and question matching.

---

## Features
- Answers common questions about products, orders, shipping, returns, and more.
- Uses NLP to understand user questions and match them to the closest FAQ.

---

## Requirements
- Python 3.7 or higher
- pip (Python package manager)
- Internet connection (for first-time NLTK data download)

---

## Installation

1. **Clone or download this repository.**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download required NLTK data:**
   Open a Python shell and run:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   nltk.download('wordnet')
   ```
   If you encounter errors about missing resources (like `punkt_tab`), try:
   ```python
   nltk.download('all')
   ```

---

## Usage

Run the chatbot from your terminal:
```bash
python chatbot.py
```

Type your question and press Enter. Type `exit` or `quit` to stop the chatbot.

---

## Troubleshooting

### Fatal Python error: Failed to import encodings module
- This means your Python installation is broken. Try:
  - Unsetting environment variables:
    ```bash
    unset PYTHONHOME
    unset PYTHONPATH
    ```
  - Reinstalling Python:
    ```bash
    sudo dnf reinstall python3
    ```

### NLTK LookupError (missing resources)
- If you see errors about missing NLTK resources (e.g., `punkt`, `punkt_tab`):
  - Open a Python shell and run:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```
  - Or download all NLTK data:
    ```python
    nltk.download('all')
    ```

### Virtual Environment Issues
- If you are not in a virtual environment, you can ignore `deactivate` errors.
- If you are in a virtual environment, just type `deactivate` (no path).

---

## Customizing FAQs
- Edit `faq_data.json` to add, remove, or change questions and answers.

---

## Submitting Your Project
- Ensure your `requirements.txt`, `chatbot.py`, `faq_data.json`, and `README.md` are included.
- Test your project on a clean machine or virtual environment before submitting.

---

## Contact
For further help, see the [NLTK documentation](https://www.nltk.org/data.html) or contact your internship supervisor. 