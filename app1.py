# import the frameworks, packages and libraries 
import streamlit as st 
from PIL import Image , ImageEnhance, ImageFilter, ImageOps
from io import BytesIO 
import numpy as np 
import cv2 # computer vision 
import imageio.v3 as iio
#import ipympl
import matplotlib.pyplot as plt
import skimage as ski

# function to load an image 
def load_an_image(image): 
	img = Image.open(image) 
	return img 

# the main function which has the code for 
# the web application 
def main(): 
	# basic heading and titles 
	st.title('WEB APPLICATION TO CONVERT IMAGE') 
	st.write("Image Processing Web Application using Streamlit") 
	st.write("This is an application developed for converting your ***image***") 
	st.subheader("Please Upload your image") 
	
	# image file uploader 
	image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"]) 

	# if the image is uploaded then execute these 
	# lines of code 
	if image_file is not None: 
		
		# select box (drop down to choose between water 
		# color / pencil sketch) 
		st.subheader("Choose an option") 
		
	
		if st.button('Brighten Image'):
			image = Image.open(image_file) 
			new_bri = 2.5
# 			new_bri = st.number_input("Choose Brightness level")
			curr_bri = ImageEnhance.Brightness(image)
			
  	
			brightened_image = curr_bri.enhance(new_bri) 
			
		
			col1, col2 = st.columns(2) 
			
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Brighten image") 
				st.image(brightened_image, width=250) 
				buf = BytesIO() 
				img = brightened_image
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="brightenimage.png", 
					mime="image/png"
				)
				
		if st.button("Contrast Image"):
			image = Image.open(image_file)
			
			curr_con = ImageEnhance.Contrast(image) 
			new_con = 5
			img_contrasted = curr_con.enhance(new_con)
			
			col1, col2 = st.columns(2) 
			
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Contrast image") 
				st.image(img_contrasted, width=250) 
				buf = BytesIO() 
				img = img_contrasted
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="contrastimage.png", 
					mime="image/png"
				)
			
		if st.button("Sharpen Image"):
			image = Image.open(image_file)
			
			curr_sharp = ImageEnhance.Sharpness(image) 
			new_sharp = 8.3
			img_sharped = curr_sharp.enhance(new_sharp) 
			
			col1, col2 = st.columns(2)
			
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Sharpened image") 
				st.image(img_sharped, width=250) 
				buf = BytesIO() 
				img = img_sharped
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="sharpenedimage.png", 
					mime="image/png"
				)
				
		if st.button("Gaussian Blur"):
			image = Image.open(image_file)
			
			img_gaussian = image.filter(ImageFilter.GaussianBlur(radius = 5))
			
			col1, col2 = st.columns(2)
			
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Gaussian Blur image") 
				st.image(img_gaussian, width=250) 
				buf = BytesIO() 
				img = img_gaussian
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="gaussianblurimage.png", 
					mime="image/png"
				)
				
		if st.button("Laplacian Filter"):
			image = Image.open(image_file)
			image = image.convert("L")		
			image = image.filter(ImageFilter.FIND_EDGES)
		
			col1, col2 = st.columns(2)
			
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Laplacian Filter image") 
				st.image(image, width=250) 
				buf = BytesIO() 
				img = image
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="laplacianfilterimage.png", 
					mime="image/png"
				)
				
		if st.button("Equalize Image"):
			
			im1 = Image.open(image_file)
			
			image = ImageOps.equalize(im1, mask = None)
			
			col1, col2 = st.columns(2)
			
			with col1: 	
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 	
				st.header("Equalized image") 
				st.image(image, width=250) 
				buf = BytesIO() 
				img = image
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="equalizedimage.png", 
					mime="image/png"
				)
			
		if st.button("Gray-scale Histogram"):

			
			plant_seedling = iio.imread(image_file, mode = "L")
			
			
			plant_seedling = ski.util.img_as_float(plant_seedling)
			
			fig, ax = plt.subplots()
			ax.imshow(plant_seedling, cmap="gray")
			
			histogram, bin_edges = np.histogram(plant_seedling, bins=256, range=(0, 1))
			
			fig, ax = plt.subplots()
			ax.set_title("Grayscale Histogram")
			ax.set_xlabel("Grayscale Value")
			ax.set_ylabel("Pixel Count")
			ax.set_xlim([0.0, 1.0])  
			
			ax.plot(bin_edges[0:-1], histogram)  
			
			col1, col2 = st.columns(2)
			
			with col1: 	
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 	
				st.header("Histogram") 
				st.pyplot(fig)
  			
  
		if st.button("RGB Histogram"):
			
			image = iio.imread(image_file)
			
			fig, ax = plt.subplots()
			ax.imshow(image)
 			
			colors = ("red", "green", "blue")
			
			fig, ax = plt.subplots()
			ax.set_xlim([0, 256])
			for channel_id, color in enumerate(colors):
			    histogram, bin_edges = np.histogram(
			        image[:, :, channel_id], bins=256, range=(0, 256)
			    )
			    ax.plot(bin_edges[0:-1], histogram, color=color)
			
			ax.set_title("Color Histogram")
			ax.set_xlabel("Color Value")
			ax.set_ylabel("Pixel Count") 
			
			col1, col2 = st.columns(2)
			
			with col1: 	
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 	
				st.header("Histogram") 
				st.pyplot(fig)
			 

if __name__ == '__main__': 
	main() 
# 	sys.argv = ["streamlit", "run", "app.py"]
# 	sys.exit(stcli.main())
