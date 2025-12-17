from flask import Flask, render_template, request
from ai_solver import solve_physics
from ai_solver import clean_solution
from ocr import extract_text_from_image
from ocr import clean_ocr_text
import markdown

app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def home():
    problem = ""
    solution = ""

    if request.method == "POST":
        problem = request.form.get("problem","").strip()
        image = request.files.get("problem_image")

        if image and image.filename != "":
            problem = extract_text_from_image(image)
            problem = clean_ocr_text(problem)

        if problem:
            print("OCR TEXT:",problem)
            solution = solve_physics(problem)
            solution = clean_solution(solution)
            solution = markdown.markdown(solution)


    return render_template("index.html",problem=problem,solution=solution)

if __name__ == "__main__":
    app.run()
