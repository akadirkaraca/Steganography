# Steganography LSB
Steganography LSB is a technique that hides secret data by modifying the least significant bits (LSB) of an image, allowing data to be embedded without noticeable changes to the visual quality.

![Running on](https://img.shields.io/badge/running_on:-purple%20?style=for-the-badge)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## 📦 Installation
![C++](https://img.shields.io/badge/c++-%2300599C.svg?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Qt](https://img.shields.io/badge/Qt-%23217346.svg?style=for-the-badge&logo=Qt&logoColor=white)

```bash
python3 -m pip install -r requirements.txt
python3 main.py
```

## 🐳 Docker
_Build Docker Image_
```bash
docker build -t steganography .
```

_Run Docker Container For Windows_
```bash
docker run -e DISPLAY=host.docker.internal:0.0 -v C:/Users/$USER:/mnt/C steganography
```

_Run Docker Container For Ubuntu_
```bash
xhost +local:docker
docker run -e DISPLAY=$DISPLAY -e QT_X11_NO_MITSHM=1 -v /tmp/.X11-unix:/tmp/.X11-unix:rw -v /home/$(whoami):/home/$(whoami):rw steganography
```

---

> [!NOTE]
> To view the GUI on your OS, X11 forwarding must be configured.
>
> **X11 Forwarding on Windows** (Download: [VcXsrv](https://vcxsrv.com/)):
> 1. Start the XLaunch application.
> 2. Choose the '_Multiple windows_' selection.
> 3. Mark the '_Start no client_' selection.
> 4. Allow Firewall access by marking '_Disable Access Control_'.
> 5. Finally, press the '_Finish_' button to start the X Server.

## 🚧 Under Construction

- [x] Add Docker Usage
- [ ] Code Refactoring
- [ ] Add Build Instructions for C++ Version
- [ ] Add Build Instructions for Python Version