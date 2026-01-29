import re
import os
import shutil
from blocks import (
    block_to_block_type,
    BlockType
)
from sync import (
    markdown_to_blocks
)

from combine import (
    markdown_to_html_node
)

def generate_page(from_path: str, template_path: str, dest_path: str, basepath:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # Read the markdown
    with open(from_path, "r") as f:
        md_contents = f.read()
    
    # Read the templete
    with open(template_path, "r") as f:
        tm_contents = f.read()
        
    node = markdown_to_html_node(markdown=md_contents)
    html_str = node.to_html()
    
    # Extracting the title
    title = extract_title(markdown=md_contents)
    
    # Replacing Title and Content
    tm_contents = tm_contents.replace("{{ Title }}", title)
    tm_contents = tm_contents.replace("{{ Content }}", html_str)
    
    tm_contents = tm_contents.replace('href="/', f'href="{basepath}')
    tm_contents = tm_contents.replace('src="/', f'src="{basepath}')
    
    os.makedirs(os.path.dirname(dest_path), exist_ok=True)
    
    # Writing the updated templete file
    with open(dest_path, "w") as f:
        f.write(tm_contents)

def extract_title(markdown: str) -> str:
    blocks = markdown_to_blocks(markdown=markdown)
    for block in blocks:
        if block_to_block_type(block=block) == BlockType.HEADING:
            result = re.match(r"^#{1} ", block)
            if result:
                return block[result.end():]
                
    raise ValueError("Markdown must have an h1 title")

def generate_pages_recursive(dir_path_content:str, template_path:str, dest_dir_path:str, basepath:str):
    
    for file_name in os.listdir(dir_path_content):
        file_path = os.path.join(dir_path_content, file_name)
        if os.path.isfile(file_path):
            
            if not file_name.endswith(".md"):
                continue
            
            # Changing the extensions
            html_file_name = file_name.replace(".md", ".html")
            target_file_path = os.path.join(dest_dir_path, html_file_name)
            
            os.makedirs(os.path.dirname(target_file_path), exist_ok=True)
            
            generate_page(
                from_path=file_path,
                template_path=template_path,
                dest_path=target_file_path,
                basepath=basepath
            )

        else:
            new_target_dir = os.path.join(dest_dir_path, file_name)
            generate_pages_recursive(file_path, template_path, new_target_dir, basepath)

def transfer_contents(source: str = None, dest: str = None, first_call: bool = True):
    dest_abs = os.path.abspath(dest)
    source_abs = os.path.abspath(source)
    
    # only for first ite
    if os.path.exists(path=dest_abs) and first_call:
        shutil.rmtree(path=dest_abs)
        
    os.makedirs(dest_abs, exist_ok=True)
    
    for file_name in os.listdir(source_abs):
        file_path = os.path.join(source_abs, file_name)
        if os.path.isfile(file_path):
            # print(f"Copying file: {file_path} to {dest_abs}")
            shutil.copy(src=file_path, dst=dest_abs)
        else:
            new_dir = os.path.join(dest_abs, file_name)
            transfer_contents(source=file_path, dest=new_dir, first_call=False)