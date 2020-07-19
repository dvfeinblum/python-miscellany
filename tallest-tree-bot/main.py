import time

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


def debug_menu():
    """
    Optional function you can throw in the while loop below
    to watch all sorts of neat things that helped me with timing.
    """
    import cv2

    cv2.imshow("OpenCV/Numpy normal", img)
    if drop_cnt % 5 == 0:
        print(f"Current FPS: {1 / (time.time() - last_time)}")
        print(f"Current RGB at 0th pixel: {img[0]}")
        print(f"Current sleep time: {dynamic_timer} seconds")


with mss.mss() as sct:
    # Part of the screen to capture; note that this not might work on your computer
    monitor = {"top": 197, "left": 767, "width": 1, "height": 180}
    drop_cnt = 0

    # The logs speed up over time so we need to sleep less as we drop
    dynamic_timer = 1.8
    sleep_timers = {0: 1.47,
                    1: 1.65,
                    2: 4.15}

    while "Screen capturing":
        last_time = time.time()

        # debug_menu()

        img = np.array(sct.grab(monitor))

        if should_press_space(img):
            print("Dropping log!")
            press_and_release("space")
            time.sleep(sleep_timers.get(drop_cnt, dynamic_timer))
            drop_cnt += 1
            dynamic_timer *= 0.99
