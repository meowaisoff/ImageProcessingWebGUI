# import the frameworks, packages and libraries 
import streamlit as st 
from PIL import Image , ImageEnhance, ImageFilter, ImageOps
from io import BytesIO 
import numpy as np 
import cv2 # computer vision 

# function to convert an image to a 
# water color sketch 
def convertto_watercolorsketch(inp_img): 
	img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8) 
	img_water_color = cv2.stylization(img_1, sigma_s=100, sigma_r=0.5) 
	return(img_water_color) 

# function to convert an image to a pencil sketch 
def pencilsketch(inp_img): 
	img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch( 
		inp_img, sigma_s=50, sigma_r=0.07, shade_factor=0.0825) 
	return(img_pencil_sketch) 


# function to load an image 
def load_an_image(image): 
	img = Image.open(image) 
	return img 

# the main function which has the code for 
# the web application 
def main(): 
	
	# basic heading and titles 
	st.title('WEB APPLICATION TO CONVERT IMAGE') 
	st.write("This is an application developed for converting your ***image***") 
	st.subheader("Please Upload your image") 
	
	# image file uploader 
	image_file = st.file_uploader("Upload Images", type=["png", "jpg", "jpeg"]) 

	# if the image is uploaded then execute these 
	# lines of code 
	if image_file is not None: 
		
		# select box (drop down to choose between water 
		# color / pencil sketch) 
		option = st.selectbox('How would you like to convert the image', 
							('Convert to water color sketch', 
							'Convert to pencil sketch', 'Brighten Image', 'Contrast Image', 'Sharpen Image', 'Gaussian Blur', 'Laplacian Filter', 'Equalize Image')) 
		
		if option == 'Convert to water color sketch': 
			image = Image.open(image_file) 
			final_sketch = convertto_watercolorsketch(np.array(image)) 
			im_pil = Image.fromarray(final_sketch) 

			# two columns to display the original image and the 
			# image after applying water color sketching effect 
			col1, col2 = st.columns(2) 
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Water Color Sketch") 
				st.image(im_pil, width=250) 
				buf = BytesIO() 
				img = im_pil 
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="watercolorsketch.png", 
					mime="image/png"
				) 

		if option == 'Convert to pencil sketch': 
			image = Image.open(image_file) 
			final_sketch = pencilsketch(np.array(image)) 
			im_pil = Image.fromarray(final_sketch) 
			
			# two columns to display the original image 
			# and the image after applying 
			# pencil sketching effect 
			col1, col2 = st.columns(2) 
			with col1: 
				st.header("Original Image") 
				st.image(load_an_image(image_file), width=250) 

			with col2: 
				st.header("Pencil Sketch") 
				st.image(im_pil, width=250) 
				buf = BytesIO() 
				img = im_pil 
				img.save(buf, format="JPEG") 
				byte_im = buf.getvalue() 
				st.download_button( 
					label="Download image", 
					data=byte_im, 
					file_name="watercolorsketch.png", 
					mime="image/png"
				) 
		if option == 'Brighten Image': 
			image = Image.open(image_file) 
		
			curr_bri = ImageEnhance.Brightness(image)
			new_bri = 2.5
  			# Brightness enhanced by a factor of 2.5 
			brightened_image = curr_bri.enhance(new_bri) 
			
			# two columns to display the original image and the 
			# image after applying sharpen your image 
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
				
		if option == 'Contrast Image':
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
			
		if option == 'Sharpen Image':
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
				
		if option == 'Gaussian Blur':
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
				
		if option == 'Laplacian Filter':
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
				
		if option == 'Equalize Image':
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
			
			
		

if __name__ == '__main__': 
	main() 
