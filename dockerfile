FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    x11-apps \
    libx11-6 \
    libxcb-cursor0 \
    libxcb-shape0 \
    libgl1-mesa-glx \
    libxcb-icccm4 \
    libxcb-image0 \
    libxcb-keysyms1 \
    libxcb-render-util0 \
    libxcb-xinerama0 \
    libxcb-xkb1 \
    libxkbcommon-x11-0 \
    libxkbcommon0 \
    libegl1 \
    libgl1-mesa-dev \
    libglib2.0-0 \
    libdbus-1-3 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

COPY python/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY python/ .

CMD ["python", "main.py"]
