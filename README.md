
# Caesar Cipher Project

## 项目简介
本项目实现了经典的**凯撒密码**（Caesar Cipher）的加密与解密功能。  
通过简单的移位算法，可以将文本信息进行加密保护，也可以将加密信息恢复为原文。

---

## 项目文件
- `caesar_cipher.py`：  
  - 包含加密函数 `encrypt(text, shift)` 和解密函数 `decrypt(text, shift)`  
  - 支持对字母字符进行加密，非字母字符保持不变  
  - 运行示例中会对 `"information security"` 进行加密与解密，并打印结果
- `README.md`：项目说明文件，包含项目简介、文件功能及使用方法

---

## 使用方法
1. 确保你已安装 Python（推荐 3.10 及以上版本）  
2. 打开命令行或在 PyCharm 中运行 `caesar_cipher.py`：
```bash
python caesar_cipher.py
