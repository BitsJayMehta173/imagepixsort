# Using Image to sort the array for recognisation of partnership model where even with parallel process and GPU rendering can sort out the array utilizing the common process two different process combines together in this method where one is processing the image just like in games where he needs to do the analysis which makes uses of the images and this algorithm utilizes it

# for now we have seen the algorithm 10 times slower than the inbuilt sorting method present in the python
# but as two jobs are done with energy used by one it is beneficial
from PIL import Image
import time
import numpy as np


width, height = 800, 1

white_image = Image.new('RGB', (width, height), color='white')
image_array = np.array(white_image)


arr=[]
for j in range(0,10000):
    for i in range(0,700):
        arr.append(i)
arr1=arr
start_t=time.time()

arr=sorted(arr)
end_t=time.time()

print(end_t-start_t)

# new_color = (255, 0, 0)
start_t=time.time()

for x in arr1:
    # print(x)
    y=x
    image_array[0, x] = (244, 0, y%256)
end_t=time.time()
modified_image = Image.fromarray(image_array)
print(end_t-start_t)
# Save the image or show it
modified_image.show()  # To display the image
modified_image.save('modified_image.png')  # To save the image