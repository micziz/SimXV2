# SimX!

---

- [SimX!](#simx)
  - [What is SimX?](#what-is-simx)
  - [Who is SimX developed by?](#who-is-simx-developed-by)
  - [Oh, can i contribute?](#oh-can-i-contribute)
  - [How do i download?](#how-do-i-download)
    - [Windows](#windows)
    - [MacOS](#macos)
    - [Linux](#linux)
  - [License](#license)

---

Welcome to the world of SimulationeXtreme! Work, buy (yet to be implemented), sell (yet to be implemented) and do much more all in your command line.

## What is SimX?

SimX, witch stands for SimulationeXtreme (i know, not really extreme but it's my game and i make the rules...) is a real-ish simulator of life. It's currently in very early stages of development, but you would help out a ton if you visited the project, and gave me a help with contributions...

## Who is SimX developed by?

By me! And also a lot of contributors.

## Oh, can i contribute?

Of course! Just check contributing.md and then you are ready!

## How do i download?

Currently only downloading from source is available, hers'e how you do it!

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

## License

This project is distributed under the MIT License! Learn more ate the License file!