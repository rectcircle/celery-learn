# celery 学习

## 运行

```bash
# 安装redis：略
pip install -r requirements.txt
# 运行worker
celery -A get_started.tasks worker --loglevel=info
celery -A get_started.tasks1 worker --loglevel=info
```

运行client

```bash
python run.py
python run1.py
```
