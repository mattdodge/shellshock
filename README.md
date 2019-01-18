<p align="center">
<img src="logo.png" />
<em><strong>Write your shell scripts using Python</strong></em>
</p>
<hr/>
Shell scripts are great - they run on most *nix machines, they allow you interact with the file system easily, and they are light weight and don't require a massive runtime. However, the syntax is error prone and they are difficult to manage and test. Shellshock lets you write and test your shell scripts using the Python syntax and test cases you already know and love.

## Installation

Writing with Shellshock requires Python. The shell scripts it outputs do not require Python to run though.
```bash
pip install shellshock
```

## Usage
To convert a Python shellshock script to a regular shell script:
```bash
shellshock my_script.py -o my_script.sh
```
