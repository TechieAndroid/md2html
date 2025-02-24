import markdown
import sys

def convert_markdown_to_html(markdown_text):
    # Use the 'tables' and 'nl2br' extensions
    extensions = ['tables', 'nl2br']
    return markdown.markdown(markdown_text, extensions=extensions)

def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py input.md [output.html]")
        sys.exit(1)
    
    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "output.html"
    
    try:
        with open(input_file, "r", encoding="utf-8") as md_file:
            markdown_text = md_file.read()
            html_content = convert_markdown_to_html(markdown_text)
        
        with open(output_file, "w", encoding="utf-8") as html_file:
            html_file.write(html_content)
        
        print(f"Conversion successful! Output saved to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
