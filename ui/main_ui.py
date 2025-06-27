import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLineEdit, QListWidget, QLabel, QFileDialog,
    QTextEdit
)
import os

class JobMatcherUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Job Matcher")
        self.setGeometry(100, 100, 400, 300)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # 输入框
        self.input_line = QLineEdit()
        self.input_line.setPlaceholderText("Enter keywords, e.g., Berlin, Python, SAP...")
        layout.addWidget(self.input_line)

        # Add & Remove buttons in one line
        button_layout = QHBoxLayout()
        add_btn = QPushButton("Add Keyword")
        add_btn.clicked.connect(self.add_keyword)
        button_layout.addWidget(add_btn)

        delete_btn = QPushButton("Remove Keyword")
        delete_btn.clicked.connect(self.delete_keyword)
        button_layout.addWidget(delete_btn)

        layout.addLayout(button_layout)

        # Upload CV button
        upload_layout = QHBoxLayout()
        upload_btn = QPushButton("Upload Resume")
        upload_btn.clicked.connect(self.upload_resume)
        self.resume_label = QLabel("No resume uploaded")
        self.resume_label.setStyleSheet("color: gray")
        upload_layout.addWidget(upload_btn)
        upload_layout.addWidget(self.resume_label)
        layout.addLayout(upload_layout)

        # List display area
        layout.addWidget(QLabel("Added Keywords:"))
        self.keyword_list = QListWidget()
        layout.addWidget(self.keyword_list)

        # Start button
        self.start_btn = QPushButton("Start Matching")
        self.start_btn.clicked.connect(self.start_matching)
        layout.addWidget(self.start_btn)

        # Match result display area
        self.result_display = QTextEdit()
        self.result_display.setPlaceholderText("This area will display analysis results, prompts, etc...")
        self.result_display.setReadOnly(True)
        self.result_display.setFixedHeight(150)  # Adjust height as needed
        layout.addWidget(self.result_display)

        self.setLayout(layout)

    def add_keyword(self):
        keyword = self.input_line.text().strip()
        if keyword and keyword not in [self.keyword_list.item(i).text() for i in range(self.keyword_list.count())]:
            self.keyword_list.addItem(keyword)
            self.input_line.clear()

    def delete_keyword(self):
        selected_items = self.keyword_list.selectedItems()
        if not selected_items:
            return
        for item in selected_items:
            self.keyword_list.takeItem(self.keyword_list.row(item))

    def upload_resume(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "选择简历文件", "", "PDF Files (*.pdf);;All Files (*)"
        )
        if file_path:
            self.resume_path = file_path  # 完整路径保存起来

            # 获取路径的最后 3 层
            path_parts = file_path.split(os.sep)
            short_path = os.sep.join(path_parts[-3:]) if len(path_parts) >= 3 else file_path

            self.resume_label.setText(f"...{os.sep}{short_path}")

    def start_matching(self):
        keywords = [self.keyword_list.item(i).text() for i in range(self.keyword_list.count())]
        print("匹配关键词：", keywords)
        # TODO: 调用分析模块或爬虫模块

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = JobMatcherUI()
    window.show()
    sys.exit(app.exec_())