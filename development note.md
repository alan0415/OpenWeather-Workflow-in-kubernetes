# 開發筆記

# Kubernetes 架設 db, django
## mysql
[參考文件](https://kubernetes.io/zh/docs/tasks/run-application/run-single-instance-stateful-application/)
### 優化
1. mysql資料庫密碼改用secret
https://kubernetes.io/zh/docs/tasks/run-application/run-single-instance-stateful-application/

## django
```=cmd
# 存下目前環境安裝的套件
pip freeze > requirements.txt

```

### Reference
[Dockerizing a Python Django Web Application](https://semaphoreci.com/community/tutorials/dockerizing-a-python-django-web-application)