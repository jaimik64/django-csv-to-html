from django.shortcuts import render, HttpResponseRedirect

from django import forms
import csv


def index(request):
    if request.method == "POST":
        days = request.POST["days"]
        # read data in uploaded_file (which is read in form of bytes)
        uploaded_file = request.FILES['csvfile'].read()
        # convert bytes data(uploaded_file) into string using decode
        linebylinedetails = uploaded_file.decode("utf-8")
        # make a list from linebylinedetails using split("\n")
        new_lines = linebylinedetails.split("\n")

        # list to store each sublist, each sublist contains line
        main = list()

        # convert each line into string using split(",") and append it in a main
        for i in new_lines:
            l1 = i.split(",")
            main.append(l1)

        table = list()  # list to store sublist of employe_id and present count
        # traverse main list
        for i in main:
            l1 = list()
            present = 0  # count present days of employee
            for j in i:  # traverse each word from particular line
                if j not in ("p", "a"):  # check if word is not p and a
                    l1.append(j)  # append employee id to list
                if j == "p":  # if word is p then increase present count by 1
                    present += 1
            l1.append(days)  # append total days in list l1
            l1.append(present)  # append present in list l1
            percentage = ((present * 100) / int(days))  # calculate percentage
            # append percentage in list l1
            l1.append("{0:.2f}".format(percentage))
            table.append(l1)  # append list l1 to table

        print(table)
    else:
        table = []
    return render(request, "csvTOhtml/form.html", {
        "details": table
    })
