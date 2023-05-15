# 1. 프로젝트 주제
-	서울시 구별 아파트 매매가격과 교육기관의 상관관계 분석

# 2. 기획의도 및 목표
-	서울시 집값과 교육기관의 관계 분석
-	학원과 서울시 집값 데이터와의 관계 분석
-	학교와 서울시 집값 데이터와의 관계 분석
-	서울시 평형별 아파트 매매가격과 교육기관의 관계 분석
-	서울시 아파트 매매가격과 교육기관의 가장 상관관계가 깊은 관계 분석

# 3. 데이터
-	서울시 구별 2018 ~ 2020 아파트 매매 현황
-	서울시 구별 학교 데이터
-	서울시 구별 학원 데이터
-	서울시 구별 학급당 학생수

# 4. 데이터 시각화
### 서울시 구별 매매 평균
- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/9112ddb8-e660-429c-83d3-8df902aa2d94)

### 서울시 구별 학원과 집값의 관계
- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/2219918d-7c49-4e6e-9fcd-36cc76a8e2e2)

### 지도 시각화
- 서울시 구별 학원수
- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/39894cfd-7d79-4b03-9d7f-a4c866283dad)
- 서울시 구별 매매 평균
- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/bed9bfd2-db12-4810-b5ab-5ded83e0698b)

# 5. 데이터 분석
- 상관계수 그래프
- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/e4ee18a5-6129-4bc0-9ff9-1bb6409ea223)


# 6. 결론 도출
### 결론 1. 서울시 아파트 매매가격 평균과 교육기관의 상관관계
- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/96c7f0e4-4e93-4c50-a63f-894ca9a12e4e)

-	사진은 서울시 평균 아파트 매매가격과 교육기관별 상관계수이며 서울시 아파트 매매가격은 학교수와 상관관계가 없음을 알 수 있으며, 학원과 서울시 아파트 매매가격은 stats.pearsonr 기준 0.699% 상관관계가 있음을 알수있다
-	![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/5815cc92-120c-4cf8-8e9e-5c11991cbb8b)

-	서울시 평균 아파트 매매가격과 학원수가 상관관계가 있음을 알수있었으며, 사진은 학원과 서울시 아파트 구별 매매가격과의 데이터 분포도로 학원 개수가 많아짐에 따라 서울시 아파트 매매가격도 높아짐을 알수있다


### 결론 2. 서울시 아파트 평형별, 평균 금액과 학원의 상관관계

- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/23ddcaf8-9715-49b6-9ff1-cf4113700f65)

-	위 사진은 결론1. 의 결과 학원의 상관계수가 높았기에, 학원 관련된 컬럼과 평형별, 평균 금액과의 상관계수 그래프이다
-	평형별 금액과 평균금액 결과 학생당_학원수가 가장 높은 상관계수를 보였으며,
평형별 가장 높은 상관계수는 중형금액별 학생당_학원수 이다.
- ![image](https://github.com/dkdlel395/DataAnalysis/assets/74848389/8b1c4619-dd9c-4654-a034-6e80c680cbd1)
  
               < 서울시 구별 아파트 매매 평균 지도 >                          < 서울시 구별 학생당_학원수 지도 >

