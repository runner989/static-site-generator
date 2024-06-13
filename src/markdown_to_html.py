from htmlnode import ParentNode
from textnode import TextNode
from inline_markdown import text_to_textnodes
from markdown_to_blocks import (
    block_to_block_type,
    markdown_to_blocks,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list,
)


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []

    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == block_type_heading:
            level = block.count('#',0, block.find( ' '))
            content = block[level + 1:].strip()
            html_block = ParentNode(f"h{level}", text_to_textnodes(content))
            children.append(html_block)
        elif block_type == block_type_unordered_list:
            items = block.split('\n')
            list_items = [ParentNode("li", text_to_textnodes(item[2:].strip())) for item in items]
            html_block = ParentNode("ul", list_items)
            children.append(html_block)
        elif block_type == block_type_ordered_list:
            items = block.split('\n')
            list_items = [ParentNode("li", text_to_textnodes(item[item.index('.') + 1:].strip())) for item in items]
            html_block = ParentNode("ol", list_items)
            children.append(html_block)
        elif block_type == block_type_code:
            lines = block.split('\n')[1:-1]
            content = '\n'.join(lines).strip()
#            content = block.strip('`').strip()
            html_block = ParentNode("pre", [ParentNode("code", [TextNode(content, "text")])])
            children.append(html_block)
        elif block_type == block_type_quote:
            lines = block.split('\n')
            content = '\n'.join(line.strip('> ') for line in lines)
            # content = block[2:].strip()
            html_block = ParentNode("blockquote", text_to_textnodes(content))
            children.append(html_block)
        else:
            html_block = ParentNode("p", text_to_textnodes(block))
            children.append(html_block)

    return ParentNode("div", children)

