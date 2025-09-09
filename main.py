import sys
import json
from PyQt5.QtWidgets import QApplication, QMessageBox
from retriever import GitaRetriever
from llm_handler import GitaLLMHandler
from config import get_api_key
from ui_main import MainWindow
from PyQt5.QtGui import QIcon


def load_verses():
    try:
        with open("data/reformatted_bhagavad_gita.json", "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return []

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("images/app_icon.ico"))
    verses = load_verses()
    retriever = GitaRetriever(verses)
    api_key = get_api_key()
    if not api_key:
        QMessageBox.critical(None, "Error", "No API key provided. Exiting.")
        sys.exit(1)

    llm_handler = GitaLLMHandler(api_key=api_key)
    window = MainWindow(retriever, llm_handler)
    window.show()
    sys.exit(app.exec_())
