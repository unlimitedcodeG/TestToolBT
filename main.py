import unittest
import allure
import cv2
import numpy as np


# 示例：简单的按钮点击测试
@allure.feature("Game Test")
@allure.story("Start Button Test")
def test_start_button():
    print("Test: Start Button Clicked!")
    # 这里可以加入实际的按钮点击逻辑，模拟点击
    assert True  # 假设点击操作正常


# 示例：简单的角色移动测试
@allure.feature("Game Test")
@allure.story("Character Move Test")
def test_character_move():
    print("Test: Character Moved!")
    # 这里可以加入实际的角色移动逻辑，模拟角色移动
    assert True  # 假设移动操作正常


# 示例：图像识别与对比测试
@allure.feature("Game Test")
@allure.story("Image Recognition Test")
def test_image_recognition():
    print("Test: Image Recognition Started!")

    # 读取图像
    image1 = cv2.imread("screenshot.png", cv2.IMREAD_GRAYSCALE)  # 屏幕截图
    image2 = cv2.imread("expected_image.png", cv2.IMREAD_GRAYSCALE)  # 预期图像

    # 使用OpenCV的模板匹配方法进行图像对比
    res = cv2.matchTemplate(image1, image2, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9  # 设置匹配的阈值

    # 获取匹配结果
    loc = np.where(res >= threshold)

    for pt in zip(*loc[::-1]):
        print(f"匹配区域的位置：{pt}")
        cv2.rectangle(
            image1,
            pt,
            (pt[0] + image2.shape[1], pt[1] + image2.shape[0]),
            (0, 0, 255),
            2,
        )

    # 显示匹配结果
    cv2.imshow("Match", image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # 如果没有匹配，抛出异常
    assert len(loc[0]) > 0, "No match found!"


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
