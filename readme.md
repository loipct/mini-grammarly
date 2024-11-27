
Download the [weight file](https://drive.google.com/file/d/1-B9sWiuJLgwAbP63WT22s0LWaD5rEoU7/view?usp=sharing) and put it into [app/ai/models](app\ai\models)

## Usage

1. Create pythonn env: 
```
python -m venv venv
```
3. Install Requirements:
```
venv\Scripts\activate
python -m pip install -r requirements.txt
```
4. Run the FastAPI server:
```
uvicorn app.main:app --reload
```
5. View the Swagger Docs: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

