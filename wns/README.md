# WiFi 管家官网

纯静态官网，无需构建步骤。

## 本地预览

```bash
python3 -m http.server 4173 -d .
```

打开 `http://127.0.0.1:4173/`。

## 部署

将本目录中的全部文件上传到 GitHub Pages 路径 `/gw/wns/`：

- 官网：`https://diaoshinanshi.github.io/gw/wns/`
- 隐私政策：`https://diaoshinanshi.github.io/gw/wns/privacy.html`

正式上线前请完成：

- App Store 上线后，将首页「即将登陆 App Store」入口替换为正式下载链接。
- 当前联系邮箱为 `support@wns-wifimanager.app`。
- 根据实际运营主体、服务地区和所接入的第三方 SDK 对隐私政策做法律审核。
