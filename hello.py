import torch
import torch.nn as nn

# CUDA가 사용할 수 있는지 확인
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# 간단한 CNN 모델 정의
class SimpleCNN(nn.Module):
    def __init__(self):
        super(SimpleCNN, self).__init__()
        self.conv1 = nn.Conv2d(1, 32, kernel_size=3, stride=1, padding=1)  # cuDNN 사용
        self.pool = nn.MaxPool2d(kernel_size=2, stride=2, padding=0)
        self.fc1 = nn.Linear(32 * 14 * 14, 10)

    def forward(self, x):
        x = self.pool(torch.relu(self.conv1(x)))
        x = x.view(-1, 32 * 14 * 14)
        x = self.fc1(x)
        return x

# 모델과 텐서 준비
model = SimpleCNN().to(device)
input_tensor = torch.randn(1, 1, 28, 28).to(device)  # 가짜 이미지 텐서 (28x28 크기)

# 모델 실행
output = model(input_tensor)

print("Output shape:", output.shape)
