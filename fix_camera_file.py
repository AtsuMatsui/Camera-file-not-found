# Enter this python code to Script Editor
# 下記のコードをScript Editorへコピペして実行します

import nuke

# Replace with your actual file path
# 実際のファイルパスを記入します
file_path = "path/to/your_camera_file.abc"

# Create a camera from the file path
# ファイルパスからカメラを読み込みます
to_node = nuke.toNode("Camera1")
to_node["file"].fromUserText(file_path)
