from data_organizer import handle_query, load_data, make_frame
from flask import Flask, render_template, request
import os

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=["GET", "POST"])
def home_page():
    # IF forms are submitted
    if request.method == "POST":
        # Checks every single possible query for data
        # Loading the masterlist from the data
        masterlist, toprow = load_data()
        # The left query - forms and sent off
        try:
            # This checks if the left form as submitted at all before
            # forming the left query
            if request.form["left_hidden"] == "left":
                left_query = [None, None, None, None]
                # Years - left
                year_query = []
                try:
                    year_query.append(request.form["left_2016"])
                except:
                    pass
                try:
                    year_query.append(request.form["left_2017"])
                except:
                    pass
                try:
                    year_query.append(request.form["left_2018"])
                except:
                    pass
                try:
                    year_query.append(request.form["left_2019"])
                except:
                    pass
                if year_query:
                    left_query[0] = year_query
                # Months - left
                month_query = []
                try:
                    month_query.append(request.form["left_january"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_february"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_march"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_april"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_may"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_june"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_july"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_august"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_september"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_october"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_november"])
                except:
                    pass
                try:
                    month_query.append(request.form["left_december"])
                except:
                    pass
                if month_query:
                    left_query[1] = month_query
                # Districts - left
                district_query = []
                try:
                    district_query.append(request.form["left_brooklyn_north"])
                except:
                    pass
                try:
                    district_query.append(request.form["left_brooklyn_south"])
                except:
                    pass
                try:
                    district_query.append(request.form["left_bronx"])
                except:
                    pass
                try:
                    district_query.append(request.form["left_manhattan"])
                except:
                    pass
                try:
                    district_query.append(request.form["left_queens_east"])
                except:
                    pass
                try:
                    district_query.append(request.form["left_queens_west"])
                except:
                    pass
                if district_query:
                    left_query[2] = district_query
                try:
                    left_query[3] = request.form["left_sorting"]
                except:
                    raise Exception("No left sorting method for some reason")
                worklist = handle_query(left_query, masterlist)
                make_frame(worklist, "templates/frame_1", toprow)
        except:
            pass
        # The right query - forms and sent off
        try:
            # Same as above here - checks for right query before forming
            if request.form["right_hidden"] == "right":
                right_query = [None, None, None, None]
                # Years - right
                year_query = []
                try:
                    year_query.append(request.form["right_2016"])
                except:
                    pass
                try:
                    year_query.append(request.form["right_2017"])
                except:
                    pass
                try:
                    year_query.append(request.form["right_2018"])
                except:
                    pass
                try:
                    year_query.append(request.form["right_2019"])
                except:
                    pass
                if year_query:
                    right_query[0] = year_query
                # Months - right
                month_query = []
                try:
                    month_query.append(request.form["right_january"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_february"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_march"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_april"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_may"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_june"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_july"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_august"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_september"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_october"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_november"])
                except:
                    pass
                try:
                    month_query.append(request.form["right_december"])
                except:
                    pass
                if month_query:
                    right_query[1] = month_query
                # Districts - right
                district_query = []
                try:
                    district_query.append(request.form["right_brooklyn_north"])
                except:
                    pass
                try:
                    district_query.append(request.form["right_brooklyn_south"])
                except:
                    pass
                try:
                    district_query.append(request.form["right_bronx"])
                except:
                    pass
                try:
                    district_query.append(request.form["right_manhattan"])
                except:
                    pass
                try:
                    district_query.append(request.form["right_queens_east"])
                except:
                    pass
                try:
                    district_query.append(request.form["right_queens_west"])
                except:
                    pass
                if district_query:
                    right_query[2] = district_query
                # Sorting - right
                try:
                    right_query[3] = request.form["right_sorting"]
                except:
                    raise Exception("No right sorting method for some reason")
                worklist = handle_query(right_query, masterlist)
                make_frame(worklist, "templates/frame_2", toprow)
        except:
            pass
        # Finally, here's the script for the reset button
        try:
            if request.form["reset"] == "reset":
                with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "templates/frame_1.html"), mode='w') as file:
                    file.write(" ")
                with open(os.path.join(os.path.realpath(os.path.dirname(__file__)), "templates/frame_2.html"), mode='w') as file:
                    file.write(" ")
        except:
            pass
    return render_template("main_page.html")

@app.route('/frame1')
def table_1():
    return render_template("frame_1.html")

@app.route('/frame2')
def table_2():
    return render_template("frame_2.html")
