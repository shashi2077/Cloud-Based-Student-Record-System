from flask import Flask, render_template, request, redirect, url_for, flash
from db_config import get_connection

app = Flask(__name__)
app.secret_key = "change-this-secret-key"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        email = request.form.get("email", "").strip()
        course = request.form.get("course", "").strip()

        if not name or not email or not course:
            flash("All fields are required.", "error")
            return redirect(url_for("add_student"))

        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO students (name, email, course) VALUES (%s, %s, %s)",
                (name, email, course),
            )
            conn.commit()
            flash("Student added successfully ✅", "success")
        except Exception as e:
            flash(f"Error: {e}", "error")
        finally:
            try:
                cursor.close()
                conn.close()
            except Exception:
                pass

        return redirect(url_for("view_students"))

    return render_template("add_student.html")

@app.route("/view")
def view_students():
    students = []
    try:
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM students ORDER BY id DESC")
        students = cursor.fetchall()
    except Exception as e:
        flash(f"Error: {e}", "error")
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass

    return render_template("view_students.html", students=students)

@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
        conn.commit()
        flash("Student deleted.", "success")
    except Exception as e:
        flash(f"Error: {e}", "error")
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass
    return redirect(url_for("view_students"))

if __name__ == "__main__":
    app.run(debug=True)
