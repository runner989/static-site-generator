import os
import shutil
import sys

from markdown_to_html import markdown_to_html_node

def copy_directory_contents(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isdir(s):
            copy_directory_contents(s, d)
        else:
            shutil.copy2(s, d)
            print(f"Copied: {s} to {d}")

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No H1 header found")

def generate_page(from_path, template_path, dest_path, basepath='/'):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        template_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()

    title = extract_title(markdown_content)

    final_content = template_content.replace('{{ Title }}', title)    
    final_content = final_content.replace('{{ Content }}', html_content)
    
    # Replace href and src attributes with basepath
    final_content = final_content.replace('href="/', f'href="{basepath}')
    final_content = final_content.replace('src="/', f'src="{basepath}')

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(final_content)

    print(f"Page generated at {dest_path}")

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath='/'):
    for item in os.listdir(dir_path_content):
        item_path = os.path.join(dir_path_content, item)
        dest_path = os.path.join(dest_dir_path, item.replace('.md', '.html'))

        if os.path.isdir(item_path):
            generate_pages_recursive(item_path, template_path, dest_path, basepath)
        elif item_path.endswith('.md'):
            generate_page(item_path, template_path, dest_path, basepath)


def main():
    # Get basepath from CLI argument, default to '/'
    basepath = sys.argv[1] if len(sys.argv) > 1 else '/'
    
    src_dir = './static'
    dest_dir = './docs'

    print(f"Deleting {dest_dir}")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    copy_directory_contents(src_dir, dest_dir)
    print(f"Copied contents of {src_dir} to {dest_dir}")

    generate_pages_recursive('content', 'template.html', 'docs', basepath)

if __name__ == "__main__":
    main()