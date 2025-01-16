import cv2

# 视频路径
video_path = "task_programs/task4_level3.mp4" # 替换为你的视频路径

# 打开视频
cap = cv2.VideoCapture(video_path)

# 检查视频是否成功打开
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

# 获取原视频的帧率（FPS）
fps = cap.get(cv2.CAP_PROP_FPS)

# 获取原视频的分辨率
original_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
original_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 设置目标帧率和分辨率
new_fps = 15  # 设置新的播放帧率，15 帧每秒
new_width = 640  # 设置目标宽度
new_height = 480  # 设置目标高度

# 计算每帧之间的延迟（毫秒）
frame_delay = int(1000 / new_fps)  # 计算新的帧延迟（毫秒）

while True:
    # 逐帧读取视频
    ret, frame = cap.read()

    # 如果视频播放完毕，退出
    if not ret:
        print("Video has ended.")
        break

    # 改变帧的分辨率
    frame_resized = cv2.resize(frame, (new_width, new_height))

    # 显示修改分辨率后的帧
    cv2.imshow('Resized and Frame Rate Controlled Video', frame_resized)

    # 控制播放帧率
    if cv2.waitKey(frame_delay) & 0xFF == ord('q'):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
