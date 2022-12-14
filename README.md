# using-python-comments-to-generate-a-markdown-file
Using Pyton Comments to Generate Markdown Anchors and Links

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)

#### <a name="prerequisites"></a>Prerequisites
1. A completed install of `Python 3.x`.
2. The `.py` or `.txt` file you want to convert.

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract the `using-python-comments-to-generate-a-markdown-file-main.zip`.

**Example**:
```batch
C:\Users\nso89\using-python-comments-to-generate-a-markdown-main
```

2. In the `list.txt`, put all the words you wanted quoted (no particular order). For functions, include the `()`.

**Example**:
```
print()
type()
```

#### <a name="running-the-script"></a>Running the Script
1. Open `cmd.exe` and change the folder to the `using-python-comments-to-generate-a-markdown-file-main` folder.

**Example**:
```batch
C:\Users\nso89>cd using-python-comments-to-generate-a-markdown-file-main
```

2. Start the `main.py` script.
```batch
C:\Users\nso89\using-python-comments-to-generate-a-markdown-file-main>python main.py
```

3. Suppose the path to your `.py` file is `C:\Users\username\Projects\python-cheatsheet\example.py`, just provide the path without the `USERPROFILE`. 

**Example**:
```batch
File: Projects\python-cheatsheet\example.py
```

4. The `main.py` script generates the `example.md` file (the `.md` file will be generated in the same folder as the `.py` file).

**Example**:
```batch
C:\Users\nso89\Projects\python-cheatsheet\example.md
```
