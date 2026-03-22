{\rtf1\ansi\ansicpg1252\cocoartf2867
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;\f1\froman\fcharset0 Times-Roman;\f2\fmodern\fcharset0 Courier;
\f3\froman\fcharset0 Times-Bold;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;\red109\green109\blue109;
}
{\*\expandedcolortbl;;\cssrgb\c0\c1\c1;\cssrgb\c100000\c100000\c99985;\cssrgb\c50251\c50251\c50189;
}
{\*\listtable{\list\listtemplateid1\listhybrid{\listlevel\levelnfc23\levelnfcn23\leveljc0\leveljcn0\levelfollow0\levelstartat0\levelspace360\levelindent0{\*\levelmarker \{disc\}}{\leveltext\leveltemplateid1\'01\uc0\u8226 ;}{\levelnumbers;}\fi-360\li720\lin720 }{\listname ;}\listid1}}
{\*\listoverridetable{\listoverride\listid1\listoverridecount0\ls1}}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # Movie Recommendation System\
\
## Overview\
This project is a full-stack movie recommendation system that suggests movies based on content similarity. It integrates a machine learning model with a Django web application and displays results with movie posters using the TMDB API.\
\
---\
\
## Features\
- Search movies by name  \
- Content-based recommendations  \
- Movie posters via TMDB API  \
- Fast results using cosine similarity  \
- Web interface built with Django  \
\
---\
\
## Tech Stack\
- Backend: Django  \
- Machine Learning: Pandas, NumPy, Scikit-learn  \
- Frontend: HTML, CSS, Bootstrap  \
- API: TMDB  \
\
---\
\
## How It Works\
- Movie data is processed and combined into text features  \
- Text is converted into vectors using CountVectorizer  \
- Cosine similarity is used to find similar movies  \
- Top recommendations are displayed to the user  \
\
---\
\
## Setup\
\
```bash\
git clone <your-repo-url>\
cd movie-recommender\
python -m venv venv\
source venv/bin/activate\
pip install -r requirements.txt\
\
# Movie Recommendation System\
\
## Overview\
This project is a full-stack movie recommendation system that suggests movies based on content similarity. It integrates a machine learning model with a Django web application and displays results with movie posters using the TMDB API.\
\
---\
\
## Features\
- Search movies by name  \
- Content-based recommendations  \
- Movie posters via TMDB API  \
- Fast results using cosine similarity  \
- Web interface built with Django  \
\
---\
\
## Tech Stack\
- Backend: Django  \
- Machine Learning: Pandas, NumPy, Scikit-learn  \
- Frontend: HTML, CSS, Bootstrap  \
- API: TMDB  \
\
---\
\
## How It Works\
- Movie data is processed and combined into text features  \
- Text is converted into vectors using CountVectorizer  \
- Cosine similarity is used to find similar movies  \
- Top recommendations are displayed to the user  \
\
---\
\
## Setup\
\
```bash\
git clone <your-repo-url>\
cd movie-recommender\
python -m venv venv\
source venv/bin/activate\
pip install -r requirements.txt\
\
# Movie Recommendation System\
\
## Overview\
This project is a full-stack movie recommendation system that suggests movies based on content similarity. It integrates a machine learning model with a Django web application and displays results with movie posters using the TMDB API.\
\
---\
\
## Features\
- Search movies by name  \
- Content-based recommendations  \
- Movie posters via TMDB API  \
- Fast results using cosine similarity  \
- Web interface built with Django  \
\
---\
\
## Tech Stack\
- Backend: Django  \
- Machine Learning: Pandas, NumPy, Scikit-learn  \
- Frontend: HTML, CSS, Bootstrap  \
- API: TMDB  \
\
---\
\
## How It Works\
- Movie data is processed and combined into text features  \
- Text is converted into vectors using CountVectorizer  \
- Cosine similarity is used to find similar movies  \
- Top recommendations are displayed to the user  \
\
---\
\
## Setup\
\
```bash\
git clone <your-repo-url>\
cd movie-recommender\
python -m venv venv\
source venv/bin/activate\
pip install -r requirements.txt\
\
\pard\pardeftab720\sa240\partightenfactor0

\f1 \cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 Create 
\f2\fs26 \cf2 \strokec3 .env
\f1\fs24 \cf2 \strokec3  file: 
\f2\fs26 \cf2 \strokec3 TMDB_API_KEY=your_api_key_here\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec3 \
\pard\pardeftab720\sa240\partightenfactor0

\f1\fs24 \cf2 \strokec3 Run the app:
\f2\fs26 \cf2 \strokec3 \
\pard\pardeftab720\partightenfactor0
\cf2 \strokec3 cd webapp\
python manage.py runserver\
\
\pard\pardeftab720\sa240\partightenfactor0

\f1\fs24 \cf2 \strokec3 Open: 
\f2\fs26 \cf2 \strokec3 http://127.0.0.1:8000/\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec3 \
\pard\pardeftab720\partightenfactor0

\f1\fs24 \cf2 \strokec4 \
\pard\pardeftab720\sa298\partightenfactor0

\f3\b\fs36 \cf2 \strokec3 Future Improvements\
\pard\tx220\tx720\pardeftab720\li720\fi-720\partightenfactor0
\ls1\ilvl0
\f1\b0\fs24 \cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 Hybrid recommendation system\
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 User-based personalization\
\ls1\ilvl0\cf2 \kerning1\expnd0\expndtw0 \outl0\strokewidth0 {\listtext	\uc0\u8226 	}\cf2 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec3 Deployment\
\pard\pardeftab720\partightenfactor0
\cf2 \strokec4 \
\pard\pardeftab720\sa298\partightenfactor0

\f3\b\fs36 \cf2 \strokec3 Author\
\pard\pardeftab720\sa240\partightenfactor0

\f1\b0\fs24 \cf2 \strokec3 Yashvi Rajiv Vyas\
}