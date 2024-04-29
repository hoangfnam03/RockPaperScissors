import urllib.request

# Tải xuống tập dữ liệu huấn luyện
urllib.request.urlretrieve("https://storage.googleapis.com/learning-datasets/rps.zip", "/tmp/rps.zip")

# Tải xuống tập dữ liệu kiểm tra
urllib.request.urlretrieve("https://storage.googleapis.com/learning-datasets/rps-test-set.zip", "/tmp/rps-test-set.zip")
