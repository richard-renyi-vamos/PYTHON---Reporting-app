import pandas as pd

def generate_report(input_excel, output_report):
    try:
        # Read Excel file
        df = pd.read_excel(input_excel)

        # Create a summary of the data
        report_lines = []
        report_lines.append("Report Summary")
        report_lines.append("=" * 50)

        # Basic information about the dataset
        report_lines.append(f"Total Rows: {len(df)}")
        report_lines.append(f"Total Columns: {len(df.columns)}")
        report_lines.append("\n")

        # Column-wise summary
        report_lines.append("Column-wise Summary")
        report_lines.append("-" * 50)
        for column in df.columns:
            report_lines.append(f"Column: {column}")
            report_lines.append(f"  - Non-Null Count: {df[column].count()}")
            report_lines.append(f"  - Unique Values: {df[column].nunique()}")
            if df[column].dtype in ['int64', 'float64']:
                report_lines.append(f"  - Mean: {df[column].mean():.2f}")
                report_lines.append(f"  - Min: {df[column].min()}")
                report_lines.append(f"  - Max: {df[column].max()}")
            report_lines.append("\n")

        # Save the report to a text file
        with open(output_report, 'w') as file:
            file.write("\n".join(report_lines))

        print(f"Report successfully generated and saved to {output_report}.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Input and Output paths
input_excel = "data.xlsx"  # Replace with your Excel file path
output_report = "report.txt"  # Replace with your desired output path

# Generate the report
generate_report(input_excel, output_report)
