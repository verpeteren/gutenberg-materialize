#!/usr/bin/env python3

"""
Simple tool to expand `{#{ code_snippet(file_name="..") }#}` to ease blogging.
Although it is not bound to gutenberg-materialize, or gutenberg, it is convienient to distribute this.
"""

import os
import re
import sys
import glob
import shutil
import fnmatch
from typing import Dict, Tuple

#TODO file_name pattern and file_type pattern could switch place.....

PATTERN = re.compile("{#{ *code_snippet *\( *file_name *= *['\"](?P<file_name>.*?)['\"]( *, *file_type *= *['\"](?P<file_type>.*?)['\"] *)* *\) *}#}", re.DOTALL)

def find_snippet(text: str) -> Tuple[str, Dict[str, str]]:
    """
    Find `{#{' code_snippet(file_name="..", file_type="..") '#}' and fill a dictionary with 'file_name' and 'file_type' keys
    """
    match = PATTERN.search(text)
    dd = {}
    if not match:
        return False, {}
    for named in ['file_name', 'file_type']:
        if match.group(named):
            dd[named] = match.group(named)
    if 'file_type' not in dd:
        dd['file_type'] = ''
    return match.group(0), dd

def replace_snippet_with_content(content: str, org: str, dd: Dict[str, str], dirname: str) -> str:
    """
    Replace the found match with the mardown code block. The content of the included file will be in the code block.
    """
    with open(os.path.join(dirname, dd['file_name']), 'r') as include_h:
        include = include_h.read().rstrip() + "\n"
        included = """__**file**: [%s](%s)__\n\n```%s\n%s\n```\n\n""" % (dd['file_name'], dd['file_name'], dd['file_type'], include )
        content = content.replace(org, included)
    return content

def process_rmd_file(input_file: str) -> str:
    """
    Open the file and return it's expanded content
    """
    content = ''
    directory = os.path.dirname(input_file)
    with open(input_file, 'r') as file_in:
        content = file_in.read()
        while True:
            org, dd = find_snippet(content)
            if org == False:
                break
            content = replace_snippet_with_content(content, org, dd, directory)
    return content

def process_all_rmd_files(input_folder):
    rmd_files = []
    for root, dirnames, filenames in os.walk(input_folder):
        for filename in fnmatch.filter(filenames, '*.rmd'):
            rmd_files.append(os.path.join(root, filename))
    for rmd_file in rmd_files:
        content = process_rmd_file(rmd_file)
        parts = os.path.splitext(rmd_file)
        output_file = parts[0] + '.md'
        with open(output_file, 'w') as file_out:
            file_out.write(content)

def sync_input_to_output(input_folder, output_folder):
    "Delete the output folder and copy the usefull parts of the input_folder"
    shutil.rmtree(output_folder, True)
    shutil.copytree(input_folder,output_folder, ignore=lambda directory, contents: ['.cache', '__pycache__', 'tmp', '*.rmd', '.gitignore', 'Makefile'])

def main():
    if len(sys.argv) != 3:
        print("usage: rmd 'raw_folder' 'content_folder'\n\n* Searches recursively for `.rmd` files in 'raw_folder'.\n  Replace/expand the `{#{ code_snippet(..) }#}` shortcodes in every `.rmd` file.\n  Write the expanded output to the corresponding `.md` file.\n\n* Delete `content_folder` recursively.\n  Copy `raw_folder` into `content_folder` recursively.\n\nNeedless to say, this is a dangerous operation.....")
        sys.exit()
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
    process_all_rmd_files(input_folder)
    sync_input_to_output(input_folder, output_folder)

if __name__ == '__main__':
    main()

def test_find_snippet():
    test_cases = [
        ("""{#{ code_snippet(file_name="some.sh", file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh", file_type="sh")}#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{  code_snippet(file_name="some.sh", file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet (file_name="some.sh", file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name ="some.sh", file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh" , file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh",  file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh",file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh", file_type ="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh", file_type= "sh" ) }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh", file_type="sh") }#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh", file_type="sh")}#}""", {'file_name': 'some.sh', 'file_type': 'sh'}),
        ("""{#{ code_snippet(file_name="some.sh") }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{  code_snippet(file_name="some.sh") }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet (file_name="some.sh") }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet ( file_name="some.sh") }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet( file_name="some.sh") }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet(file_name ="some.sh") }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet( file_name= "some.sh") }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet(file_name="some.sh" ) }#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet(file_name="some.sh" )}#}""", {'file_name': 'some.sh', 'file_type': ''}),
        ("""{#{ code_snippet(file_name="some.sh") }#} """, {'file_name': 'some.sh', 'file_type': ''}),
        (""" {#{ code_snippet(file_name="some.sh") }#} """, {'file_name': 'some.sh', 'file_type': ''}),
    ]
    for test_case, solution in test_cases:
        #print(test_case)
        org, dd = find_snippet(test_case)
        assert len(dd.keys()) == len(solution.keys())
        for k, v in solution.items():
            assert dd[k] == v
        for k, v in dd.items():
            assert solution[k] == v

def test_process_file():
    file_name = "/tmp/tst.txt"
    file_type = 'c'
    with open(file_name, 'w') as file_h:
        file_h.write("int main(const int argc, const char ** argv) {\n\treturn 0;}\n")
    content = """bla\n{#{ code_snippet(file_name="%s", file_type="%s") }#}\nyada"""  % (file_name, file_type)
    org, dd = find_snippet(content)
    content = replace_snippet_with_content(content, org, dd, '')
    print(content)
    assert len(content) == 123

