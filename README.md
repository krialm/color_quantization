# Color Quantization Program

This program allows you to perform color quantization on images in the JPEG format. Color quantization reduces the number of colors in an image while preserving its visual quality. The main features of this program include:

- Load an image: You can select a JPEG image from your computer to apply color quantization.
- Set the number of clusters: You can specify the number of color clusters to quantize the image.
- Transform the image: Apply color quantization to the loaded image and display the result.
- Download the result: Save the color-quantized image to your computer.
<img width="706" alt="Screenshot 2023-10-07 at 22 25 11" src="https://github.com/krialm/color_quantization/assets/93251167/78196c98-7657-4804-a7fb-b50ae365b040">

## Usage

1. **Load an Image**:
   - Click the "Browse" button to select a JPEG image file.
   - The selected image will be displayed in the "Original Image" section.

2. **Set the Number of Clusters**:
   - Enter the desired number of color clusters in the "Number of Clusters" field.
   - This number determines the level of color quantization.

3. **Transform the Image**:
   - Click the "Transform" button to apply color quantization to the loaded image.
   - The color-quantized image will be displayed in the "Color-Quantized Image" section.
   - The program uses the K-Means clustering algorithm to reduce the number of colors.

4. **Download the Result**:
   - After transforming the image, click the "Download Result" button.
   - Choose a location on your computer to save the color-quantized image.

## Dependencies

- Python 3.x
- NumPy
- Matplotlib
- Scikit-learn (for K-Means clustering)
- Tkinter (for the graphical user interface)
- Pillow (PIL) for image handling

## How to Run

1. Make sure you have the required dependencies installed.

2. Run the program by executing the Python script `main.py`.

3. Follow the on-screen instructions to load an image, set the number of clusters, and transform the image.

4. Download the color-quantized result when you're satisfied with the transformation.

5. Explore the code for customization and further development.

## Author

This program was developed by Artem Konotopchyk.

## License

This program is open-source and available for all users.

Feel free to modify, improve, and share this program with others. Happy color quantizing!
