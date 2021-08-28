[![Python 3.9](https://github.com/addshlab/gnow/actions/workflows/python39.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python39.yml)
[![Python 3.8](https://github.com/addshlab/gnow/actions/workflows/python38.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python38.yml)
[![Python 3.7](https://github.com/addshlab/gnow/actions/workflows/python37.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python37.yml)
[![Python 3.6](https://github.com/addshlab/gnow/actions/workflows/python36.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python36.yml)
[![Python 3.5](https://github.com/addshlab/gnow/actions/workflows/python35.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python35.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# gnow

This is a wrapper command to make git add/commit/push and tagging easier.

## Installation

```
$ pip install gnow
```

## Usage

### git add -> git commit -> git push

```
$ gnow
```

### git commit

```
# Auto input (Make the commit message the status of the file)
$ gnow -c

# Manual input
$ gnow -c 'YOUR COMMIT MESSAGE'
```

### Tagging

```
# Auto input (Automatically increments the patch version)
$ gnow -t

# Manual input
$ gnow -t X.Y.Z
```

### Status

```
$ gnow -s
```


## Changelog

* 2021-07-09 Start porting to Python
* 2020-07-09 Published a bash script version on Github
