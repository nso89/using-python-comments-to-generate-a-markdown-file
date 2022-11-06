from typing import List
from pathlib import Path

def get_keywords_from(file_name : str) -> List[str]:
    """
    Read words from a file, strip and append to a 
    list using a comprehension.

    Args:
        file_name: str
    
    Returns:
        List[str]
    """
    with open(file_name, "r") as f_obj:
        lines = [word.strip() for word in f_obj.readlines()]
    return lines

def write_to_file(file_name: str, items: List[str]) -> None:
    """
    Append a list to a file.

    Args:
        file_name: str
        items : List[str]

    Returns:
        None
    """
    with open(file_name, "a") as f_obj:
        for item in items:
            f_obj.write(f"{item}\n")

def validate_parameters(validate: str, parameter: str) -> None:
    """
    Verify if validate is blank, if so, raise ValueError 
    indicating the parameter cannot be blank.

    Args:
        validate: str - the string we're checking.
        parameter: str - what the str represents.

    Returns:
        None
    """
    if not validate:
        raise ValueError(f"{parameter} cannot be blank!")

def convert_keywords_to_markdown_syntax(keywords : set[str], verify : str) -> str:
    """
    Check a string against a set of keywords, if the string exists, add 
    backquotes, and append it to the list. If the word doesn't exist, just 
    append to the list. 

    Args:
        keywords : set[str] - the set containing our keywords.
        verify : str - the word were checking for in our set.

    Returns:
        Using .join(), we return our string properly quoted.
    """
    return " ".join([f"`{word}`" if word in keywords else word for word in verify.split(" ")])

def main():

    try:
        
        keywords = set(get_keywords_from(file_name = "list.txt"))

        file_name = input("File: ")
        language = "python"

        validate_parameters(validate = file_name, parameter = "File Name")

        # Using .stem will give use the file name without the extension,
        # allowing us to join .md to the file name.
        markdown_file_name = ".".join([Path(file_name).stem, "md"])

        # The links at the top of the markdown file.
        anchors : List[str] = []

        # The section of code we jump to using the anchor.
        section : List[str] = []

        with open(file_name, mode = "r") as f_obj:
            for anchor_with_spaces in f_obj:
                # If we're reading a .py file, the code is indented by 4 spaces,
                # which we have to remove, so that we can use startsiwth(). We
                # can use in, but this doesn't mean the # is at the beginning of the
                # str.
                anchor = anchor_with_spaces.strip()
                if anchor.startswith("#") and anchor.endswith(":"):
                    # If we find the # at the start and : at the end, we slice it out.
                    anchor = anchor[2:][:-1]
                    anchor = convert_keywords_to_markdown_syntax(keywords = keywords, verify = anchor)
                    link = anchor.lower().replace(" ", "-")
                    anchors.append(f"- [{anchor}](#{link})")
                    section.append(f'#### <a name="{link}"></a> {anchor}:\n```{language}\n```')

        # Using the comments from example.py, the .md file should be:
        """
            - [Using `print()`](#using-`print()`)
            - [Using `type()`](#using-`type()`)
            #### <a name="using-`print()`"></a> Using `print()`:
            ```python
            ```
            #### <a name="using-`type()`"></a> Using `type()`:
            ```python
            ```     
        """
        write_to_file(file_name = markdown_file_name, items = anchors)
        write_to_file(file_name = markdown_file_name, items = section)

    except(ValueError, FileNotFoundError) as e:
        print(e)
    
if __name__ == "__main__":
    main()
