import torch
from torch import nn # nn contains all of PyTorch's building blocks for neural networks

# Setup device agnostic code
device = "cuda" if torch.cuda.is_available() else "cpu"
print(f"Using device: {device}")

model = nn.Sequential(
    nn.Linear(in_features=5, out_features=10),
    nn.Linear(in_features=10, out_features=10),
    nn.ReLU(),
    nn.Linear(in_features=10, out_features=1),
    nn.Sigmoid(),
).to(device)

# Create loss function
loss_fn = nn.BCEWithLogitsLoss ()
X_train = torch.Tensor([[0, 0, 0, 0, 1], [0, 0, 0, 1, 1], [0, 0, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
# Create optimizer
optimizer = torch.optim.SGD(params=model.parameters(), lr=0.001)

# Set the number of epochs (aka. number of iterations through the training data)
epochs = 1000 

for epoch in range(epochs):
    model.train()

    y_pred = model(X_train)

    loss = loss_fn(y_pred, y_train)

    optimizer.zero_grad()

    loss.backward()

    optimizer.step()

    model.eval()
    with torch.inference_mode():
        test_pred = model(X_test)
    
        test_loss = loss_fn(test_pred, y_test)

    if epoch % 100 == 0:
        print(f"Epoch: {epoch} | Train loss: {loss} | Test loss: {test_loss}")