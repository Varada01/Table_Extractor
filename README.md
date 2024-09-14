# Table Extractor

This project uses the GPT-4 API to extract and process contents from images of tables in the correct order. It provides a web interface for uploading and processing table images.

## Setup

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```
3. Install Tesseract OCR on your system (https://github.com/tesseract-ocr/tesseract)
4. Create a `.env` file in the root directory with your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Usage

To run the web interface:

1. Navigate to the project directory
2. Run the Flask app:
   ```
   python src/app.py
   ```
3. Open a web browser and go to `http://localhost:5000`
4. Use the web interface to upload an image of a table and see the extracted contents

## Testing

Run the tests using:

```
python -m unittest discover tests
```

## License

This project is licensed under the MIT License.