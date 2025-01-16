import cv2
import numpy as np

# 初始化视频捕捉
cap = cv2.VideoCapture(0)  # 替换为视频文件或摄像头设备号

# 红色和蓝色的HSV范围
lower_red = np.array([0, 120, 70])
upper_red = np.array([10, 255, 255])

lower_blue = np.array([100, 120, 70])
upper_blue = np.array([140, 255, 255])

while True:
    # 读取视频帧
    ret, frame = cap.read()
    if not ret:
        break

    # 转换为HSV色彩空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 掩模提取红色区域
    mask_red = cv2.inRange(hsv, lower_red, upper_red)
    mask_blue = cv2.inRange(hsv, lower_blue, upper_blue)

    # 查找红色和蓝色的轮廓
    contours_red, _ = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contours_blue, _ = cv2.findContours(mask_blue, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 绘制红色轮廓及其重心
    for contour in contours_red:
        if cv2.contourArea(contour) > 500:  # 过滤掉太小的区域
            # 计算轮廓的重心
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # 绘制轮廓和重心
                cv2.drawContours(frame, [contour], -1, (0, 0, 255), 2)
                cv2.circle(frame, (cX, cY), 5, (0, 0, 255), -1)

    # 绘制蓝色轮廓及其重心
    for contour in contours_blue:
        if cv2.contourArea(contour) > 500:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cX = int(M["m10"] / M["m00"])
                cY = int(M["m01"] / M["m00"])
                # 绘制轮廓和重心
                cv2.drawContours(frame, [contour], -1, (255, 0, 0), 2)
                cv2.circle(frame, (cX, cY), 5, (255, 0, 0), -1)

    # 显示结果
    cv2.imshow("Frame", frame)

    # 按'q'键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
