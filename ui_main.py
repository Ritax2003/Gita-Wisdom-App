import json
import os
import sys
import requests
from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QTextEdit, QLabel, QTabWidget,
    QMessageBox, QMainWindow,QProgressBar
)
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QPixmap, QFont,QCursor
from updater import Updater

def resource_path(relative_path):
    """ Get absolute path to resource for PyInstaller and normal runs """
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def is_connected():
    try:
        requests.get("https://www.google.com", timeout=3)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False

class UpdateTab(QWidget):
        def __init__(self):
            super().__init__()
            self.initUI()

        def initUI(self):
            self.label = QLabel(f"Current Version: {Updater.CURRENT_VERSION}", self)
            self.check_update_btn = QPushButton("Check for Updates", self)
            self.check_update_btn.clicked.connect(self.check_for_update)

            self.result_label = QLabel("", self)
            self.progress_bar = QProgressBar(self)
            self.progress_bar.setValue(0)
            self.progress_bar.setVisible(False)

            layout = QVBoxLayout()
            layout.addWidget(self.label)
            layout.addWidget(self.check_update_btn)
            layout.addWidget(self.progress_bar)
            layout.addWidget(self.result_label)
            self.setLayout(layout)

            self.updater = Updater(self.progress_bar, self.result_label)

        def check_for_update(self):
            self.updater.check_for_update()

