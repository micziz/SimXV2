## Installation Instructions

- [Installation Instructions](#installation-instructions)
  - [Windows](#windows)
  - [MacOS](#macos)
  - [Linux](#linux)

### Windows

Ensure you have the latest version of Python3 installed. You can download Python3 [here](https://www.python.org/downloads/)

Then, download the latest release zip [here](https://github.com/micziz/SimXV2/releases), or alternatively: 

```git clone https://github.com/micziz/SimX```

(**Note! the latest commit may have some unknown bugs that we do not know of, so please use them at your own risk.**)

Then, go into the directory where you downloaded, and run:

```
pip install -r requirements.txt
cd src
python main.py
```

And enjoy!

### MacOS


(for impatient people, requires brew: 

```
brew install python@3.10 && git clone https://github.com/micziz/SimX && pip3 install -r requirements.txt && cd src && python3 main.py
```

)

Download the latest release of python, at this time 3.10.2, using the pkg that you can download [here](https://www.python.org/downloads/), or Brew/MacPorts using this command 

```brew install python@3.10```
```sudo port install python310``` 

Then, download the latest release zip [here](https://github.com/micziz/SimXV2/releases), or alternatively: 

```git clone https://github.com/micziz/SimX```

(**Note! the latest commit may have some unknown bugs that we do not know of, so please use them at your own risk.**)

Then, go into the directory where you downloaded, and do:

```
pip3 install -r requirements.txt && cd src && python3 main.py
```

And enjoy!


### Linux

Download the latest release of python, at this time 3.10.2, using your system package manager.


Debian, Ubuntu and debian-based:
```
sudo apt-get python3.10
```

Fedora:

```
sudo dnf install python3
```

Arch and Arch-based:

```
sudo pacman install python
```

Then, download the latest release zip [here](https://github.com/micziz/SimXV2/releases), or alternatively: 

```git clone https://github.com/micziz/SimX```

(**Note! the latest commit may have some unknown bugs that we do not know of, so please use them at your own risk.**)

Then, go into the directory where you downloaded, and do:

```
pip install -r requirements.txt && cd src && python main.py
```

or if not working:


```
pip3 install -r requirements.txt && cd src && python3 main.py
```

And enjoy!
