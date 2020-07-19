import time

import cv2
from keyboard import press_and_release
import mss
import numpy as np

# We need to wait to drop the log until this color is totally gone
bg_color = np.array((94, 73, 78, 255))


def should_press_space(img_arr: np.array):
    """
    We look at a sliver of pixels and if there's any color
    that doesn't match the background, we know it's the right
    frame to drop the block.

    :param img_arr: numpy array of the screenshot
    :return: bool indicating if it's time to drop the log
    """
    for arr in img_arr:
        if (not np.array_equal(arr[0], bg_color)) or (not np.array_equal(arr[1], bg_color)):
            return True

    return False


with mss.mss() as sct:
    # Part of the screen to capture
    monitor = {"top": 197, "left": 767, "width": 1, "height": 180}
    cnt = 0

    while "Screen capturing":
        cnt += 1
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = np.array(sct.grab(monitor))

        if should_press_space(img):
            print("Dropping log!")
            press_and_release("space")
            time.sleep(1.77)

        if cnt % 100 == 0:
            print(f"Current FPS: {1 / (time.time() - last_time)}")
            print(f"Current RGB at 0th pixel: {img[0]}")

        # # Display the picture
        # cv2.imshow("OpenCV/Numpy normal", img)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break
