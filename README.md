# using-python-comments-to-generate-a-markdown-file
Using Pyton Comments to Generate Markdown Anchors and Links.

* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Running the Script](#running-the-script)

#### <a name="prerequisites"></a>Prerequisites
1. A completed install of `Python 3.x`.
2. The `.py` file with properly formatted comments.

Formatted Comments:
```
Using function_name():
Using an empty collection_type:
Using collection_type with elements:
Using collection_type Comprehension:
```

#### <a name="setup"></a>Setup
1. Under your `USERPROFILE`, extract the `using-python-comments-to-generate-a-markdown-file-main.zip`.

**Example**:
```batch
C:\Users\nso89\using-python-comments-to-generate-a-markdown-main
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
3. Suppose the path to your `.py` file is `C:\Users\username\Projects\python-cheatsheet-main\using-example\example.py`, just provide the path without the `USERPROFILE`. 

**Example**:
```batch
File Path: Projects\python-cheatsheet-main\using-example\example.py
```

4. The `main.py` script generates the `example.md` file (the `.md` file will be generated in the same folder as the `.py` file).

**Example**:
```batch
C:\Users\nso89\Projects\python-cheatsheet-main\using-example\example.md
```
