import torch
import torch.nn as nn

# Define the input matrix and the kernel
input_matrix = torch.tensor([[5,1,3,7],[4,6,3,1],[2,5,5,1],[8,7,3,1]], dtype=torch.float).unsqueeze(0).unsqueeze(0)
kernel = torch.tensor([[1,2,1],[2,1,2],[1,2,1]], dtype=torch.float).unsqueeze(0).unsqueeze(0)

# Define the convolution layer
conv_layer = nn.Conv2d(in_channels=1, out_channels=1, kernel_size=3, stride=1, padding=0)

# Set the weights of the convolution layer to the kernel
conv_layer.weight = nn.Parameter(kernel)

# Perform the convolution operation
output_matrix = conv_layer(input_matrix)

# Convert the output matrix to integers
output_matrix = output_matrix.round().long()

# Print the output matrix
print(output_matrix.squeeze())
