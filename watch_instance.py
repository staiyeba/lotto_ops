#! /usr/bin/env python

import sys
import operator
import time
import csv
import os
import subprocess

filename = sys.argv[1]
tests = []
csv_table = []
this_dir = os.path.dirname(os.path.abspath(__file__))
upload_dir = 'templates/'
path_uploads = os.path.join(this_dir, upload_dir)

def get_csv_table(filename,headers=None,delimiter=","):

    with open(filename, 'rb') as f:
        mycsv = csv.reader(f)

        table = "<table border=1>"

#            table+= "".join(["<th align=center>"+cell+"</th>" for cell in headers])
    #    else:
    #        table+= "".join(["<th align=center>"+cell+"</th>" for cell in mycsv[0]])
    #        rows=rows[1:]
        firstline = True
        for row in mycsv:
            if firstline:
                for cell in row:
                    table+= "".join(["<th align=center>"+cell+"</th>"])
                firstline = False  #skip first line next time
                continue
            table += "<tr>"
            for cell in row:
                if int(row[4]) > int(0):
                    table += "".join(["<td align=center style=color:red;>"+cell+"</td>"])
                else:
                    table += "".join(["<td align=center>"+cell+"</td>"])
            table += "</tr>"
        table+="</table><br>"
    #    print table
    return table


def main():


    html_table = get_csv_table(filename)
    fname = filename.split(".")[0]
    fname_html = '{0}{1}'.format(fname,".html")

    with open(fname_html, 'w') as f:
        f.write("<h1 align=center>INSTANCE HEALTH</h1><br>")
        for s in html_table:
            f.write(s)
        #    f.write("\n")
    #        print s
    call_mv = 'mv {0} {1}'.format(fname_html, path_uploads)
    subprocess.call(call_mv, shell=True)


if __name__ == '__main__':
    main()
