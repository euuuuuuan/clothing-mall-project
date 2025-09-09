# 🛒 온라인 쇼핑몰 프로젝트 (Django)

---

### 🌟 프로젝트 소개
이 프로젝트는 **Django와 Python**을 활용하여 사용자 친화적인 **온라인 쇼핑몰**을 구축한 예제입니다.  

로그인, 회원가입, 장바구니, 결제 시스템 등 **기본적인 전자상거래 기능**을 구현하여,  
웹 개발의 전반적인 과정을 경험하고 **사용자 중심의 UI/UX 설계**에 중점을 두었습니다.

---

### 🚀 주요 기능
- ✅ **사용자 인증**: Django의 기본 인증 시스템을 활용한 로그인 및 회원가입 기능  
- ✅ **상품 관리**: 상품 목록 조회, 상세 페이지 확인 기능  
- ✅ **장바구니 시스템**: 상품 담기, 수량 변경, 삭제 기능  
- ✅ **주문 및 결제**: 장바구니 상품을 기반으로 주문 생성 및 완료 페이지 제공  
- ✅ **UI/UX 개선**: `landing.html` 및 `style.css`를 개선하여 전문적인 쇼핑몰 디자인 구현  

---

## 💡 기술적 성과 및 문제 해결
- 🚀 **Django 프레임워크 활용**: MTV(Model-Template-View) 아키텍처 이해 및 핵심 기능 구현  
- 🛠️ **405 오류 해결**: HTML 폼의 `method` 속성과 Django 뷰의 `@require_POST` 불일치 문제 해결  
- 🖼️ **정적 파일 관리**: `STATIC_URL`, `STATICFILES_DIRS` 최적화로 CSS 및 이미지 로드 문제 해결  
- 🗃️ **데이터베이스 연동**: SQLite3를 통한 상품, 장바구니, 주문 데이터 관리  
- ⭐ **코드 디버깅**: Pillow 모듈 미설치, 경로 오류 등 문제를 해결하며 디버깅 능력 강화  

---

## 🤖 AI 도구 활용
본 프로젝트는 **Google Gemini, ChatGPT, Claude** 등의 AI 도구를 적극적으로 활용했습니다.

- 📚 **학습 지원**: Django의 기능 및 템플릿 문법 학습 시간을 단축  
- ✨ **코드 품질 개선**: 뷰 함수 최적화 및 HTML 템플릿 구조 개선  
- 🧩 **문제 해결**: 반복되는 `405 오류`, `NameError` 원인을 AI와 함께 분석 및 해결  
- 📝 **문서화 보조**: README 및 프로젝트 구조 설명을 AI를 통해 체계적으로 정리  

---

## 🛠️ 개발 환경 및 실행 방법

### ⚙️ 실행 환경 및 기술 스택
- ![Python](https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white)  
- ![Django](https://img.shields.io/badge/Django-5.0-092E20?style=flat-square&logo=django&logoColor=white)  
- ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)  
- ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white)  
- ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)  
- ![Pillow](https://img.shields.io/badge/Pillow-Image%20Library-yellow?style=flat-square)  

---

### ▶ 실행 방법

1️⃣ **프로젝트 클론**

[git clone](https://github.com/your-username/your-repository.git)

2️⃣ 가상 환경 생성 및 활성화

```
python -m venv venv
# Windows
.\venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```
3️⃣ 의존성 설치

```
pip install -r requirements.txt
# 또는
pip install Django Pillow
```
4️⃣ 데이터베이스 마이그레이션

```
python manage.py makemigrations
python manage.py migrate
```
5️⃣ 슈퍼유저 생성 (관리자 계정)

```
python manage.py createsuperuser
```
6️⃣ 서버 실행

```
python manage.py runserver
```
7️⃣ 접속

```
http://127.0.0.1:8000/
```

---
📂 프로젝트 구조 예시
```
clothing-mall-project/
 ┣ 📂 myshop/                  # 프로젝트 설정
 ┣ 📂 shop/                    # 쇼핑몰 앱
 ┃ ┣ 📂 migrations/
 ┃ ┣ 📂 static/shop/
 ┃ ┃ ┣ 📂 images/
 ┃ ┃ ┗ style.css
 ┃ ┣ 📂 templates/shop/
 ┃ ┣ admin.py
 ┃ ┣ models.py
 ┃ ┣ urls.py
 ┃ ┗ views.py
 ┣ 📂 venv/                    # 가상 환경
 ┣ db.sqlite3
 ┗ manage.py
```

### 🧑‍💻 개발자 정보

| 이름   | 역할               | 연락처                                                                 |
| :----- | :----------------- | :--------------------------------------------------------------------- |
| 전유안 | QA 자동화 엔지니어 | GitHub: [euuuuuuan](https://github.com/euuuuuuan)
