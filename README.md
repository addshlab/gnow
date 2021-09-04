[![Python 3.9](https://github.com/addshlab/gnow/actions/workflows/python39.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python39.yml)
[![Python 3.8](https://github.com/addshlab/gnow/actions/workflows/python38.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python38.yml)
[![Python 3.7](https://github.com/addshlab/gnow/actions/workflows/python37.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python37.yml)
[![Python 3.6](https://github.com/addshlab/gnow/actions/workflows/python36.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python36.yml)
[![Python 3.5](https://github.com/addshlab/gnow/actions/workflows/python35.yml/badge.svg)](https://github.com/addshlab/gnow/actions/workflows/python35.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# gnow

A wrapper command to make git add/commit/push and tagging easier.

## Installation

```
$ pip install gnow
```

## Usage

### Status

```
$ gnow -s
main
-----------------
 Working tree
 - No files.
 Index
 - No files.
 Unpushed commit
 - No commits.
-----------------
```

### git add -> git commit -> git push

```
# Auto commit message
$ gnow

# Manual commit message
$ gnow 'YOUR COMMIT MESSAGE'

 main
---------------------
 Working tree
 - Updated README.md
 Index
 - No files.
 Unpushed commit
 - No commits.
---------------------
 ADD
Add a file to the index? [n/Y or Enter]
Staging done. ✔

 COMMIT
message
 ┗ Updated README.md
branch
 ┗ main
Commiting? [n/Y or Enter]
Commit done. ✔

 PUSH
branch
 ┗ main
Push? [n/Y or Enter]
Push done. ✔
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
 TAG
Latest tag is 1.0.1
New tag is 1.0.2

# Manual input
$ gnow -t 1.0.0
 TAG
Latest tag is 0.0.6
New tag is 1.0.0
Tagging? [n/Y or Enter]

# When there are no tag settings
$ gnow -t
 TAG
No tags are currently.
Auto incremented version is 0.0.1
Tagging? [n/Y or Enter]
```

## Changelog

- 2021-07-09 Start porting to Python
- 2020-07-09 Published a bash script version on Github
