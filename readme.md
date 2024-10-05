# Image to Sketch Converter

A simple web application that convert an image into a sketch using OpenCV and Streamlit.
[project link](https://imagetosketch-aashish.streamlit.app/)
## Feature
- Upload an image ('jpg','jpeg', or 'png' formats supported)
- Converts the uploaded image into a pencil sketch
- Displays both the original image and the converted image
- download the converted sketch as a PNG file

## Built With

- [OpenCV](https://opencv.org/) - Used for image processing
- [Streamlit](https://streamlit.io/) - Fast and easy to create a web app
- [Pillow](https://python-pillow.org/) - Image manipulation library

## Installation

To run the project locally, follow these steps:
1. **Clone the repository**
```bash
git clone https://github.com/Aashish-kushwaha/image_to_sketch.git

cd image_to_sketch
```

2. **Create and activate a virtual environment**
```bash
python -m venv myenv
source myenv/bin/activate  # On Windows: myenv\Scripts\activate
```

3. **Install the required dependencies**
```bash
pip install -r requirements.txt
```
4. **Run the Streamlit app**
```bash
streamlit run app.py
```
