# 45th github project -->PDF Merger
print('----------PDF Merger----------')
from pypdf import PdfWriter, PdfReader


def main():
    print("PDF MERGER")

    raw = input("PDF files to merge (comma-separated): ")
    files = [f.strip() for f in raw.split(",") if f.strip()]

    if len(files) < 2:
        print("Enter at least two files.")
        return

    output = input("Output file name (e.g. merged.pdf): ").strip()
    if not output.endswith(".pdf"):
        output += ".pdf"

    writer = PdfWriter()

    try:
        for path in files:
            reader = PdfReader(path)
            for page in reader.pages:
                writer.add_page(page)
            print(f"Added {path} ({len(reader.pages)} pages)")
    except FileNotFoundError as e:
        print(f"File not found: {e.filename}")
        return
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return

    with open(output, "wb") as f:
        writer.write(f)

    print(f"\nMerged into {output}")

main()