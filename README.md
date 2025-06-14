# 📄 Simple OCR - Text Extraction Tool

A powerful and easy-to-use OCR (Optical Character Recognition) tool that extracts text from a wide range of documents and image formats using Tesseract and PyMuPDF.

---

## ✨ Features

- 🧾 **Multi-format Support**: Works with PDFs, DOCX, TXT, JPG, PNG, HEIC, and more
- 🧠 **Smart Detection**: Automatically applies the correct method for each file type
- 📄 **PDF Dual Mode**: Extracts from both text-based and scanned/image-based PDFs
- 🌐 **Web Interface**: Streamlit-powered interactive UI
- 🔒 **Offline Ready**: No internet connection required
- 💡 **Free & Open Source**: Built using open-source technologies

---

## 🎯 Use Cases

- Digitize scanned documents or handwritten notes
- Convert receipts, invoices, and forms to text
- Extract text from screenshots or images
- Batch-process documents for text analytics

---

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- [Tesseract OCR](https://github.com/UB-Mannheim/tesseract/wiki)

### Install Python Dependencies

```bash
pip install -r requirements.txt
# or individually:
pip install PyMuPDF pytesseract Pillow python-docx streamlit pillow-heif
````

### Tesseract Installation

* **Windows**: [Download here](https://github.com/UB-Mannheim/tesseract/wiki)
* **macOS**: `brew install tesseract`
* **Linux**:

```bash
sudo apt update
sudo apt install tesseract-ocr
```

### Configure Tesseract Path

Edit line 10 in `extract_text.py`:

```python
# Windows:
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

## 🚀 Usage

### Launch Web App

```bash
streamlit run app.py
# or
python -m streamlit run app.py
```

Go to `http://localhost:8501` and upload your file.

### Programmatic Use

```python
from extract_text import extract_text

with open("document.pdf", "rb") as f:
    print(extract_text(f, "document.pdf"))
```

---

## 📁 Supported Formats

| Type        | Extensions                               |
| ----------- | ---------------------------------------- |
| Documents   | `.pdf`, `.docx`, `.txt`                  |
| Images      | `.png`, `.jpg`, `.jpeg`, `.bmp`, `.tiff` |
| HEIC Images | `.heic`                                  |

---

## 🌐 OCR Language Support

Change the OCR language:

```python
pytesseract.image_to_string(img, lang="eng+deu+fra")
```

Install additional Tesseract language packs as needed.

---

## 📦 Project Structure

```
simple_ocr/
├── app.py              # Web interface
├── extract_text.py     # Text extraction logic
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── .gitignore
```

---

## 🧠 How It Works

1. **Detects File Type** based on extension
2. **Applies Format-Specific Extraction**:

   * OCR for scanned PDFs/images
   * Direct read for DOCX, TXT
3. **Cleans Text** by removing unnecessary whitespace

---

## 🐞 Troubleshooting

* ❌ **"No module named 'fitz'"**
  → `pip install PyMuPDF`

* ❌ **"TesseractNotFoundError"**
  → Ensure correct path in `extract_text.py`

* ❌ **Streamlit not found**
  → `python -m streamlit run app.py`

* ⚠️ **Poor OCR accuracy**
  → Use high-quality images and try `--psm` or preprocessing

---

## 📋 Requirements

Main dependencies:

* `PyMuPDF==1.26.0`
* `pytesseract==0.3.13`
* `Pillow==11.2.1`
* `python-docx==1.1.2`
* `streamlit==1.45.1`
* `pillow-heif==0.22.0`

---

## 🤝 Contributing

1. Fork this repo
2. Create a feature branch
3. Submit a pull request

---

## 📜 License

MIT License — free to use and modify.

---

## 🙏 Acknowledgments

* [Tesseract OCR](https://github.com/tesseract-ocr/tesseract)
* [PyMuPDF](https://pymupdf.readthedocs.io/)
* [Streamlit](https://streamlit.io/)
* [Pillow](https://python-pillow.org/)

---

## 📧 Support

Open an issue with logs or detailed steps to reproduce if you encounter bugs.

```

---


```
