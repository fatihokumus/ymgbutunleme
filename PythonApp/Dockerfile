FROM python:3.9-slim

# Gerekli paketleri yükleyin
RUN pip install --no-cache-dir flask flask-cors

# Uygulama dosyalarını kopyalayın
COPY app.py /app/app.py

# Çalışma dizinine geçin
WORKDIR /app

# Uygulama portunu açın
EXPOSE 5000

# Flask uygulamasını çalıştırın
CMD ["python", "app.py"]