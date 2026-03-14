# CNPhoneAPI

[English](#english) | [中文](#中文)

免费的中国手机号归属地查询API，支持自动更新数据库。

## 功能特性

- 支持中国手机号段查询
- 返回归属地信息（省份/城市/运营商/区号/邮编）
- 启动时自动检查更新数据库
- 支持手动触发数据库更新
- 免费部署 (Render)
- 零成本数据

## 在线演示

部署完成后访问: `https://your-app.onrender.com`

## API 使用

### 查询手机号归属地

```bash
curl "https://your-app.onrender.com/api/phone?phone=13800138000"
```

### 更新数据库

```bash
curl "https://your-app.onrender.com/api/db/update"
```

### 查看数据库信息

```bash
curl "https://your-app.onrender.com/api/db/info"
```

### 响应示例

```json
{
  "phone": "13800138000",
  "phone_prefix": "1380013",
  "province": "上海",
  "city": "上海",
  "isp": "中国移动",
  "area_code": "021",
  "zip_code": "200000"
}
```

## 本地运行

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

访问 http://localhost:8000/docs 查看API文档

## 部署到 Render

1. 将代码推送到 GitHub
2. 登录 Render 创建新的 Web Service
3. 配置:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. 点击 Deploy

## 技术栈

- Python 3.11
- FastAPI

## 数据说明

使用纯真IP库作为数据源，支持自动更新。

- 启动时自动检查更新
- 远程有新版自动下载
- 可手动调用更新接口

## License

MIT

---

## English

Free Chinese phone number lookup API with auto-update support.

## Features

- Chinese mobile phone number lookup
- Returns location info (province/city/ISP/area code/zip code)
- Auto-update database on startup
- Manual database update endpoint
- Free deployment (Render)
- Zero cost data

## API Usage

### Query phone number

```bash
curl "https://your-app.onrender.com/api/phone?phone=13800138000"
```

### Update database

```bash
curl "https://your-app.onrender.com/api/db/update"
```

### Get database info

```bash
curl "https://your-app.onrender.com/api/db/info"
```

### Response Example

```json
{
  "phone": "13800138000",
  "phone_prefix": "1380013",
  "province": "Shanghai",
  "city": "Shanghai",
  "isp": "China Mobile",
  "area_code": "021",
  "zip_code": "200000"
}
```

## Local Run

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Visit http://localhost:8000/docs for API documentation

## Deploy to Render

1. Push code to GitHub
2. Login to Render and create new Web Service
3. Configure:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4. Click Deploy

## Tech Stack

- Python 3.11
- FastAPI

## Data Source

Uses ChunZhen IP database with auto-update support.

- Auto-check for updates on startup
- Auto-download when new version available
- Manual update endpoint available

## License

MIT
