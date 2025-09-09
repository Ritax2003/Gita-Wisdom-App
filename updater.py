import requests
import os
import subprocess
import sys
import time
from PyQt5.QtWidgets import QMessageBox, QProgressBar

GITHUB_REPO = "Ritax2003/Gita-Wisdom-App"
CURRENT_VERSION = "0.0.4"

class Updater:
    CURRENT_VERSION = CURRENT_VERSION

    def __init__(self, progress_bar: QProgressBar, result_label):
        self.progress_bar = progress_bar
        self.result_label = result_label

    def check_for_update(self):
        latest_version, download_url ,changelog = self.get_latest_release()
        if latest_version and latest_version != CURRENT_VERSION:
            reply = QMessageBox.question(
                None, "Update Available",
                f"A new version {latest_version} is available!\n\nChnagelog:\n{changelog}\n\nDo you want to update?",
                QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes
            )

            if reply == QMessageBox.Yes:
                self.progress_bar.setVisible(True)
                self.progress_bar.setValue(0)
                self.download_and_install_update(download_url)
        else:
            self.result_label.setText("No updates available. You have the latest version.")

    def get_latest_release(self):
        try:
            url = f"https://api.github.com/repos/{GITHUB_REPO}/releases/latest"
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                latest_version = data["tag_name"]
                changelog = data.get("body", "No changelog provided.")
                assets = data.get("assets", [])
                for asset in assets:
                    if asset["name"].endswith(".exe"):
                        return latest_version, asset["browser_download_url"],changelog
            return None, None ,None
        except requests.exceptions.RequestException as e:
            self.result_label.setText(f"Error checking update: {str(e)}")
            return None, None ,None

    def download_and_install_update(self, download_url):
        try:
            # Extract the filename from the URL
            original_filename = download_url.split("/")[-1]
            download_path = os.path.join(os.getcwd(), original_filename)

            response = requests.get(download_url, stream=True)
            total_size = int(response.headers.get("content-length", 0))
            downloaded_size = 0

            with open(download_path, "wb") as f:
                for chunk in response.iter_content(1024):
                    if chunk:
                        f.write(chunk)
                        downloaded_size += len(chunk)
                        progress = int((downloaded_size / total_size) * 100)
                        self.progress_bar.setValue(progress)

            if not os.path.exists(download_path) or os.path.getsize(download_path) == 0:
                self.result_label.setText("Download failed: file is empty.")
                return

            QMessageBox.information(None, "Update Ready", f"App will now restart using: {original_filename}")
            self.start_new_executable_and_exit(download_path)

        except Exception as e:
            self.result_label.setText(f"Update failed: {str(e)}")
            self.progress_bar.setVisible(False)

    # def replace_executable_and_restart(self, new_exe_path):
    #     try:
    #         current_exe = sys.argv[0]
    #         backup_exe = current_exe + ".bak"

    #         if not current_exe.endswith(".exe"):
    #             self.result_label.setText("Auto-update works only when running from an .exe.")
    #             return

    #         # Create a batch file to perform replacement after closing current app
    #         batch_file = "update_replace.bat"
    #         with open(batch_file, "w") as f:
    #             f.write(f'''@echo off
    #             timeout /t 2 /nobreak > NUL
    #             move /Y "{current_exe}" "{backup_exe}"
    #             move /Y "{new_exe_path}" "{current_exe}"
    #             start "" "{current_exe}"
    #             del "%~f0"
    #             ''')

    #         # Run the batch file and exit current app
    #         subprocess.Popen(batch_file, shell=True)
    #         time.sleep(1)
    #         os._exit(0)

        except Exception as e:
            self.result_label.setText(f"Executable replacement failed: {str(e)}")
            self.progress_bar.setVisible(False)
            self.progress_bar.setValue(0)
            self.result_label.setText("Update failed. Please try again later.")
            time.sleep(2)

    def start_new_executable_and_exit(self, new_exe_path):
        try:
            # Launch the new executable
            subprocess.Popen([new_exe_path], shell=True)

            # Delay to let the new app boot up
            time.sleep(1)

            # Kill the current app
            os._exit(0)

        except Exception as e:
            self.result_label.setText(f"Restart failed: {str(e)}")
