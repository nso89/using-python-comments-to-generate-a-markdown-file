from pathlib import Path
from typing import List
import itertools


LANGUAGE = "python"
HASHTAG : str  = "#"
COLON : str = ":"


def read_from(file: Path) -> str:
    with open(file, mode = "r") as f_obj:
        for line in f_obj:
            yield line.strip()


def validate_parameters(validate: str, parameter: str) -> None:
    """
    Verify if validate is blank, if so, raise ValueError.
    """
    if not validate:
        raise ValueError(f"{parameter} cannot be blank!")
    if validate.startswith(" ") or validate.endswith(" "):
        raise ValueError(f"{parameter} cannot begin or end with an empty space!")


def validate_file_type(file_name: Path, acceptable_ext: str = ".py") -> None:
    """
    Check if the file ends with one of the acceptable extensions.                                     
    """
    if file_name.suffix != acceptable_ext:
        raise ValueError("Unacceptable file type!")


def parse(elements: List[str], words: str, index: int) -> str:
    """
    Check if the file ends with one of the acceptable extensions.                                     
    """
    keyword = elements[index]
    converted_word = words.replace(keyword, f"`{keyword}`")
    return converted_word


def convert_word_to_markdown_syntax(words: str) -> tuple[str, bool]:
    """
    Using a pattern, find a specifc keyword, quote it, and
    replace it in the orignal string.
    """
    elements : List[str] = words.split(" ")
    converted_word_and_parse_status : tuple[str, bool]

    if words.startswith("Using"):
        if len(elements) == 2:
            converted_word = parse(elements = elements, words = words, index = -1)
            converted_word_and_parse_status = (converted_word, True)  
        elif len(elements) == 4 and elements[2] == "empty":
            converted_word = parse(elements = elements, words = words, index = -1)
            converted_word_and_parse_status = (converted_word, True)  
        elif len(elements) == 4 and words.endswith("with elements"):
            converted_word = parse(elements = elements, words = words, index = 1)
            converted_word_and_parse_status = (converted_word, True)  
        elif len(elements) == 3 and elements[2] == "Comprehension":
            converted_word = parse(elements = elements, words = words, index = 1)
            converted_word_and_parse_status = (converted_word, True)  
        else:
            converted_word_and_parse_status = (words, False)
    else:
        converted_word_and_parse_status = (words, False)
    return converted_word_and_parse_status
        

def write_to_file(file_name: Path, items: List[str]) -> None:
    with open(file_name, "a") as f_obj:
        for item in items:
            f_obj.write(f"{item}\n")


def main():

    try:

        partial_py_file_path = input("File Path: ").strip()
        complete_py_file_path = Path.home().joinpath(partial_py_file_path)

        validate_file_type(file_name = complete_py_file_path)

        markdown_file_name = complete_py_file_path.with_suffix(".md")

        anchors : List[str] = []
        sections : List[str] = []

        not_safe_to_parse : List = []

        for comment in read_from(file = complete_py_file_path):
            if comment.startswith(HASHTAG) and comment.endswith(COLON):
                comment = comment[2:][:-1]
                anchor, status = convert_word_to_markdown_syntax(words = comment)

                if status:
                    link = comment.lower().replace(" ", "-")
                    anchors.append(f"- [{anchor}](#{link})")
                    sections.append(f'#### <a name="{link}"></a>{anchor}:\n```{LANGUAGE}\n```')
                else:
                    not_safe_to_parse.append(anchor)
                    
        anchors_with_sections = itertools.chain(anchors, sections)
        write_to_file(file_name = markdown_file_name, items = anchors_with_sections)

        if not_safe_to_parse:
            print(f"Unable to parse: {not_safe_to_parse}" )
    
    except (ValueError, FileNotFoundError) as e:
        print(e)
    
if __name__ == "__main__":
    main()
