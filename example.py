import webview
import sys
import os

fronezen = getattr(sys, "frozen", False)

# Check if the application is packaged
if fronezen:
    # If packaged, the current directory is the directory of the executable
    base_dir = sys._MEIPASS
else:
    # If not packaged, the current directory is the directory of the script
    base_dir = os.path.dirname(os.path.abspath(__file__))


index_file = os.path.join(base_dir, "index.html")

dev_url = "http://localhost:5173"

is_dev = False if fronezen else True

url = dev_url if is_dev else index_file


class Api:
    def send(self, value):
        print(value)
        return "Received: " + value


if __name__ == "__main__":
    webview.create_window("My first HTML5 application", url, js_api=Api())
    # HTTP server is started automatically for local relative paths
    webview.start(ssl=True, debug=True)
