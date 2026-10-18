from PIL import Image
import numpy as np
img = Image.open("your_image.jpg")
gamma = 1.5 
inv_gamma = 1.0 / gamma
table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
img = img.point(table * 3)
img.save("gamma_output.jpg")