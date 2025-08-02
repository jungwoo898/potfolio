# Potfolio

Django 기반의 포트폴리오 웹 애플리케이션입니다.

## 주요 기능
- 블로그 및 게시글 관리 (`blog`, `posts` 앱)
- 게시판 기능 (`boards` 앱)
- 정적 페이지 제공 (`pages` 앱)
- 사용자 인증 및 계정 관리 (`users` 앱)

## 개발 환경 설정
1. 저장소를 클론합니다.
2. 가상환경을 생성하고 활성화합니다.
3. 필요한 패키지를 설치합니다. (예: `pip install django`)
4. 데이터베이스 마이그레이션을 수행합니다: `python manage.py migrate`
5. 개발 서버를 실행합니다: `python manage.py runserver`

## 테스트 실행
```bash
python manage.py test
```

## 라이선스
이 프로젝트는 개인 학습용으로 제작되었습니다.
