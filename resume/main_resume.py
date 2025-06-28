import fitz  # PyMuPDF

class ResumeLoader:
    def __init__(self, pdf_path):
        """
        Initialize the ResumeLoader with the path to the PDF file.
        """
        self.pdf_path = pdf_path
        self.text = None  # Cache for extracted text

    def extract_text(self):
        """
        Extract all text content from the PDF, separated by pages.
        """
        doc = fitz.open(self.pdf_path)
        all_text = []
        for page_num, page in enumerate(doc):
            page_text = page.get_text()
            all_text.append(f"===== PAGE {page_num + 1} =====\n{page_text}")
        self.text = "\n".join(all_text)
        return self.text

    def get_text(self):
        """
        Get the extracted text. If not extracted, it will extract automatically.
        """
        if self.text is None:
            return self.extract_text()
        return self.text


# 示例使用
if __name__ == "__main__":
    loader = ResumeLoader("resume/CV_Haomin Shi_EN.pdf")
    text = loader.get_text()
    print("\n📄 Extracted Text:\n")
    print(text)