# 萌天天官网（静态站）

用于 App Store「支持网址 / 营销网址 / 隐私政策网址」的静态页面。

## 本地预览

```bash
cd website
python3 -m http.server 8080
```

浏览器打开：

- 首页：http://localhost:8080/
- 隐私政策：http://localhost:8080/privacy.html

## 部署前请替换

1. 首页「即将上线 App Store」按钮的真实商店链接
2. 页脚版权主体（如需公司法定名称）

联系邮箱已统一为：`Geetikagujral@icloud.com`（首页首屏、导航、页脚与隐私政策均已展示）。

## 文件说明

| 路径 | 说明 |
|------|------|
| `index.html` | 产品官网（中英切换） |
| `privacy.html` | 隐私政策（中英切换） |
| `styles.css` | 样式 |
| `assets/` | 来自 iOS 工程的 App Icon / BrandLogo / OpenMoji 装饰图 |
