# SBAH Master Plan v5.1 — Definitive Final
## Claude CLI 에이전트의 절대 기준 (SSOT)

---

## 0) Release Blockers (이 6가지가 0이 아니면 출판 불가)

1. Tier-3 core claims = 0
2. Data↔prose mismatches = 0
3. AI banned words = 0
4. Print images < 300 DPI = 0
5. EPUB errors (epubcheck) = 0
6. KDP preflight violations = 0

---

## 1) 정체성

### 한 문장
A living, evidence-first narrative tracking how AI predictions convert
into measurable reality—month by month—using primary sources,
reproducible data, and falsifiable scorecards.

### The Confirmation Gap
기술적 변곡점과 대중적 인식 사이의 시차.
- Capability inflection: Nov 17 → Dec 11, 2025
- Behavioral proof: Dec 2025 → Jan 2026
- Public confirmation: Feb 5, 2026

Ch1 명명, Ch8 심화, Ch14 귀결.

### 독자
1차: Product/Engineering 리더, 투자자, 정책 직군
2차: 실무 개발자 (agentic workflow)
3차: "AI가 내 직업에 미치는 영향" 일반 독자

---

## 2) 목표 수치

| 항목 | 현재 | 목표 |
|------|------|------|
| 총 단어 | 67K | 80K~85K |
| PDF 페이지 | 240 | 190~210 |
| Words/page | ~289 | 380~420 |
| Named characters | ~8 | 20~30 |
| Tier-3 core claims | 다수 | 0 |
| AI 금지어 | 미측정 | 0 |
| Ch12 citations | 9 | 20+ |
| EPUB errors | 미측정 | 0 |

---

## 3) 챕터 블루프린트 (6단계)

```
1. Cold Open Scene (300~600 words)
   → 날짜 + 장소 + 인물 + 감각 디테일 1개

2. Claim (1~2문장)

3. Evidence (70~75%)

4. Counterpoint (200~400 words)
   → "왜 이게 틀릴 수 있는가" + 반증 조건 1~2개

5. Prediction Scorecard + So-what Tool (300~500 words)

6. Closing Hook (1~2문단)
```

### 파트별 변주

```
Part I  (Ch1~2):  Scene+Claim에 무게. 프레임 설정.
Part II (Ch3~6):  Evidence에 무게. 차트/표 밀도 높음.
Part III(Ch7~10): Scene에 무게. 인물 밀도 최대.
Part IV (Ch11~12): Evidence+Counterpoint에 무게. 정책/지정학.
Part V  (Ch13~14): Counterpoint에 무게. "What Would Change My Mind" 종합.
```

---

## 4) Iterative Execution (별도 원칙)

컨텍스트 윈도우 한계로 인해 반드시 준수:

1. **챕터별 1장씩 순회.** 한 번에 14장 금지.
2. **순서:** Ch1 → Ch8 (핵심 2장 먼저) → Ch3~7 → Ch9~14
3. **STORY-BIBLE.md:** 각 챕터 완료 후 업데이트. 다음 챕터 시작 전 반드시 로드.

### docs/STORY-BIBLE.md 형식
```markdown
## Ch1
- 등장인물: [이름, 역할, 출처]
- 핵심 인용: [인용 1줄 요약]
- Closing hook: [다음 챕터로 넘긴 질문]
- 미해결: [callback 필요한 서사 요소]

## Ch8
...
```

---

## 5) Anti-Hallucination Protocol

### 절대 규칙
1. 인물/장면/인용 추가 시 반드시 웹 검색으로 실재 확인
2. 실명 불가 시 "출처 있는 익명" (매체명+날짜 필수)
3. 이름, 인용구, 사건을 절대 지어내지 않는다
4. 충분한 검색 후에도 출처 못 찾으면:
   `[TODO: HUMAN-RESEARCH-REQUIRED]` 삽입 후 다음 챕터로
5. 검증 주석 형식:
   `<!-- PROOF: url=원본URL | archive=archive.org/... | accessed=YYYY-MM-DD | key=citation_key -->`
   (archive는 있으면 병기, 없어도 FAIL 아님)

---

## 6) 2축 출처 정책

