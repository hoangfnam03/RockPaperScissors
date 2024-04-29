import numpy as np
from keras.preprocessing import image
import os

# Đường dẫn tới thư mục chứa file bạn muốn tải lên
local_path = "/path/to/your/directory/"

# Liệt kê tất cả các file trong thư mục
file_list = os.listdir(local_path)

for fn in file_list:
    # Đường dẫn đầy đủ tới từng file
    path = os.path.join(local_path, fn)
    
    # Load ảnh và chuyển đổi kích thước
    img = image.load_img(path, target_size=(150, 150))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    
    # Dự đoán lớp của ảnh
    images = np.vstack([x])
    classes = model.predict(images, batch_size=10)
    
    # In ra tên file và dự đoán
    print(fn)
    print(classes)
