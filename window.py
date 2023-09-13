import numpy as np
import matplotlib.image as mpimg
from sklearn.cluster import KMeans
from tkinter import filedialog, ttk
from tkinter import *
from PIL import Image, ImageTk

class User:
    def __init__(self, root):
        self.current_path = ''
        self.converted_image = None
        self.result_image = None

        # Create and configure the main window
        self.root = root
        self.root.title("Color Quantization")
        self.root.geometry("800x520+400+200")

        # Create and configure frames
        frm = ttk.Frame(root, padding=15)
        frm.grid(row=0, column=0, padx=10, pady=10, sticky=(N, S, E, W))

        # Create widgets
        self.filename_path = StringVar()
        self.n_clusters = StringVar()

        path_label = Label(frm, text='Choose an image (in .jpg format)')
        path_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

        path_entry = ttk.Entry(frm, textvariable=self.filename_path, width=50)
        path_entry.grid(row=1, column=0, columnspan=2)

        browse_button = ttk.Button(frm, text="Browse", command=self.getting_path)
        browse_button.grid(row=1, column=2, padx=5)

        cluster_label = Label(frm, text='Number of Clusters:')
        cluster_label.grid(row=2, column=0, pady=(10, 0))

        cluster_entry = ttk.Entry(frm, textvariable=self.n_clusters, width=5)
        cluster_entry.grid(row=2, column=1)

        transform_button = ttk.Button(frm, text="Transform", command=self.color_quantization)
        transform_button.grid(row=2, column=2, padx=5)

        original_label = Label(frm, text="Original Image:")
        original_label.grid(row=3, column=0, pady=10)

        result_label = Label(frm, text="Color-Quantized Image:")
        result_label.grid(row=3, column=1, pady=10)

        frame_images = Frame(frm)
        frame_images.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

        self.original_image_label = Label(frame_images)
        self.original_image_label.grid(row=0, column=0)

        self.result_image_label = Label(frame_images)
        self.result_image_label.grid(row=0, column=1)

        download_button = ttk.Button(frm, text="Download Result", command=self.download_result)
        download_button.grid(row=5, column=0, columnspan=3, pady=10)

    def getting_path(self):
        self.current_path = filedialog.askopenfilename(initialdir="/", title="Select an image",
                                                       filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")))
        self.filename_path.set(self.current_path)

        if Image.open(self.current_path):
            image = Image.open(self.current_path)
            # Resize the image to fit the Label
            resized_image = image.resize((300, 300), Image.LANCZOS)
            self.converted_image = ImageTk.PhotoImage(resized_image)
            self.original_image_label.config(image=self.converted_image)

    def color_quantization(self):
        n_clusters = int(self.n_clusters.get())
        image_df = mpimg.imread(self.current_path)
        h, w, c = image_df.shape
        scaled_image_df = image_df.reshape(h * w, c)
        model = KMeans(n_clusters=n_clusters, n_init=10)
        prediction = model.fit_predict(scaled_image_df)
        rgb_colors = model.cluster_centers_.round(0).astype(int)
        final_image = rgb_colors[prediction]
        answer = np.reshape(final_image, (h, w, c))

        pil_image = Image.fromarray(answer.astype('uint8'))
        # Resize the transformed image to fit the Label
        if h < w:
            resized_image = pil_image.resize((300, 300), Image.LANCZOS)
        else:
            resized_image = pil_image.resize((300, 150), Image.LANCZOS)
        self.result_image = ImageTk.PhotoImage(resized_image)
        self.result_image_label.config(image=self.result_image)
       

    def download_result(self):
        if self.result_image:
            # Save the result image to a file
            file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=(("JPEG files", "*.jpg"), ("All files", "*.*")))
            if file_path:
                self.result_image_label.image.save(file_path)

if __name__ == '__main__':
    root = Tk()
    user = User(root)
    root.mainloop()
