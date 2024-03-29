# Braille Translator

 개발환경 : PyCharm, Visual Studio Code, Arduino IDE

 개발언어 : Python, Arduino, HTML, CSS, JavaScript


## 개발 배경

시각장애인들은 일상생활속에서 많은 어려움을 직면한다. 다음과 같다 

1.점자프린터기에 대한 접근성이 낮다. 시각장애인들이 글을 접해야 할 때 대부분은 점자 출력물이 아니기에 어려움을 겪는다. 그래서 시각장애인들을 위해 점자로 표현 하고 싶어도 주변에 시각장애인이 있지 않는 이상 점자 프린터기가 없어 표현하기 힘든 현실이다. 

2.시중에 시각장애인을 위한 대체자료 제작률은 매우 낮다. 전공책, 일반 서적등 년간 수많은 도서들이 출판되고 있지만 시각장애인에게는 빈 종이나 다름 없다. 시각장애인은 텍스트가 아닌 점자체계로 이루어진 대체제작물이 필요하다. 물론 대체자료도 만들어지고 있다. 하지만 전체 도서의 15%이하로 매우 낮은 수치이다. 

3.일반인들 보다 언어의 장벽이 높다. 점자체계는 한 언어에 따라 만들어진다. 언어가 한국어이면 한국어에 맞는 점자체계가 있고 언어가 영어이면 영어에 맞는 점자체계가 있다. 이말은 즉 한국어 점자체계를 공부해도 영어를 기반으로 만들어진 점자는 읽지 못한다는 것이다. 예를 들어 한국어를 공부하고 싶은 영어권 시각장애인 학생과 영어로 이루어진 전공책을 읽고 싶은 한국인 시각장애인 학생이 있다고 해보자. 영어권 시각장애인 학생은 한국어를 공부하기 위해 일반 학생처럼 영어 → 한국어만 공부하는 것 이 아니라. 영어 → 영어 점자체계 → 한국어 → 한국어 점차체계 식으로 공부해야한다. 또, 한국인 시각장애인 학생은 단순하게 번역을 돌리는 것이 아닌 영어 → 한국어 → 점자체계로 한번더 과정을 거쳐야한다. 


이러한 문제들을 해결하고자 프로젝트를 진행하게 되었다. 
## 코드 구성

2
 
+ app



+ code_3rd

문자열로 들어온 데이터를 유니코드 통해 한글, 영어, 숫자, 기호로 분류한다.

한글은 초성, 중성, 종성으로 나누어 분류한다. 

또, 참조되는 변수들의 값들을 저장한다.


+ dot_data , dot_data_eng

점자 체계를 저장해둔 곳이다.

초성, 중성, 종성, 영어, 숫자, 기호들을 각각 대응하는 점자 규격에 맞추어서 저장해놓은 코드이다.

점자 규격

(1) (4)

(2) (5)

(3) (6)



+ grm

들어온 텍스트를 약자인지 판별하는 코드이다.


+ setup

최종 실행 파일이다. 

결과를 확인하기 위해 실행하는 코드이다. 

+ circuit

통신을 위해 전송할 데이터를 리스트에 저장하는 코드이다.




## 사용 방법(예시)

1. 입력할 언어(한국어, 영어) 와 변역시키고 싶은 언어를 선택한다(한국어, 영어)

2. 입력창에 텍스트를 입력하고 “ Translat “ 버튼을 누른다.

3. 오른쪽 번역창에 번역된 언어가 뜨면 텍스트를 확인하고(수정 가능) “Braille_Print” 버튼을 누른다.

5. 점자체계 변환 및 전송이 완료될 때까지 기다린다. (로딩)

## 이후 발전시킬 부분

1. 유선통신에서 무선통신으로 한다.