import math
import os

import numpy as np
from PIL import Image

"""
deep learning :
    1.1.2 Building basic functions with numpy 
    LEARNING REMEMBER DOWNS
    • np.exp(x) works for any np.array x and applies the exponential function
      to every coordinate
    • the sigmoid function and its gradient
    • image2vector is commonly used in deep learning
    • np.reshape is widely used. In the future, you’ll see that keeping your
      matrix/vector dimensions straight will go toward eliminating a lot of bugs.
    • numpy has efficient built-in functions
    • broadcasting is extremely useful
"""


def basic_sigmoid(x):
    """
    实现一个基本的 sigmoid S 曲线函数
    输入一个 实数值 返回结果
     s = 1 / (1 + math.exp(-x))
    """
    s = 1 / (1 + math.exp(-x))
    return s


x_x = [1, 2, 3, 4, 5, 6, 7]

print(basic_sigmoid(x_x[1]))

'''
    使用 numpy 模块 是实现S 曲线
'''
# 定义一个 S曲线的 x 一维数组
x_a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
s_a = np.exp(x_a)
print(s_a)


def sigmoid(x):
    """
    :param x: 给定义任意一个向量或者矩阵计算其倒数 S 曲
    :return s: 返回一个 计算完成后的 sigmoid 曲线
    """
    s = 1 / (1 + np.exp(x))

    return s


print("=======")
print(sigmoid(x_a))


def sigmoid_derivative(x):
    """
    计算 sigmoid 函数的导数  公式: σ′(x) = σ(x)(1 − σ(x))
    :param x: x 输入 标量或者数字数组
    :return ds: 返回关于 sigmoid 函数的梯度或者叫导数
    """
    ds = sigmoid(x) * (1 - sigmoid(x))
    return ds


print(sigmoid_derivative(x_a))


# GRADED FUNCTION: image2vector
def image2vector(image):
    """
    Argument:
    image -- a numpy array of shape (length, height, depth)
    Returns:
    v -- a vector of shape (length*height*depth, 1)
    """

    ### START CODE HERE

    v = image.reshape((image.shape[0] * image.shape[1] * image.shape[2]), 1)
    return v


def getImage(image_path="images/test.jpg"):
    """
    获取图片
    :param image_path: 传入一个图片的路径
    :return pixel_array: 返回一个 numpy 数据类型的数组
    """
    # 打开图片
    image = Image.open(image_path).convert("RGB")
    # 显示图片
    # image.show()
    # 获取图片大小
    width, height = image.size
    print("width: ", image.format, width, "height: ", height)
    # 获取像素值
    pixel_value = list(image.getdata())
    # 转换为numpy数组
    pixel_array = np.array(pixel_value).reshape((width, height, 3))
    print("pixel_array: ", pixel_array.shape)
    return pixel_array


getImage()


def normalizeRows(x):
    """
    规范化行Another common technique we use in Machine Learning and Deep Learning is to
    normalize our data. It often leads to a better performance because gradient descent
    converges faster after normalization. Here, by normalization we mean changing x to ||X||
    (dividing each row vector of x by its norm).
    For example, if
    x =
    [0 3 4
    2 6 4]
    :return 返回规范化行 的数据:
    """
    # Compute x_norm as the norm 2 of x. Use np.linalg.norm(..., ord =2, axis = ..., keepdims = True)
    x_norm = np.linalg.norm(x, axis=1, keepdims=True)
    x = x / x_norm
    print("x_norm.shape:", x_norm.shape, "x.shape: ", x.shape)
    return x


x1 = np.array([
    [0, 3, 4],
    [1, 6, 4]])
print(str(normalizeRows(x1)))


# GRADED FUNCTION: softmax
def softmax(x):
    """Calculates the softmax for each row of the input x.
    Your code should work for a row vector and also for matrices of
    shape (n, m). , →
    Argument:
    x -- A numpy matrix of shape (n,m)
    Returns x:
    s -- A numpy matrix equal to the softmax of x, of shape (n,m)
    """
    # Apply exp() element-wise to x. Use np.exp(...).
    x_exp = np.exp(x)
    # Create a vector x_sum that sums each row of x_exp. Use np.sum(..., axis = 1, keepdims = True). , →
    x_sum = np.sum(x_exp, axis=1, keepdims=True)
    print("x_sum: ", x_sum)
    # Compute softmax(x) by dividing x_exp by x_sum. It should automatically use numpy broadcasting. , →
    s = x_exp / x_sum
    return s


print(softmax(x1))
