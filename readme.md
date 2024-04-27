# Scaffold for Python(Python web 的脚手架)

默认数据库为: Mysql
默认web端口: 8086

# Framework Features
- Python  
- fastapi(swaggerUI/Openapi.json) 
- Sqlalchemy(默认mysql)
- 自动建表 

## 用的到的地址
- swagger 文档地址：http://127.0.0.1:8086/docs
- redoc 地址：  http://127.0.0.1:8086/redoc 
- openapi 地址： http://127.0.0.1:8086/openapi.json
# static file Supports

> /static

# Users

```sql
grant all privileges on *.* to words@"%" identified by "89759e1284e2479b991d2669de104942" with grant option;
flush privileges;
```

# Usage Demo for user

```
# 0. 打开浏览器地址 http://127.0.0.1:8086/docs
 
# 1.创建用户   /auth/create_user
{
  "name": "leo",
  "email": "leo@qq.com",
  "password": "leo"
}

# 2. 登录 页面右上角Authorize  -- 用上面的密码

# 3. 接口查询用户信息。  auth/create_user
默认使用token。

```

# 工程结构介绍
```
core
    models   -- 数据库表模型
    schemas  -- web接口结构
routes -- web路由
configuration.py -- 配置
main.py -- 入口
```