# DevSecOps Demo Project - API Service

## 1. Deskripsi & Fungsi Aplikasi
Aplikasi backend REST API ringan berbasis Python Flask yang menangani endpoint dasar untuk health check dan otentikasi login mock-up pengguna.

## 2. Bahasa & Framework
- **Bahasa**: Python 3.11
- **Framework Web**: Flask 3.0.3
- **Testing Framework**: Pytest 8.2.2
- **SAST Scanner**: Semgrep OSS (Ruleset `p/ci` & `p/owasp-top-ten`)

## 3. Cara Menjalankan Aplikasi Lokal (macOS)
```bash
# Buat virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Jalankan Unit Test
pytest

# Jalankan server lokal
python -c "from app import create_app; create_app().run(port=5000)"