class MainWindow(QMainWindow):
    def __init__(self, retriever, llm_handler):
        super().__init__()
        self.retriever = retriever
        self.llm_handler = llm_handler

        self.setWindowTitle("Gita Wisdom Guide")
        self.setGeometry(200, 100, 900, 600)

        # --- Tabs ---
        self.tabs = QTabWidget()
        self.update_tab = UpdateTab()
        self.tabs.addTab(self.ask_tab(), "💬 Ask Question")
        self.tabs.addTab(self.sample_tab(), "🎯 Sample Queries")
        self.tabs.addTab(self.update_tab,"Update")

        

        # --- Internet status icons ---
        self.online_icon = QPixmap("images/online.jpg").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.offline_icon = QPixmap("images/offline.jpg").scaled(24, 24, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.status_icon = QLabel()
        self.status_icon.setPixmap(self.offline_icon)
        self.status_text = QLabel("Checking connection...")
        self.status_text.setStyleSheet("color: orange; font-size: 12px;")

        # --- Top layout (status bar) ---
        top_layout = QHBoxLayout()
        top_layout.addWidget(self.status_icon)
        top_layout.addWidget(self.status_text)
        stretch_widget = QWidget()
        stretch_layout = QHBoxLayout()
        stretch_layout.setContentsMargins(0,0,0,0)
        stretch_widget.setLayout(stretch_layout)

        # 1️⃣ Wikipedia link
        wiki_label = QLabel(f"Read More Here: "'<a href="https://en.wikipedia.org/wiki/Bhagavad_Gita">Bhagavad Gita Wiki</a>')
        wiki_label.setOpenExternalLinks(True)
        wiki_label.setStyleSheet("color: blue; font-size: 12px;")
        wiki_label.setCursor(QCursor(Qt.PointingHandCursor))
        stretch_layout.addWidget(wiki_label)

        # 2️⃣ Total chapters and verses
        total_chapters = 18  # standard Bhagavad Gita
        total_verses = 640   # approximate total
        verses_label = QLabel(f"Chapters: {total_chapters} | Verses: {total_verses}")
        verses_label.setStyleSheet("font-size: 12px; color: #555; margin-left: 20px;")
        stretch_layout.addWidget(verses_label)

        top_layout.addStretch()
        stretch_layout.addStretch()
        top_layout.addWidget(stretch_widget)

        # --- Container layout ---
        container = QWidget()
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.tabs)
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # --- Timer to auto-refresh connection ---
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_connection_status)
        self.timer.start(2000)  # every 2 sec
        self.update_connection_status()  # call immediately

    # --- Check connection before actions ---
    def check_connection(self):
        """Returns True if online; shows warning if offline."""
        if not is_connected():
            QMessageBox.warning(self, "No Internet", 
                "⚠️ No Internet Connection.\nPlease reconnect and try again.")
            return False
        return True

    # --- Update the status icon and text ---
    def update_connection_status(self):
        if is_connected():
            self.status_icon.setPixmap(self.online_icon)
            self.status_text.setText("Connected to Internet")
            self.status_text.setStyleSheet("color: green; font-size: 12px;")
        else:
            self.status_icon.setPixmap(self.offline_icon)
            self.status_text.setText("No Internet Connection")
            self.status_text.setStyleSheet("color: red; font-size: 12px;")

    

    # --- Ask Question Tab ---
    def ask_tab(self):
        # --- Disclaimer (reused) ---
        self.disclaimer = QLabel(
            "⚠️ Disclaimer: This tool provides spiritual guidance based on the Bhagavad Gita. "
            "For serious mental health concerns, please consult a qualified professional."
        )
        self.disclaimer.setStyleSheet("color: red; font-size: 11px; margin-top: 5px;")
        widget = QWidget()
        layout = QVBoxLayout()

        self.query_input = QTextEdit()
        self.query_input.setPlaceholderText("Type your question here...")
        layout.addWidget(self.query_input)

        btn_layout = QHBoxLayout()
        self.ask_btn = QPushButton("🔮 Get Guidance")
        self.clear_btn = QPushButton("🧹 Clear")
        btn_layout.addWidget(self.ask_btn)
        btn_layout.addWidget(self.clear_btn)
        layout.addLayout(btn_layout)

        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)
        layout.addWidget(self.disclaimer)

        # --- Connect buttons ---
        self.ask_btn.clicked.connect(self.process_query)
        self.clear_btn.clicked.connect(lambda: self.query_input.clear())

        widget.setLayout(layout)
        return widget

    # --- Sample Queries Tab ---
    def sample_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()

        self.samples = [
            "I'm feeling depressed and lost",
            "How do I handle work stress?",
            "What should I do when I fail?",
            "I'm confused about my life purpose",
            "How to deal with difficult people?"
        ]

        self.sample_widgets = {}

        for q in self.samples:
            qa_box = QVBoxLayout()

            btn = QPushButton(q)
            btn.setStyleSheet("font-weight: bold;")
            btn.clicked.connect(lambda _, query=q: self.toggle_sample(query))

            answer_label = QLabel("")
            answer_label.setWordWrap(True)
            answer_label.setStyleSheet("color: darkgreen; margin-left: 10px;")
            answer_label.setVisible(False)

            qa_box.addWidget(btn)
            qa_box.addWidget(answer_label)

            layout.addLayout(qa_box)
            self.sample_widgets[q] = {"button": btn, "label": answer_label}

        layout.addStretch()
        widget.setLayout(layout)
        return widget

    # --- Toggle sample answer ---
    def toggle_sample(self, query):
        if not self.check_connection():
            return  # stop if offline

        btn = self.sample_widgets[query]["button"]
        label = self.sample_widgets[query]["label"]

        if not label.isVisible():
            if not label.text().strip():
                verses = self.retriever.find_relevant_verses(query)
                themes = self.retriever.extract_query_themes(query)
                context = {
                    'formatted_context': "\n".join(
                        [f"Ch {v['chapter']}, V {v['verse']}: {v['text']}" for v in verses]
                    ),
                    'query_themes': themes
                }
                result = self.llm_handler.generate_response(query, context)
                label.setText(f"✨ {result['response']}")

            label.setVisible(True)
            btn.setText(f"{query} ⬆ Hide Answer")
        else:
            label.setVisible(False)
            btn.setText(query)

    # --- Process user query ---
    def process_query(self):
        if not self.check_connection():
            return  # stop if offline

        query = self.query_input.toPlainText().strip()
        if not query:
            QMessageBox.warning(self, "Warning", "Please enter a question.")
            return

        verses = self.retriever.find_relevant_verses(query)
        themes = self.retriever.extract_query_themes(query)
        context = {
            'formatted_context': "\n".join(
                [f"Ch {v['chapter']}, V {v['verse']}: {v['text']}" for v in verses]
            ),
            'query_themes': themes
        }
        result = self.llm_handler.generate_response(query, context)
        self.result_box.setText(result['response'])
