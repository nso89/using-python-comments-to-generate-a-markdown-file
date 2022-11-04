from typing import List
from pathlib import Path

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

def check_for_function_names(verify: str) -> str:
    """
    Using a for loop with str.split(), we check 
    if verify ends with brackets, indicating 
    the word represents a function. If we find 
    brackets, we surround the word with 
    backquotes, append it to a list, and use 
    str.join() with " " as the seperator.

    Args:
    verify: str - the string we're splitting and 
                  looping over.
    
    Returns:
    str - the string with the function name 
          (if any) properly quoted.
          
    Example:
    Using title() becomes Using `title()`
    """
    return " ".join([f"`{word}`" if word.endswith("()") else word for word in verify.split(" ")])

def main():
    
    try:

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

        with open(file_name, mode="r") as f_obj:
           for anchor_with_spaces in f_obj:
                # If we're reading a .py file, the code is indented by 4 spaces,
                # which we have to remove, so that we can use startsiwth(). We
                # can use in, but this doesn't mean the # is at the beginning of the
                # str.
                anchor = anchor_with_spaces.strip()
                if anchor.startswith("#") and anchor.endswith(":"):
                    # If we find the # at the start and : at the end, we slice it out.
                    anchor = anchor[2:][:-1]
                    anchor = check_for_function_names(verify = anchor)
                    link = anchor.lower().replace(" ", "-")
                    anchors.append(f"- [{anchor}](#{link})")
                    section.append(f'#### <a name="{link}"></a> {anchor}:\n```{language}\n```')
        
        # Using the comments from example.py, the md file should be:
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
