import webview
import os

dev_url = "http://localhost:5173"
prod_url = "./static/index.html"

is_dev = os.getenv("ENVIROMENT") == "dev"

url = dev_url if is_dev else prod_url


class Api:
    def send(self, value):
        print(value)
        return "Received: " + value


if __name__ == "__main__":
    webview.create_window("My first HTML5 application", url, js_api=Api())
    # HTTP server is started automatically for local relative paths
    webview.start(ssl=True, debug=is_dev)
