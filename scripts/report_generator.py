import os
from jinja2 import Environment, FileSystemLoader

def generate_html_report(metrics, output_file):
    # Load Jinja2 template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report_template.html')

    # Render the template with metrics
    html_content = template.render(metrics=metrics)

    output_dir = os.path.dirname(output_file)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Generate the report
    with open(output_file, 'w') as report_file:
        report_file.write("<html><body><h1>Model Training Report</h1></body></html>")

    print(f"Report generated: {output_file}")
