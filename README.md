# Personal Portfolio

A responsive recruiter-friendly portfolio for M. Yuvashankar, built with Flask, semantic HTML, CSS, and vanilla JavaScript.

## Features

- Responsive portfolio layout with hero, about, education, skills, projects, experience, certifications, and contact sections
- Mobile navigation, active section highlighting, scroll reveals, back-to-top control, and accessible form labels
- Flask contact route with basic server-side validation
- Resume download route and media placeholders
- Environment-based configuration with `.env`
- Project cards are ready to link directly to GitHub repositories when project details are added

## Technologies Used

Python, Flask, HTML5, CSS3, JavaScript, Font Awesome, Google Fonts.

## Project Structure

```text
portfolio/
├── app.py
├── config.py
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
├── README.md
├── static/
│   ├── css/style.css
│   ├── js/script.js
│   ├── images/
│   │   ├── profile.jpg          # add later
│   │   ├── projects/            # add project images
│   │   └── certificates/        # add certificate images
│   └── resume/resume.pdf        # add later
└── templates/
    ├── base.html
    ├── index.html
    ├── 404.html
    └── 500.html
```

## Installation

Create and activate a virtual environment on Windows, then install the dependencies from `requirements.txt`.

Run the application with `python app.py` and open `http://127.0.0.1:5000` in your browser.

## Customization

1. Add your profile image at `static/images/profile.jpg`.
2. Add your resume at `static/resume/resume.pdf`.
3. Replace the project placeholder in `templates/index.html` with project cards containing descriptions and GitHub URLs.
4. Add GitHub, LinkedIn, and other social URLs in `templates/index.html`.
5. Add skills, internships, certifications, achievements, and project data extracted from your resume.
6. Keep credentials in `.env`; never commit `.env` to Git.

## Email configuration

The contact route validates and logs submissions initially. SMTP delivery can be connected using `EMAIL_HOST`, `EMAIL_PORT`, `EMAIL_USERNAME`, `EMAIL_PASSWORD`, and `EMAIL_RECEIVER` in `.env` without hard-coding credentials.

## Deployment

Use a production WSGI server such as Gunicorn on a Linux host, or deploy to a Flask-compatible platform. Set environment variables securely in the hosting provider and disable debug mode in production.
