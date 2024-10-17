import subprocess
import os

class VideoDownloader:
    def __init__(self):
        self.download_directory = os.path.join(os.getcwd(), 'downloads')
        if not os.path.exists(self.download_directory):
            os.makedirs(self.download_directory)

    def download_videos(self, links):
        success_messages = []
        error_messages = []

        for link in links:
            try:
                result = subprocess.run(
                    ['yt-dlp', link, '-o', os.path.join(self.download_directory, '%(title)s.%(ext)s')],
                    check=True,
                    capture_output=True,
                    text=True
                )
                success_messages.append(f"Successfully downloaded video from: {link}")
            except subprocess.CalledProcessError as e:
                error_messages.append(f"Failed to download video from: {link}\nError: {e.stderr}")

        summary_message = "\n".join(success_messages) + "\n\n" + "\n".join(error_messages)

        return summary_message
