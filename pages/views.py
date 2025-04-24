from django.shortcuts import render

def about(request):
    return render(request, "pages/about.html")

def about(request):
    portfolio_items = [
        {"modal_id": "festival", "image_path": "images/festival.png", "title": "정릉어울림축제", "description": "전통시장의 현대적 가치를 발굴·홍보하기 위해 제가 총 기획·운영한 정릉어울림축제는 하루 724명의 방문객을 기록하며 지역 활성화에 기여했습니다."},
        {"modal_id": "intern", "image_path": "images/intern.jpg", "title": "인턴십", "description": "2020~21년 겨울, 서울연탄은행에서 인턴으로 근무하며 취약계층을 위한 연탄 배달·사회복지 프로그램을 지원했습니다."},
        {"modal_id": "study", "image_path": "images/study.jpg", "title": "교육 이모저모", "description": "협상, 디지털 마케팅, SW 기초 등 다양한 전문 교육 과정을 수료하며 역량을 강화했습니다."},
    ]
    return render(request, 'pages/about.html', {"portfolio_items": portfolio_items})