from typing import List
from pathlib import Path

def write_to_file(file_name:str, items:List[str]) -> None:
    with open(file_name, "a") as f_obj:
        for anchor in items:
            print(f"Writing {anchor} to {file_name}")
            f_obj.write(f"{anchor}\n")

def validate_parameters(validate: str, parameter: str) -> None:
    if not validate:
        raise ValueError(f"{parameter} cannot be blank!")

def check_for_function_names(verify: str) -> str:
    return " ".join([f"`{word}`" if "()" in word else word for word in verify.split(" ")]) 

def main():
    
    try:

        file_name = input("File: ")
        language = "python"

        validate_parameters(validate=file_name, parameter="File Name")
     
        markdown_file_name = ".".join([Path(file_name).stem,"md"])
        anchors : List[str] = []
        links : List[str] = []

        with open(file_name, mode="r") as f_obj:
            for anchor_with_spaces in f_obj:
                anchor = anchor_with_spaces.strip()
                if anchor.startswith("#") and anchor.endswith(":"):
                    anchor = anchor[2:][:-1]
                    anchor = check_for_function_names(verify=anchor)
                    link = anchor.lower().replace(" ", "-")
                    anchors.append(f"- [{anchor}](#{link})")
                    links.append(f'#### <a name="{link}"></a> {anchor}:\n```{language}\n```')

        write_to_file(file_name=markdown_file_name,items=anchors)
        write_to_file(file_name=markdown_file_name,items=links)

    except(ValueError, FileNotFoundError) as e:
        print(e)

if __name__ == "__main__":
    main()
