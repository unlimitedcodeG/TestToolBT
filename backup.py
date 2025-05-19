import unittest
import allure
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim
from sklearn.metrics import mean_squared_error


# 图像预处理：去噪和增强
def preprocess_image(image):
    # 去噪：使用高斯模糊去噪
    image = cv2.GaussianBlur(image, (5, 5), 0)

    # 直方图均衡化：增强对比度
    image = cv2.equalizeHist(image)

    return image


# 示例：图像识别与对比测试
@allure.feature("Game Test")
@allure.story("Image Recognition Test")
def test_image_recognition():
    print("Test: Image Recognition Started!")

    # 读取图像
    image1 = cv2.imread("screenshot.png", cv2.IMREAD_GRAYSCALE)  # 屏幕截图
    image2 = cv2.imread("expected_image.png", cv2.IMREAD_GRAYSCALE)  # 预期图像

    if image1.shape != image2.shape:
        print("The images have different dimensions!")
        assert False  # 图片尺寸不同，直接终止测试

    # 预处理图像
    image1 = preprocess_image(image1)
    image2 = preprocess_image(image2)

    # 计算结构相似性指数 (SSIM)
    score, _ = ssim(image1, image2, full=True)

    print(f"Image similarity score: {score * 100:.2f}%")

    # 判断是否相似度超过 95%
    assert score >= 0.95, "The images are too different! Similarity score is below 95%."

    # 计算均方误差 (MSE) 作为补充的度量
    mse = mean_squared_error(image1.flatten(), image2.flatten())
    print(f"Mean Squared Error (MSE): {mse}")

    # 如果需要，根据 MSE 来进一步判断图像是否足够相似
    assert mse < 500, "The images are too different! MSE is too high."

    print("Test passed!")


# 测试类的实现
class TestGameAutomation(unittest.TestCase):

    def test_button_click(self):
        test_start_button()

    def test_character_move(self):
        test_character_move()

    def test_image_recognition(self):
        test_image_recognition()


if __name__ == "__main__":
    # 运行指定的测试用例
    unittest.main()
