import unittest
import allure
import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


@allure.feature("Game Test")
@allure.story("Start Button Test")
def test_start_button():
    print("Test: Start Button Clicked!")
    # 这里可以加入实际的按钮点击逻辑，模拟点击
    assert True  # 假设点击操作正常


@allure.feature("Game Test")
@allure.story("Character Move Test")
def test_character_move():
    print("Test: Character Moved!")
    # 这里可以加入实际的角色移动逻辑，模拟角色移动
    assert True  # 假设移动操作正常


@allure.feature("Game Test")
@allure.story("Image Recognition Test")
def test_image_recognition():
    print("Test: Image Recognition Started!")

    # 1. 读入 & 归一化到 [0,1]
    img1 = cv2.imread("screenshot.png", cv2.IMREAD_GRAYSCALE).astype(np.float32) / 255.0
    img2 = (
        cv2.imread("expected_image.png", cv2.IMREAD_GRAYSCALE).astype(np.float32)
        / 255.0
    )

    # 2. 形状校验
    assert img1.shape == img2.shape, f"Dimension mismatch: {img1.shape} vs {img2.shape}"

    # 3. 快速差值检查
    diff = np.abs(img1 - img2)
    mean_diff = diff.mean()
    assert mean_diff < 0.05, f"Mean pixel diff too big: {mean_diff:.4f}"

    # 4. 阈值像素占比检查
    bad_ratio = np.count_nonzero(diff > 0.1) / diff.size
    assert bad_ratio < 0.02, f"Bad-pixel ratio too high: {bad_ratio:.2%}"

    # 5. 精细 SSIM 判断
    score = ssim(
        img1,
        img2,
        data_range=1.0,
        gaussian_weights=True,
        sigma=1.5,
        use_sample_covariance=False,
    )
    print(f"Image similarity score: {score * 100:.2f}%")
    assert score >= 0.95, f"SSIM below threshold: {score:.4f}"

    print("Test passed!")


class TestGameAutomation(unittest.TestCase):

    def test_button_click(self):
        test_start_button()

    def test_character_move(self):
        test_character_move()

    def test_image_recognition(self):
        test_image_recognition()


if __name__ == "__main__":
    unittest.main()
