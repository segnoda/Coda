![icon](https://github.com/segnoda/Coda/raw/master/resources/icon/coda.png)

# Coda

**Coda** is a simple, cross-platform, and open source **visual novel game engine** using PyQt5.

## Getting Started

Everyone can create your own visual novel games using **Coda** by simply writing XML scripts and importing your resources. Your creation is good to go!

### Requirements

* [Python 3.5](https://www.python.org/downloads/)
* [Qt 5.6 Libraries](http://www.qt.io/download/)
* [SIP 4.18](https://riverbankcomputing.com/software/sip/download)
* [PyQt 5.6](https://riverbankcomputing.com/software/pyqt/download5)

### Installation

First, clone the repo to any target directory.

```
$ git clone git@github.com:segnoda/Coda.git
```

Run the shell script to build resources files.

```
$ ./pyrcc.sh
```

### Usage

Just run main.py to execute **Coda** with example resources.

```
$ python3 main.py
```

## Documentation

The guideline below allows you to control and modify your game flow.

### Basic Script Layout

```xml
<script>
    <content id="0">
    ...
    </content>
    <content id="1">
    ...
    </content>
    ...
</script>
```
