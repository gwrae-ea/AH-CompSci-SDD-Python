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


def read_program_markdown(py_file, program_num):
    """Read matching Program markdown file in the same folder, if available."""
    folder = Path(py_file).parent
    md_candidates = sorted(folder.glob("Program*.md"))
    for md_file in md_candidates:
        if re.search(rf"Program\s+{re.escape(program_num)}\b", md_file.name):
            try:
                with open(md_file, 'r', encoding='utf-8') as f:
                    return f.read()
            except Exception as e:
                print(f"Error reading {md_file}: {e}")
                return ""
    return ""


def extract_markdown_section(md_text, section_name):
    """Extract a top-level markdown section like '## Analysis'."""
    if not md_text:
        return ""

    pattern = rf"^##\s+{re.escape(section_name)}\s*$([\s\S]*?)(?=^##\s+|\Z)"
    match = re.search(pattern, md_text, flags=re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip()


def extract_technical_explanation(md_text):
    """Extract the '### Technical Explanation' block before Analysis."""
    if not md_text:
        return ""

    pattern = r"^###\s+Technical Explanation\s*$([\s\S]*?)(?=^---\s*$|^##\s+Analysis\s*$|\Z)"
    match = re.search(pattern, md_text, flags=re.MULTILINE)
    if not match:
        return ""
    return match.group(1).strip()


def _parse_markdown_table_row(line):
    row = line.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    return [cell.strip() for cell in row.split("|")]


def _is_markdown_separator_row(line):
    row = line.strip()
    if row.startswith("|"):
        row = row[1:]
    if row.endswith("|"):
        row = row[:-1]
    cells = [c.strip() for c in row.split("|")]
    if not cells:
        return False
    return all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def convert_test_plan_to_html(test_plan_text):
    """Convert markdown test-plan table to HTML table while preserving surrounding text."""
    if not test_plan_text:
        return '<div class="section-content">Section not found in matching Program markdown file.</div>'

    lines = test_plan_text.splitlines()
    table_start = -1
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and line.strip().count("|") >= 2:
            table_start = i
            break

    if table_start == -1:
        return f'<div class="section-content">{escape_html(test_plan_text)}</div>'

    table_end = table_start
    for i in range(table_start, len(lines)):
        if lines[i].strip().startswith("|") and lines[i].strip().count("|") >= 2:
            table_end = i
        else:
            break

    before_text = "\n".join(lines[:table_start]).strip()
    table_lines = lines[table_start:table_end + 1]
    after_text = "\n".join(lines[table_end + 1:]).strip()

    if len(table_lines) < 2 or not _is_markdown_separator_row(table_lines[1]):
        return f'<div class="section-content">{escape_html(test_plan_text)}</div>'

    headers = _parse_markdown_table_row(table_lines[0])
    body_rows = [_parse_markdown_table_row(line) for line in table_lines[2:]]

    html_parts = []
    if before_text:
        html_parts.append(f'<div class="section-content">{escape_html(before_text)}</div>')

    html_parts.append('<div class="table-wrap"><table class="test-plan-table"><thead><tr>')
    for header in headers:
        html_parts.append(f"<th>{escape_html(header)}</th>")
    html_parts.append('</tr></thead><tbody>')

    for row in body_rows:
        html_parts.append('<tr>')
        padded_row = row + [""] * (len(headers) - len(row))
        for cell in padded_row[:len(headers)]:
            html_parts.append(f"<td>{escape_html(cell)}</td>")
        html_parts.append('</tr>')

    html_parts.append('</tbody></table></div>')

    if after_text:
        html_parts.append(f'<div class="section-content">{escape_html(after_text)}</div>')

    return "".join(html_parts)

def escape_html(text):
    """Escape HTML special characters."""
    return (text
            .replace('&', '&amp;')
            .replace('<', '&lt;')
            .replace('>', '&gt;')
            .replace('"', '&quot;')
            .replace("'", '&#39;'))

def create_html(program_num, title, py_content, technical_text, analysis_text, design_text, implementation_text, test_plan_text):
    """Create HTML content with syntax-highlighted Python code."""
    escaped_code = escape_html(py_content)
    technical_html = escape_html(technical_text) if technical_text else "Section not found in matching Program markdown file."
    analysis_html = escape_html(analysis_text) if analysis_text else "Section not found in matching Program markdown file."
    design_html = escape_html(design_text) if design_text else "Section not found in matching Program markdown file."
    implementation_html = escape_html(implementation_text) if implementation_text else "Section not found in matching Program markdown file."
    test_plan_html = convert_test_plan_to_html(test_plan_text)
    
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
        
        .section-block {{
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-bottom: 20px;
        }}

        h2 {{
            font-size: 20px;
            margin-bottom: 10px;
            color: #1f2937;
        }}

        .section-content {{
            background: #fafafa;
            border: 1px solid #e5e7eb;
            border-radius: 4px;
            padding: 12px;
            white-space: pre-wrap;
            font-family: 'Courier New', Courier, monospace;
            font-size: 13px;
            margin-bottom: 12px;
        }}

        .python-code-label {{
            font-size: 14px;
            font-weight: 600;
            color: #374151;
            margin: 8px 0;
        }}

        .table-wrap {{
            overflow-x: auto;
            border: 1px solid #e5e7eb;
            border-radius: 4px;
            background: #fff;
            margin-bottom: 12px;
        }}

        .test-plan-table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13px;
        }}

        .test-plan-table th,
        .test-plan-table td {{
            border: 1px solid #e5e7eb;
            padding: 8px;
            text-align: left;
            vertical-align: top;
        }}

        .test-plan-table th {{
            background: #f3f4f6;
            font-weight: 600;
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
        
        <section class="section-block">
            <h2>Technical Explanation</h2>
            <div class="section-content">{technical_html}</div>
        </section>

        <section class="section-block">
            <h2>Analysis</h2>
            <div class="section-content">{analysis_html}</div>
        </section>

        <section class="section-block">
            <h2>Design</h2>
            <div class="section-content">{design_html}</div>
        </section>

        <section class="section-block">
            <h2>Implementation</h2>
            <div class="section-content">{implementation_html}</div>
            <div class="python-code-label">Python Code</div>
            <pre><code>{escaped_code}</code></pre>
        </section>

        <section class="section-block">
            <h2>Test Plan</h2>
            {test_plan_html}
        </section>
        
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

        md_content = read_program_markdown(str(py_file), program_num)
        technical_text = extract_technical_explanation(md_content)
        analysis_text = extract_markdown_section(md_content, "Analysis")
        design_text = extract_markdown_section(md_content, "Design")
        implementation_text = extract_markdown_section(md_content, "Implementation")
        test_plan_text = extract_markdown_section(md_content, "Test plan")
        if not test_plan_text:
            test_plan_text = extract_markdown_section(md_content, "Test Plan")
        
        html_content = create_html(
            program_num,
            title,
            py_content,
            technical_text,
            analysis_text,
            design_text,
            implementation_text,
            test_plan_text,
        )
        
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