### Core Claim 정의 (자동 게이트 대상)
숫자, 날짜, 벤치마크, 릴리즈, 밸류에이션, 시장점유율,
정책/규제, 수출통제, 고용/해고 통계

### Tier (신뢰도)
- Tier-1: 공식, 원 논문, 정부, Reuters/Bloomberg/WSJ/FT/Fortune/NYT
- Tier-2: TechCrunch, The Information, Semafor, Stanford HAI
- Tier-3: Wikipedia, SEO, 집계 — **core claim 금지**

### Type (원천성)
- Primary: 당사자 발언/데이터/논문/공식 발표
- Secondary: Primary를 인용/분석한 보도
- Tertiary: 집계/요약

### 규칙
- Core claim → (Tier-1) AND (Primary OR Secondary)
- 맥락 → Tier-2 허용 + Primary practitioner 허용
- Tier-3 → core claim에서 0건
- 2차 출처 인용 시: 원문을 직접 인용하는 2차만 허용

### source-registry.yml 스키마
```yaml
citations:
  cherny-fortune-2026:
    tier: 1
    type: primary
    scope: core
    paywalled: no
    url: "https://fortune.com/2026/01/29/..."
    archive_url: ""
    notes: "Cherny direct quote on 100% AI coding"
```

### Paywall 규칙
paywalled=yes인 core claim은 반드시 비페이월 1차 출처(공식/정부/원보고서) 링크를 병기.

---

## 7) 인용 분량 규칙 (Quote Hygiene)

출처 품질뿐 아니라 인용 분량의 저작권 리스크도 관리:

- 직접 인용(blockquote) 1건당 **25단어 이하**
- 동일 출처에서 총 **200단어 이하**
- Shumer 에세이: 핵심 2~3문장만 직접 인용, 나머지 패러프레이즈
- `scripts/quote_audit.py`가 초과 시 FAIL

---

## 8) 글쓰기 스타일

### AI 금지어
```
delve, moreover, furthermore, it is worth noting, it is important to consider,
robust, comprehensive, crucial, landscape, navigate, leverage, multifaceted,
tapestry, serves as a testament, in the ever-evolving, pivotal, underscore,
nuanced, paradigm shift, at the heart of, in an era where, vibrant
```

### 패턴 금지 (챕터 내 2회 이상)
```
"X was not merely Y. It was Z."
"The implication was stark/sharp/clear."
"This was not X. This was Y."
```

### 필수
- burstiness stdev > 8
- 축약형, 불완전 문장
- 분량 확장 = 장면/인물/도구로. 분석 추가 금지.

---

## 9) 포맷팅

### print-kdp
```yaml
format:
  pdf:
    documentclass: scrbook
    classoption: [openany]
    pdf-engine: lualatex
    papersize: [6in, 9in]
    fontsize: 11pt
    linestretch: 1.2
    indent: true
    geometry:
      - inner=0.55in
      - outer=0.45in
      - top=0.60in
      - bottom=0.70in
    include-in-header:
      - templates/print-header.tex
    fig-pos: 'H'
```

### templates/print-header.tex
```latex
\usepackage{fontspec}
\setmainfont{TeX Gyre Pagella}
\usepackage{float}
\usepackage{microtype}          % 자간 미세 조정
\usepackage{xurl}               % 긴 URL 안전 줄바꿈
\clubpenalty=10000              % 고아줄 방지
\widowpenalty=10000             % 과부줄 방지
\setlength{\textfloatsep}{8pt plus 2pt minus 2pt}
\setlength{\intextsep}{6pt plus 2pt minus 2pt}
\setlength{\floatsep}{6pt plus 2pt minus 2pt}
```

### KDP 파일 위생
- crop marks, annotations 금지. ≤650MB. 폰트 임베딩. 300DPI+.
- 차트 선 두께 0.75pt 이상. 인쇄판 큰 면적 배경색 금지.
- MOBI 사용 금지 (2025년 이후 미수용). EPUB이 기준.

---

## 10) 자동 검증 게이트

