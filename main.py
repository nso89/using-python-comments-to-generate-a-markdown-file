from typing import List
from pathlib import Path


LANGUAGE = "python"
HASHTAG : str  = "#"
COLON : str = ":"


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


def validate_file_type(*acceptable_exts : tuple[str], file_name: Path) -> None:
    """
    Check if the file ends with one of the acceptable extensions.

    Args:
        *acceptable_exts : tuple[str] - the tuple containing all the acceptable
                                        extensions.
        file_name: Path - the file name were checking.                                        
    """
    if file_name.suffix not in acceptable_exts:
        raise ValueError("Unacceptable file type!")


def convert_comment_to_markdown_syntax(keywords : set[str], verify : str) -> str:
    """
    Check a string against a set of keywords, if the string exists, add 
    backquotes, and append it to the list. If the word doesn't exist, just 
    append to the list. 

    Args:
        keywords : set[str] - the set containing our keywords.
        verify : str - the word were checking for in our set.

    Returns:
        Using .join(), we return our string properly quoted.
        
    Example:
        Using title() becomes Using `title()`
    """
    return " ".join([f"`{word}`" if word in keywords else word for word in verify.split(" ")])


def main():
 
    try:

        unclean_file_name = input("File Path: ")
        validate_parameters(validate = unclean_file_name, parameter = "File Name")

        file_name = Path.home().joinpath(unclean_file_name)
        
        validate_file_type(".txt",".py", file_name = file_name)

        markdown_file_name = ".".join([str(file_name.parent.joinpath(file_name.stem)), "md"])
        
        keywords = set(get_keywords_from(file_name = "list.txt"))

        anchors : List[str] = []
        section : List[str] = []

        with open(file_name, mode = "r") as f_obj:
            for comment_with_spaces in f_obj:
                comment = comment_with_spaces.strip()
                if comment.startswith(HASHTAG) and comment.endswith(COLON):
                    comment = comment[2:][:-1]
                    anchor = convert_comment_to_markdown_syntax(keywords = keywords, verify = comment)
                    link = comment.lower().replace(" ", "-")
                    anchors.append(f"- [{anchor}](#{link})")
                    section.append(f'#### <a name="{link}"></a> {anchor}:\n```{LANGUAGE}\n```')

        # Using the comments from example.py, the .md file should be:
        """
            - [Using `print()`](#using-print())
            - [Using `type()`](#using-type())
            #### <a name="using-print()"></a> Using `print()`:
            ```python
            ```
            #### <a name="using-type()"></a> Using `type()`:
            ```python
            ```     
        """
        write_to_file(file_name = markdown_file_name, items = anchors)
        write_to_file(file_name = markdown_file_name, items = section)

    except(ValueError, FileNotFoundError) as e:
        print(e)

if __name__ == "__main__":
    main()
