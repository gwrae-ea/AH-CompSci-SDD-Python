#!/usr/bin/env python3
"""Generate HTML files for all Program*.py files for better readability."""

import os
import re
from pathlib import Path

def get_program_number_and_title(py_file):
    """Extract program number and title from filename."""
    basename = os.path.basename(py_file)
    match = re.search(r'Program\s+(\d+)\s*(?:-\s*)?(.+?)\.py', basename)
    if match:
        num = match.group(1)
        title = match.group(2).strip()
        return num, title
    return None, None

def read_python_file(py_file):
    """Read Python file content."""
    try:
        with open(py_file, 'r', encoding='utf-8') as f:
            return f.read()
    except Exception as e:
        print(f"Error reading {py_file}: {e}")
        return None

def escape_html(text):
    """Escape HTML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def create_html(program_num, title, py_content):
    """Create HTML content with syntax-highlighted Python code."""
    escaped_code = escape_html(py_content)
    
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Program {program_num}: {title}</title>
    <style>
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            background: #f5f5f5;
        }}
        
        .container {{
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
        }}
        
        header {{
            background: white;
            padding: 20px;
            border-radius: 8px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        
        h1 {{
            font-size: 24px;
            margin-bottom: 5px;
        }}
        
        .subtitle {{
            color: #666;
            font-size: 14px;
        }}
        
        .code-block {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            overflow-x: auto;
        }}
        
        pre {{
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            line-height: 1.5;
            background: #2d2d2d;
            color: #f8f8f2;
            padding: 15px;
            border-radius: 4px;
            overflow-x: auto;
        }}
        
        code {{
            font-family: 'Courier New', Courier, monospace;
        }}
        
        footer {{
            text-align: center;
            padding: 20px;
            color: #666;
            font-size: 12px;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>Program {program_num}: {title}</h1>
            <p class="subtitle">AH CompSci SDD - Python Learning Repository</p>
        </header>
        
        <div class="code-block">
            <pre><code>{escaped_code}</code></pre>
        </div>
        
        <footer>
            <p>View the original Python file for execution. This HTML version is for easier reading.</p>
        </footer>
    </div>
</body>
</html>
"""
    return html

def main():
    """Find all Program files and generate HTML versions."""
    base_path = Path('/workspaces/AH-CompSci-SDD-Python')
    
    # Find all Program*.py files
    py_files = sorted(base_path.glob('**/Program*.py'))
    
    if not py_files:
        print("No Program*.py files found")
        return
    
    print(f"Found {len(py_files)} program files. Generating HTML versions...\n")
    
    for py_file in py_files:
        program_num, title = get_program_number_and_title(str(py_file))
        if not program_num:
            print(f"⚠ Skipped: Could not parse {py_file.name}")
            continue
        
        py_content = read_python_file(py_file)
        if not py_content:
            print(f"✗ Failed: Could not read {py_file.name}")
            continue
        
        html_content = create_html(program_num, title, py_content)
        
        # Save HTML in same directory as Python file
        html_file = py_file.with_name(f"Program {program_num}.html")
        
        try:
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(html_content)
            print(f"✓ Created: {html_file.relative_to(base_path)}")
        except Exception as e:
            print(f"✗ Failed to write {html_file}: {e}")
    
    print("\n✓ HTML generation complete!")

if __name__ == '__main__':
    main()
