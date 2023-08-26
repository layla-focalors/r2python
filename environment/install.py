# 1회 실행, 자동 패키지 설치
import os

packages = ['numpy', 'pandas', 'matplotlib', 'seaborn', 'scikit-learn', 'scipy', 'statsmodels', 'stemgraphic']

for i in range(len(packages)):
    install = f'pip install {packages[i]}'
    os.system(install)
    print("now installing " + packages[i] + "...")
