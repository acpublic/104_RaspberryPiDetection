# OpenCV
import cv2

# File
import datetime
import os

# Discord
import requests

# 通知先Discord
WEBHOOK_URL = "https://discord.com/api/webhooks/xxx/yyy"
DATA = {
    "content": "Raspberry Pi からの通知！",
}

# 撮影画像の保存フォルダを作成
save_dir = "./capture"
os.makedirs(save_dir, exist_ok=True)

# USBカメラを起動（/dev/video0）
cap = cv2.VideoCapture(0)

# HOG + SVM による人検出器
# HOG（Histogram of Oriented Gradients）は画像の特徴量を抽出する手法
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

print("カメラ起動：Ctrl+Cで終了")

while True:
    ret, frame = cap.read()
    if not ret:
        print("カメラから映像が取得できません")
        break

    # 人を検出
    # detectMultiScale は領域（矩形）を返す
    # 「人の可能性がある領域」を複数返します。
    # winStride：検出の移動幅（小さいほど精度UPだが重い）
    # padding：境界の余白
    # scale：画像を縮小しながら検出する倍率
    people, _ = hog.detectMultiScale(frame,
                                     winStride=(8, 8),
                                     padding=(8, 8),
                                     scale=1.05)

    # 人が1人でも検出されたら保存処理
    if len(people) > 0:
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = os.path.join(save_dir, f"{timestamp}.jpg")
        cv2.imwrite(filename, frame)
        print(f"人を検出： {filename}")
        with open(filename, "rb") as f:
            files = {"file": f}
            response = requests.post(WEBHOOK_URL, data=DATA, files=files)
        print(response.status_code)

        # 連続保存を避けるためwait
        cv2.waitKey(2000)

    # 処理を少し軽くするためのwait
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
