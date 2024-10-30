# import os
# from collections import defaultdict
#
# def load_yolo_annotations(label_dir):
#     """
#     加载YOLO格式的标签文件并解析。
#
#     参数:
#     label_dir (str): 标签文件的目录路径。
#
#     返回:
#     dict: 包含每个类别的宽度和高度列表的字典。
#     """
#     annotations = defaultdict(list)
#     for label_file in os.listdir(label_dir):
#         if label_file.endswith(".txt"):
#             with open(os.path.join(label_dir, label_file), 'r') as f:
#                 for line in f.readlines():
#                     parts = line.strip().split()
#                     if len(parts) == 5:
#                         category_id = int(parts[0])
#                         width = float(parts[3])
#                         height = float(parts[4])
#                         annotations[category_id].append((width, height))
#     return annotations
#
# def print_statistics(category_sizes):
#     """
#     打印每个类别的ground truth统计数据。
#
#     参数:
#     category_sizes (dict): 包含每个类别的宽度和高度列表的字典。
#     """
#     for category_id, sizes in category_sizes.items():
#         widths = [size[0] for size in sizes]
#         heights = [size[1] for size in sizes]
#         areas = [size[0] * size[1] for size in sizes]
#
#         print(f"Category: {category_id}")
#         print(f"  Number of ground truths: {len(sizes)}")
#         print(f"  Average width: {sum(widths) / len(widths):.4f}")
#         print(f"  Average height: {sum(heights) / len(heights):.4f}")
#         print(f"  Average area: {sum(areas) / len(areas):.4f}")
#
# # 主函数
# if __name__ == "__main__":
#     label_dir = r"E:\HD\yolov8-main\cervicalData\labels\train2017"  # 标签文件目录
#     category_sizes = load_yolo_annotations(label_dir)
#     print_statistics(category_sizes)
import os
import cv2
from collections import defaultdict


def load_yolo_annotations(label_dir, image_dir):
    """
    加载YOLO格式的标签文件并解析，同时加载图像分辨率。

    参数:
    label_dir (str): 标签文件的目录路径。
    image_dir (str): 图像文件的目录路径。

    返回:
    dict: 包含每个类别的实际宽度和高度列表的字典。
    """
    annotations = defaultdict(list)
    for label_file in os.listdir(label_dir):
        if label_file.endswith(".txt"):
            label_path = os.path.join(label_dir, label_file)
            image_path_base = os.path.join(image_dir, label_file.replace('.txt', ''))

            # 尝试多种图像格式
            image = None
            for ext in ['.bmp', '.jpg', '.png']:
                image_path = image_path_base + ext
                if os.path.exists(image_path):
                    image = cv2.imread(image_path)
                    break

            if image is not None:
                height, width = image.shape[:2]
                with open(label_path, 'r') as f:
                    for line in f.readlines():
                        parts = line.strip().split()
                        if len(parts) == 5:
                            category_id = int(parts[0])
                            rel_width = float(parts[3])
                            rel_height = float(parts[4])
                            abs_width = rel_width * width
                            abs_height = rel_height * height
                            annotations[category_id].append((abs_width, abs_height))
            else:
                print(f"Error: Unable to open image {image_path_base}")
    return annotations


def print_statistics(category_sizes):
    """
    打印每个类别的ground truth统计数据。

    参数:
    category_sizes (dict): 包含每个类别的实际宽度和高度列表的字典。
    """
    for category_id, sizes in category_sizes.items():
        widths = [size[0] for size in sizes]
        heights = [size[1] for size in sizes]
        areas = [size[0] * size[1] for size in sizes]

        print(f"Category: {category_id}")
        print(f"  Number of ground truths: {len(sizes)}")
        print(f"  Average width: {sum(widths) / len(widths):.2f} pixels")
        print(f"  Average height: {sum(heights) / len(heights):.2f} pixels")
        print(f"  Average area: {sum(areas) / len(areas):.2f} square pixels")


# 主函数
if __name__ == "__main__":
    label_dir = r"E:\HD\yolov8-main\cervicalData\labels\train2017"  # 标签文件目录
    image_dir = r"E:\HD\yolov8-main\cervicalData\images\train2017"  # 图像文件目录
    category_sizes = load_yolo_annotations(label_dir, image_dir)
    print_statistics(category_sizes)
