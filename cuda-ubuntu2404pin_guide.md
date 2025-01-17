# pin 파일
.pin 파일을 /etc/apt/preferences.d/와 같은 적절한 시스템 디렉토리에 두어야 합니다. 이렇게 하면, 시스템 전체에서 해당 CUDA 버전이 고정됩니다.

다른 라이브러리나 패키지가 설치되면, 의존성 문제로 CUDA나 cuDNN의 버전이 바뀌기도 합니다. 예를 들어, 다른 라이브러리가 더 높은 버전의 CUDA나 cuDNN을 요구할 수 있습니다.

# pin 파일 위치 저장
sudo cp cuda-ubuntu2404.pin.1 /etc/apt/preferences.d/cuda-ubuntu2404.pin
# 버전 고정 확인
apt-cache policy cuda

dpkg -l | grep cuda

dpkg -l | grep cudnn

# 고정된 버전으로 업데이트 차단
sudo apt-mark hold cuda cudnn

위 방법으로 차단되긴 하는데 오류 뜸.

sudo mv /etc/apt/preferences.d/cuda-ubuntu2404.pin /etc/apt/preferences.d/cuda-ubuntu2404.pref

위 명령어로 .pref로 변경
# 업데이트 차단 해제제
sudo apt-mark unhold cuda cudnn