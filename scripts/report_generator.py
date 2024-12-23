import os
from jinja2 import Environment, FileSystemLoader

def generate_html_report(metrics, output_file):
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    # Render the template with metrics
    html_content = template.render(metrics=metrics)
    
    # Ensure the directory exists
    output_dir = os.path.dirname(output_file)
    os.makedirs(output_dir, exist_ok=True)


    # Generate the report
    with open(output_file, 'w') as report_file:
        report_file.write(html_content)

    print(f"Report generated: {output_file}")
