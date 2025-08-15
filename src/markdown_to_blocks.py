
block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

# def markdown_to_blocks(markdown):
#     blocks = markdown.split("\n\n")
#     filtered_blocks = []
#     for block in blocks:
#         if block == "":
#             continue
#         block = block.strip()
#         filtered_blocks.append(block)
#     return filtered_blocks

def markdown_to_blocks(markdown):
    lines = [line.strip() for line in markdown.split('\n')]
    cleaned_markdown = '\n'.join(lines)
    # Split the input string by double newlines to identify separate blocks
    raw_blocks = cleaned_markdown.split('\n\n')
    # Strip leading and trailing whitespace from each block and remove empty blocks
    blocks = [block.strip() for block in raw_blocks if block.strip()]
    return blocks


def block_to_block_type (block):
    block = block.strip()
    if block.startswith("#"):
        for i in range(1, 7):
            if block.startswith("#" * i + " "):
                return block_type_heading

    # Check if block is a code block
    if block.startswith("```") and block.endswith("```"):
        return block_type_code
    
    # Check if block is a quote block
    if all(line.strip().startswith(">") for line in block.split("\n")):
        return block_type_quote
    
    # Check if block is an unordered list
    lines = block.split("\n")
    if all(line.strip().startswith("* ") or line.strip().startswith("- ") for line in lines):
        return block_type_unordered_list

    # Check if block is an ordered list
    lines = block.split("\n")
    if all(line.strip().startswith(f"{i + 1}. ") for i, line in enumerate(lines)):
        return block_type_ordered_list
    
    # Default to paragraph if none of the above conditions are met
    return block_type_paragraph
