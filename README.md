# 環境設定
## 使用カメラ
- ロジクール ウェブカメラ C270nd

## カメラ接続
- 接続確認
```
lsusb
Bus 001 Device 004: ID 0c45:6366 Microdia Webcam
```
## 顔検出
- OpenCV
```
sudo apt update
sudo apt install python3-opencv
```
## 通知機能（Discord）
### サーバーの作成
- サーバーを追加
- 自分と友人のため
- 新規作成
### Webhook URLの取得
- Spidey Bot
- ウェブフックURLをコピー
- curlインストール
```
sudo apt install libcurl4-openssl-dev
```
- Discordに通知
```
curl -X POST -F "file=@/home/my-pi/MyApp2/test.jpg" "https://discord.com/api/webhooks/XXXX/XXXX"
```
