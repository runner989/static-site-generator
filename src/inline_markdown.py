import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_code,
    text_type_italic
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        within_delimiter = False
        part_index = 0
        while part_index < len(parts):
            part = parts[part_index]
            if within_delimiter:
                new_nodes.append(TextNode(part, text_type))
            else:
                if part or part_index == 0:
                    new_nodes.append(TextNode(part, text_type_text))
            within_delimiter = not within_delimiter
            part_index += 1

    return new_nodes    


def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)


def extract_markdown_links(text):
    pattern = r"\[(.*?)\]\((.*?)\)"
    return re.findall(pattern, text)

# Usage example:
# node = TextNode(
#     "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)",
#     text_type_text,
# )
# new_nodes = split_nodes_image([node])


# output would contain:
# [
#     TextNode("This is text with an ", text_type_text),
#     TextNode("image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
#     TextNode(" and another ", text_type_text),
#     TextNode(
#         "second image", text_type_image, "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png"
#     ),
# ]

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        images = extract_markdown_images(node.text)
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for alt, url in images:
            before, remaining_text = remaining_text.split(f"![{alt}]({url})", 1)
            if before:
                new_nodes.append(TextNode(before, text_type_text))
            new_nodes.append(TextNode(alt, "image", url))

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue

        images = extract_markdown_links(node.text)
        if not images:
            new_nodes.append(node)
            continue

        remaining_text = node.text
        for text, url in images:
            before, remaining_text = remaining_text.split(f"[{text}]({url})", 1)
            if before:
                new_nodes.append(TextNode(before, text_type_text))
            new_nodes.append(TextNode(text, "link", url))

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, text_type_text))

    return new_nodes


def text_to_textnodes(text):
    text = text.replace('\n', ' ')
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "_", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    return nodes