### 스크립트 6개
1. `verify_counts.py` — CSV↔본문 수치 동기화
2. `source_audit.py` — 2축 분류, core+Tier-3 → FAIL
3. `voice_audit.py` — 금지어, 패턴, burstiness
4. `image_dpi_check.py` — 실효 DPI < 300 → FAIL
5. `quote_audit.py` — 25단어/건, 200단어/출처 초과 → FAIL
6. `preflight_kdp.sh` — marks, annotations, 650MB, 폰트, 빈 페이지 탐지

### CI 2단계
```
PR:  verify_counts + source_audit + voice_audit + quote_audit + render web
Tag: 위 전부 + image_dpi + EPUB + PDF + preflight + epubcheck
```

---

## 11) 실행 계획

### Phase 0: 인프라 (1~2일)
```
1. docs/ 생성: SSOT.md, SOURCE-POLICY.md, FORMAT-SPECS.md, VOICE-STYLEGUIDE.md
2. docs/STORY-BIBLE.md 초기화
3. references/source-registry.yml 생성
4. scripts/ 6개 스크립트 작성
5. templates/print-header.tex (microtype+xurl+widow/orphan 포함)
6. _quarto.yml + 3개 프로필 (web/ebook/print-kdp)
7. 기준선 측정 → reports/baseline.json
```

### Phase 1: 출처 품질 (3~5일)
```
source_audit.py EXIT 0 달성.
Tier-3 core claim 교체. Ch12 → 20+ citations.
```

### Phase 2: 서사 강화 (5~8일)
```
80K~85K 달성. 6단계 블루프린트 전 챕터 적용.
챕터별 1장씩 순회. STORY-BIBLE 매 챕터 후 업데이트.
```

### Phase 3: 글쓰기 품질 (3~5일)
```
voice_audit.py + quote_audit.py EXIT 0 달성.
```

### Phase 4: 포맷팅 (2~3일)
```
PDF 190~210p, 380+ w/p. EPUB epubcheck 통과.
image_dpi + preflight 통과.
```

### Phase 5: 릴리즈 (1일)
```
전체 게이트 통과 → tag v1.0
```

### Phase 6: Living Update (분기별)
```
evidence-delta-vX.md 생성: scorecard 변화 + 핵심 근거.
changelog + verify_counts 업데이트.
```

---

## 12) 완료 체크리스트 (20항목)

| # | 기준 | 목표 |
|---|------|------|
| 1 | verify_counts.py | EXIT 0 |
| 2 | source_audit.py | EXIT 0 |
| 3 | voice_audit.py | EXIT 0 |
| 4 | image_dpi_check.py | EXIT 0 |
| 5 | quote_audit.py | EXIT 0 |
| 6 | preflight_kdp.sh | EXIT 0 |
| 7 | epubcheck | 0 errors |
| 8 | Kindle Previewer | 통과 |
| 9 | 총 단어 | 80K~85K |
| 10 | PDF 페이지 | 190~210 |
| 11 | Words/page | 380+ |
| 12 | 챕터 번호 | 1~14 정확 |
| 13 | Ch12 citations | 20+ |
| 14 | 챕터당 인물 | 최소 1명 |
| 15 | 챕터당 Counterpoint | 모든 챕터 |
| 16 | 챕터당 Scorecard+Tool | 모든 챕터 |
| 17 | Confirmation Gap | Ch1, Ch8, Ch14 |
| 18 | What Would Change My Mind | Ch14 |
| 19 | 오프닝 장면 | 사람+장소+순간 |
| 20 | 차트 선 두께 | 0.75pt+ |

---

## 13) 반복 규칙

1. 이 문서는 SSOT.
2. Phase 순서 준수. 이전 미완료 시 다음 불가.
3. 6개 스크립트 + epubcheck 모두 EXIT 0까지 반복.
4. 각 Phase 후 REVIEW-REPORT 작성.
5. 새 핵심 주장에 Tier-1 + (Primary OR Secondary) 필수.
6. 인물 추가 시 웹 검색 + PROOF 주석. 못 찾으면 TODO.
7. 분량 확장 = 장면/인물/도구. 분석 추가 금지.
8. Counterpoint는 모든 챕터 필수.
9. 챕터 수정은 1장씩. STORY-BIBLE 매번 업데이트.
10. Phase 내에서 gate fail → stderr 읽고 자가 수정 후 재실행.
    Phase 완료 후 → REVIEW-REPORT 작성.
