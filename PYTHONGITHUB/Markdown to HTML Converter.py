import os
import markdown

# Configuration
source_dir = 'path/to/your/markdown_files'  # Directory containing Markdown files
output_dir = 'path/to/your/html_files'      # Directory to save HTML files

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Function to convert Markdown to HTML
def convert_markdown_to_html(markdown_text):
    html = markdown.markdown(markdown_text)
    return html

# Function to process files in the source directory
def process_files():
    for filename in os.listdir(source_dir):
        if filename.endswith('.md'):
            markdown_path = os.path.join(source_dir, filename)
            html_filename = os.path.splitext(filename)[0] + '.html'
            html_path = os.path.join(output_dir, html_filename)
            
            # Read Markdown file
            with open(markdown_path, 'r', encoding='utf-8') as file:
                markdown_text = file.read()
            
            # Convert to HTML
            html_text = convert_markdown_to_html(markdown_text)
            
            # Save HTML file
            with open(html_path, 'w', encoding='utf-8') as file:
                file.write(html_text)
            
            print(f"Converted {filename} to {html_filename}")

if __name__ == "__main__":
    print("Starting Markdown to HTML conversion...")
    process_files()
    print("Conversion complete.")
