import os
import shutil

def copy_directory_contents(src, dest):
    if not os.path.exists(dest):
        os.makedirs(dest)
    for item in os.listdir(src):
        s = os.path.join(src, item)
        d = os.path.join(dest, item)
        if os.path.isfir(s):
            copy_directory_contents(s, d)
        else:
            shutil.copy2(s, d)
            print(f"Copied: {s} to {d}")

def extract_title(markdown):
    for line in markdown.split('\n'):
        if line.startswith('# '):
            return line[2:].strip()
    raise ValueError("No H1 header found")

def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    with open(from_path, 'r') as f:
        markdown_content = f.read()

    with open(template_path, 'r') as f:
        tempate_content = f.read()

    html_content = markdown_to_html_node(markdown_content).to_html()
    title = extract_title(markdown_content)
    final_content = template_content.replace('{{ Title }}', title)    
    final_content = template_content.replace('{{ Content}}', html_content)

    os.makedirs(os.path.dirname(dest_path), exist_ok=True)

    with open(dest_path, 'w') as f:
        f.write(final_content)

    print(f"Page generated at {dest_path}")



def main():
    src_dir = './static'
    dest_dir = './public'

    print(f"Deleting {dest_dir}")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)

    copy_directory_contents(src_dir, dest_dir)

    print(f"Copied contents of {src_dir} to {dest_dir}")

if __name__ == "__main__":
    main()