import sys
from generate import (
    transfer_contents,
    generate_pages_recursive
)

def main():
    # getting the basepath
    basepath = sys.argv[0] if len(sys.argv) != 0 else '/'
    
    # copying files from static to docs
    transfer_contents(dest="docs", source="static")
    
    # Generating from content using template.html and write it to docs.
    generate_pages_recursive(
        dir_path_content="content",
        template_path="template.html",
        dest_dir_path="docs",
        basepath=basepath,
    )
    
if __name__ == "__main__":
    main()
    
    