import os
import shutil

def copy_and_rename(template_file, target_dir):
    # Đảm bảo thư mục đích tồn tại
    if not os.path.exists(target_dir):
        print(f"Directory {target_dir} does not exist.")
        return

    # Lấy danh sách các file trong thư mục đích
    target_files = os.listdir(target_dir)
    
    # Sao chép file mẫu với tên mới tương ứng với mỗi file trong thư mục đích
    for target_file in target_files:
        target_file_path = os.path.join(target_dir, target_file)
        # Chỉ sao chép nếu mục tiêu là file (không phải thư mục)
        if os.path.isfile(target_file_path):
            shutil.copy(template_file, target_file_path)

# Đường dẫn đến file mẫu và thư mục đích
template_file_path = 'deviantorgyroombackground.dds'
target_directory = 'event_scenes2'

# Gọi hàm
copy_and_rename(template_file_path, target_directory)

