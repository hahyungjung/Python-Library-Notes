# Python-Library-Notes



### [TensorFlow]

	[TensorFlow Basic]

	- [Basic](03%20-%20TensorFlow%20Basic/01%20-%20Basic.py)
  		- 텐서플로우의 연산의 개념과 그래프를 실행하는 방법을 익힙니다.
	- [Variable](03%20-%20TensorFlow%20Basic/02%20-%20Variable.py)
  		- 텐서플로우의 플레이스홀더와 변수의 개념을 익힙니다.
	- [Linear Regression](03%20-%20TensorFlow%20Basic/03%20-%20Linear%20Regression.py)
  		- 단순한 선형 회귀 모형을 만들어봅니다.

	[Neural Network Basic](04%20-%20Neural%20Network%20Basic)

	- [Classification](04%20-%20Neural%20Network%20Basic/01%20-%20Classification.py)
	  - 신경망을 구성하여 간단한 분류 모델을 만들어봅니다.
	- [Deep NN](04%20-%20Neural%20Network%20Basic/02%20-%20Deep%20NN.py)
	  - 여러개의 신경망을 구성하는 방법을 익혀봅니다.
	- [Word2Vec](04%20-%20Neural%20Network%20Basic/03%20-%20Word2Vec.py)
	  - 자연어 분석에 매우 중요하게 사용되는 Word2Vec 모델을 간단하게 구현해봅니다.

	[TensorBoard, Saver](05%20-%20TensorBoard,%20Saver)

	- [Saver](05%20-%20TensorBoard,%20Saver/01%20-%20Saver.py)
	  - 학습시킨 모델을 저장하고 재사용하는 방법을 배워봅니다.
	- [TensorBoard](05%20-%20TensorBoard,%20Saver/02%20-%20TensorBoard.py)
	  - 텐서보드를 이용해 신경망의 구성과 손실값의 변화를 시각적으로 확인해봅니다.
	- [TensorBoard #2](05%20-%20TensorBoard,%20Saver/03%20-%20TensorBoard2.py)
	  - 텐서보드에 히스토그램을 추가해봅니다.

	[MNIST](06%20-%20MNIST)

	- [MNIST](06%20-%20MNIST/01%20-%20MNIST.py)
	  - 머신러닝 학습의 Hello World 와 같은 MNIST(손글씨 숫자 인식) 문제를 신경망으로 풀어봅니다.
	- [Dropout](06%20-%20MNIST/02%20-%20Dropout.py)
	  - 과적합 방지를 위해 많이 사용되는 Dropout 기법을 사용해봅니다.

	[CNN](07%20-%20CNN)

	- [CNN](07%20-%20CNN/01%20-%20CNN.py)
	  - 이미지 처리 분야에서 가장 유명한 신경망 모델인 CNN 을 이용하여 더 높은 인식률을 만들어봅니다.
	- [tf.layers](07%20-%20CNN/02%20-%20tf.layers.py)
	  - 신경망 구성을 손쉽게 해 주는 High level API 인 layers 를 사용해봅니다.

	[Autoencoder](08%20-%20Autoencoder)

	- [Autoencoder](08%20-%20Autoencoder/01%20-%20Autoencoder.py)
	  - 대표적인 비감독(Unsupervised) 학습 방법인 Autoencoder 를 사용해봅니다.

	[GAN](09%20-%20GAN)

	- [GAN](09%20-%20GAN/01%20-%20GAN.py)
	  - 2016년에 가장 관심을 많이 받았던 비감독 학습 방법인 GAN 을 구현해봅니다.
	- [GAN #2](09%20-%20GAN/02%20-%20GAN2.py)
	  - GAN 을 응용하여 원하는 숫자의 손글씨 이미지를 생성하는 모델을 만들어봅니다. 이런 방식으로 흑백 사진을 컬러로 만든다든가, 또는 선화를 채색한다든가 하는 응용이 가능합니다.

	[RNN](10%20-%20RNN)

	- [01 - MNIST](10%20-%20RNN/01%20-%20MNIST.py)
	  - 자연어 처리나 음성 처리 분야에 많이 사용되는 RNN 의 기본적인 사용법을 익힙니다.
	- [02 - Autocomplete](10%20-%20RNN/02%20-%20Autocomplete.py)
	  - 순서가 있는 데이터에 강한 RNN 특징을 이용해, 단어 중 첫 세글자를 주면 단어를 완성하는 모델을 구현해봅니다.
	- [03 - Seq2Seq](10%20-%20RNN/03%20-%20Seq2Seq.py)
	  - 챗봇, 번역, 이미지 캡셔닝등에 사용되는 시퀀스 학습/생성 모델인 Seq2Seq 을 구현해봅니다.
	- [Chatbot](10%20-%20RNN/ChatBot)
	  - Seq2Seq 모델을 이용해 간단한 챗봇을 만들어봅니다.

	[Inception](11%20-%20Inception)

	구글에서 개발한 이미지 인식에 매우 뛰어난 신경망 모델인 Inception 을 사용해봅니다.

	신경망 모델을 직접 구현할 필요 없이, 간단한 스크립트 작성만으로 자신만의 데이터를 이용해 매우 뛰어난 인식률을 가진 프로그램을 곧바로 실무에 적용할 수 있습니다.

	자세한 내용은 [11 - Inception/README.md](11%20-%20Inception/README.md) 문서를 참고 해 주세요.

	[DQN](12%20-%20DQN)

	알파고로 유명한 구글의 딥마인드에서 개발한 딥러닝을 이용한 강화학습인 DQN 을 구현해봅니다.

	조금 복잡해보이지만, 핵심적인 부분을 최대한 분리해두었으니 충분히 따라가실 수 있을 것 입니다.

	자세한 내용은 [12 - DQN/README.md](12%20-%20DQN/README.md) 문서를 참고 해 주세요.

	## 참고

	조금 더 기초적인 이론에 대한 내용은 다음 강좌와 저장소를 참고하세요.

	- [모두를 위한 머신러닝/딥러닝 강의](https://www.youtube.com/watch?v=BS6O0zOGX4E&list=PLlMkM4tgfjnLSOjrEJN31gZATbcj_MpUm) (홍콩 과기대 김성훈 교수님 강좌)
	- [강좌 실습 코드](https://github.com/golbin/TensorFlow-ML-Exercises) (내가 만듬)

	Troubleshooting

	- Mac OS에서 matplotlib를 사용하는 코드가 실행이 안되거나 에러가 나는 경우
	  - `~/.matplotlib/matplotlibrc` 파일을 생성하고 `backend: TkAgg` 라는 설정을 추가해 주시면 됩니다.
