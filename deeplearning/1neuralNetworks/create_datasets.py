import h5py
from PIL import Image
import numpy as np
import os

"""
 全局常量 数据集的组名
"""
IMAGE_DIR_ROOT = "../images/datasets"
CAT_TRAIN_GROUP = "cat/train_set"
CAT_TEST_GROUP = "cat/test_set"
NON_CAT_TRAIN_GROUP = 'noncat/train_set'
NON_CAT_TEST_GROUP = 'noncat/test_set'
DATASETS_NAME = "train_catvnoncat.h5"
ROOT_GROUP_NAME = "images"
DATAFILE_NAMES = {
    'cat/train_set': "cat_train_set",
    'cat/test_set': "cat_test_set",
    'noncat/train_set': "non_cat_train_set",
    'noncat/test_set': "non_cat_test_set"
}


def get_min(image_dir=IMAGE_DIR_ROOT, img_shape=(128, 128)):
    """
     获取图片数据并压缩放 默认 128*128的图片 再转为 numpy 数据
    :param image_dir:
    :param img_shape:
    :return pwhArray:  全部转换完成后的数据,包含文件名和路径名称
    """
    pwhArray = {
        'cat/train_set': [],
        'cat/test_set': [],
        'noncat/train_set': [],
        'noncat/test_set': []
    }
    for root, dirs, files in os.walk(image_dir):
        for filename in files:
            filepath = os.path.join(root, filename)
            # print(root, filename)
            image = Image.open(filepath).convert("RGB")
            image128 = image.resize(img_shape)
            # 获取像素值，并将其转换为numpy数组
            pixels128 = list(image128.getdata())
            pixels128 = np.array(pixels128).reshape((image128.width, image128.height, 3))
            if "noncat" in root:
                if "train_set" in root:
                    pwhArray[CAT_TRAIN_GROUP].insert(-1, pixels128)
                else:
                    pwhArray[CAT_TEST_GROUP].insert(-1, pixels128)
            else:
                if "train_set" in root:
                    pwhArray[NON_CAT_TRAIN_GROUP].insert(-1, pixels128)
                else:
                    pwhArray[NON_CAT_TEST_GROUP].insert(-1, pixels128)
    return pwhArray


def create_group(dataset_name=DATASETS_NAME):
    """
    只创建一个数据集的组名
    :param dataset_name:
    :return group: 和数据集的组对象
    """
    h5 = h5py.File(dataset_name, "a")
    group = h5.create_group(ROOT_GROUP_NAME)
    group.create_group(CAT_TRAIN_GROUP)
    group.create_group(CAT_TEST_GROUP)
    group.create_group(NON_CAT_TRAIN_GROUP)
    group.create_group(NON_CAT_TEST_GROUP)
    return group


def create_datasets(dataset_name=DATASETS_NAME, group=None, images_data=None):
    """

    :param images_data: 传入的数据整理好的数据集
    :param dataset_name:传入数据集的.h5的文件名
    :param group: 传入数据集的组
    :return:
    """
    if images_data is None:
        images_data = get_min()

    if group is None:
        # 获取一个h5py 的 Group对象
        group = create_group(dataset_name=dataset_name)

    # ## 创建 非猫训练数据集
    group[NON_CAT_TEST_GROUP].create_dataset(
        DATAFILE_NAMES[NON_CAT_TEST_GROUP], data=images_data[NON_CAT_TEST_GROUP])
    # ## 创建 非猫测试数据集
    group[NON_CAT_TRAIN_GROUP].create_dataset(
        DATAFILE_NAMES[NON_CAT_TRAIN_GROUP], data=images_data[NON_CAT_TRAIN_GROUP])
    # ## 创建 猫训练数据集
    group[CAT_TRAIN_GROUP].create_dataset(
        DATAFILE_NAMES[CAT_TRAIN_GROUP], data=images_data[CAT_TRAIN_GROUP])
    # ## 创建 猫测试集
    group[CAT_TEST_GROUP].create_dataset(
        DATAFILE_NAMES[CAT_TEST_GROUP], data=images_data[CAT_TEST_GROUP])


def printname(name):
    print(name)


def read_datasets(dataset_name=DATASETS_NAME):
    with h5py.File(dataset_name, "r") as h5:
        group = h5["images"]
        # print(h5.visit(printname))
        # print(h5.keys())
        noncat_test_set = group[NON_CAT_TEST_GROUP][DATAFILE_NAMES[NON_CAT_TEST_GROUP]]
        noncat_train_set = group[NON_CAT_TRAIN_GROUP][DATAFILE_NAMES[NON_CAT_TRAIN_GROUP]][:]
        cat_train_set = group[CAT_TRAIN_GROUP][DATAFILE_NAMES[CAT_TRAIN_GROUP]][:]
        cat_test_set = group[CAT_TEST_GROUP][DATAFILE_NAMES[CAT_TEST_GROUP]][:]
        # print("noncat_test_set shape", noncat_test_set.shape)
        # print("noncat_train_set shape", noncat_train_set.shape)
        # print("cat_train_set shape", cat_train_set.shape)
        # print("cat_test_set shape:", cat_test_set.shape)
        return cat_train_set, cat_test_set, noncat_train_set, noncat_test_set


if __name__ == '__main__':
    # pwhArray1 = get_min()
    # print(pwhArray1.keys())
    # create_datasets()
    read_datasets()

    # with h5py.File("test.h5", "w") as f:
    #     group = f.create_group("images")
    #     group.create_group("cat/train_set")
    #     group.create_group("cat/test_set")
    #     group.create_group("noncat/train_set")
    #     group.create_group("noncat/test_set")
    # # print(get_min())

    # with h5py.File("test.h5", "r") as f:
    #     print(f.keys())
    #     print(f.visit(printname))
    print("end")
