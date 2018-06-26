import os
import urllib
import cgi
from flask import Flask, request, redirect, url_for, send_from_directory

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO

BASE_DIR = os.path.dirname(__file__)

print ("dir:%s" % BASE_DIR)

UPLOAD_FOLDER = 'templates/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def list_directory(path):
        try:
            list = os.listdir(path)
        except os.error:
            return "No permission to list directory"
        list.sort(key=lambda a: a.lower())
        f = StringIO()
        displaypath = cgi.escape(urllib.unquote(path))
        f.write("<body><h4>html file listing</h4>") #% displaypath)
        f.write("<form ENCTYPE=\"multipart/form-data\" method=\"post\">")

        for name in list:
            extension = name.split(".")[1:]
            for ex in extension:
                if ex == "html":
                    fullname = os.path.join(path, name)
                    displayname = linkname = name
                    if os.path.isdir(fullname):
                        displayname = name + "/"
                        linkname = name + "/"
                    if os.path.islink(fullname):
                        displayname = name + "@"
                    f.write('<li><a href="templates/%s">%s</a>\n'
                            % (urllib.quote(linkname), cgi.escape(displayname)))
        f.write("</ul>\n<hr>\n</body>\n</html>\n")
        length = f.tell()
        f.seek(0)
        return f


@app.route('/templates/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    uploads = os.path.join(BASE_DIR, UPLOAD_FOLDER)
    return send_from_directory(directory=uploads, filename=filename)

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print('filename:%s' % file.filename)
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('index'))
    return """
    <!DOCTYPE html>
    <html lang="en">
      <body>
        <div class="container">
          <div class="header">
            <h3 class="text-muted">Lotto Monitoring Logs</h3>
          </div>
          <hr/>
        </div>
      </body>
    </html>
    %s
    """ % "<br>".join(list_directory(app.config['UPLOAD_FOLDER']))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
