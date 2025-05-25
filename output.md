# Python Programing

Transformer 기반 Bert XSS 공격탐지

# 1922026 송준현

# Xss 공격이란?

![](img%5CBERT%EB%B0%9C%ED%91%9C_0.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_1.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_2.png)

Cross site scripting :

웹브라우저 악성 스크립트를 삽입하여 사용자의 쿠키 또는 민감한정보를 탈취하는 행위

![](img%5CBERT%EB%B0%9C%ED%91%9C_3.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_4.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_5.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_6.png)

Ｉｎｐｕｔ＿ｉｄｓ　：　　토큰화

Ａｔｔｅｎｔｉｏｎ＿ｍａｓｋ　：실제데이터와　패딩값　식별

Ｌａｂｅｌｓ　：　현재　데이터가　공격／안전　코드에대한　정답

![](img%5CBERT%EB%B0%9C%ED%91%9C_7.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_8.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_9.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_10.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_11.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_12.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_13.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_14.png)

![](img%5CBERT%EB%B0%9C%ED%91%9C_15.png)

１개의문장이　１２８개의　토큰（단어）로　이루어짐

Ｃｒｏｓｓ　Ｅｎｔｒｏｐｙ　Ｌｏｓｓ이용

결과　Ｌｏｇｉｔ　확률분포

모델　예측결괴

０번째보다　１번째의　확률값이　더높음

ＸＳＳ　공격　코드　판별

