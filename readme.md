# SimX!

---

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


---

- [SimX!](#simx)
  - [What is SimX?](#what-is-simx)
  - [WHY?](#why)
  - [Who is SimX developed by?](#who-is-simx-developed-by)
  - [Can i contribute?](#can-i-contribute)
  - [How do i download simx?](#how-do-i-download-simx)
  - [Is there a build available?](#is-there-a-build-available)
  - [So how do i build?](#so-how-do-i-build)
  - [Installation Instructions](#installation-instructions)
    - [Windows](#windows)
    - [MacOS](#macos)
    - [Linux](#linux)
  - [Compatibility.](#compatibility)
    - [Why?](#why-1)
  - [License](#license)
  - [List of contributors](#list-of-contributors)

---

Welcome to the world of SimulationeXtreme! Work, buy, sell and do much more all in your command line.

## What is SimX?

SimX, witch stands for SimulationeXtreme (i know, not really extreme but it's my game and i make the rules...) is a real-ish simulator of life. It's currently in very early stages of development, but you would help out a ton if you visited the project, and gave me a help with contributions...

## WHY?

I was board!!!!

## Who is SimX developed by?

By me! And also contributors. You can check the list at the end!

## Can i contribute?

Of course! Just check contributing.md, complete the checklist and then feel free to open a PR!

## How do i download simx?

If youre on MacOS youre in luck, since there is a build available. For every other platform you need to build from source.

## Is there a build available?

Yes! For MacOS only thougth.

## So how do i build?

Here are the install instructions

## Installation Instructions

### Windows

Download the latest release of python, at this time 3.10.2, using the exe that you can download [here](https://www.python.org/downloads/), or choclatey using this command 

```choco install python``` 

Then, download the latest zip, by going to releases, latest, zip and downloading it. Or if you prefer, 

```git clone https://github.com/micziz/SimX```

(**Note! the latest commit may have some unknown bugs that we do not know of, so please use at your own risk.**)

Then, go into the directory where you downloaded, then do:

```
cd src
python main.py
```

And enjoy!

### MacOS

**Note there is a build! Go to download the latest release!**

(for inpatient peapole, requires brew: 

```
brew install python@3.10 && git clone https://github.com/micziz/SimX && cd src && python3 main.py
```

)

Download the latest release of python, at this time 3.10.2, using the pkg that you can download [here](https://www.python.org/downloads/), or brew/MacPorts using this command 

```brew install python@3.10```
```sudo port install python310``` 

Then, download the latest zip, by going to releases, latest, zip and downloading it. Or if you prefer, 

```git clone https://github.com/micziz/SimX```

(**Note! the latest commit may have some unknown bugs that we do not know of, so please use at your own risk.**)

Then, go into the directory where you downloaded, then do:

```
cd src && python3 main.py
```

And enjoy!


### Linux

Download the latest release of python, at this time 3.10.2, using your system package manager.


Debian, ubuntu and based:
```
sudo apt-get python3.10
```

Fedora:

```
sudo dnf install python3
```

Arch and based:

```
sudo pacman install python39
```

(**Arch does not support python3.10!**)

Then, download the latest zip, by going to releases, latest, zip and downloading it. Or if you prefer, 

```git clone https://github.com/micziz/SimX```

(**Note! the latest commit may have some unknown bugs that we do not know of, so please use at your own risk.**)

Then, go into the directory where you downloaded, then do:

```
cd src && python main.py
```

or if not working:


```
cd src && python3 main.py
```

And enjoy!


---

## Compatibility.

The app was developed in python 3.10.2, the latest at this time. 

**Compatible**:

- Should be compatible with all version above 3.0, tested with python 3.8.9 and upwards, best used with python 3.10.2!

**Incompatible**:

- Python 1.0
- Python 2.0

### Why?

Python 3 breaks compatibility from python 2 a lot. Hers'e an [article](https://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).

As for python 1.0, it's just too plain old, and basically nothing works with this. Plus i cannot test it, as my computer is too new!

## License

This project is distributed under the MIT License! Learn more ate the [LISCENCE](LISCENCE) file!

## List of contributors

- micziz