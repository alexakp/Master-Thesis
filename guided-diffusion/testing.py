# Python program to perform 2D convolution operation on an image
# Import the required libraries
import torch
import torchvision
from PIL import Image
import torchvision.transforms as T

# Read input image
img = Image.open('dogncat.jpg')

# convert the input image to torch tensor
img = T.ToTensor()(img)
print("Input image size:", img.size()) # size = [3, 466, 700]

# unsqueeze the image to make it 4D tensor
img = img.unsqueeze(0) # image size = [1, 3, 466, 700]
# define convolution layer
# conv = nn.Conv2d(in_channels, out_channels, kernel_size)
conv = torch.nn.Conv2d(3, 3, 5,padding='valid')
pool = torch.nn.MaxPool2d(2)


# apply convolution operation on image
img = conv(img)
img = pool(img)
img = conv(img)
img = pool(img)

m = torch.nn.Flatten()
img = m(img)
img.size()
fc = torch.nn.Linear(48, 10)
img = fc(img)

# squeeze image to make it 3D
img = img.squeeze() #now size is again [3, 466, 700]
print(img.size())
print(img)

# convert image to PIL image
#img = T.ToPILImage()(img)

# display the image after convolution
#img.show()