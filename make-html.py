import os
import subprocess
import shutil
import sys
import time



def convert(md_file, html_file):
	if md_file.endswith("toc.md"):
		return;
	if not md_file.endswith(".md"):
		return;
		
	pre, ext = os.path.splitext(html_file)
	html_file = pre + ".html"
	
	print("Converting "+("toc" if md_file.endswith("toc.md") else "good")+" '"+md_file+"' to "+html_file);
	subprocess.call(["pandoc", md_file, "-f", "markdown", "-t", "html", "-o", html_file,
	"--css", "/style.css", "--title-prefix", "Slic3r Manual",
	"--include-before-body=html-inc/header.html", 
	"--include-before-body=html/toc.html", 
	"--include-before-body=html-inc/before-body.html", 
	"--include-after-body=html-inc/after-body.html"]);


def convert_dir(subdir):
	src_dir = "src/" + subdir;
	html_dir = "html/" + subdir;	
	if not os.path.isdir(html_dir):
		os.makedirs(html_dir)

	print("Convert dir "+src_dir+" to "+html_dir + " ("+subdir+")");
	
	if os.path.isdir(src_dir+"images"):
		shutil.copytree(src_dir+"images", html_dir+"images")
	
	extensions = ('.md')
	for item in os.listdir(src_dir):
		if os.path.isfile(src_dir + item):
			file = item;
			ext = os.path.splitext(file)[-1].lower()
			if ext in extensions:
				convert(src_dir + file, html_dir + file)
		elif os.path.isdir(src_dir + item):
			dir = item;
			if dir != "images":
				convert_dir(subdir + dir + "/")



if len(sys.argv) >= 2 and sys.argv[1] == '--server':
	os.chdir("html");
#	exec(open("SimpleHTTPServer").read())
	subprocess.call(["python", "-m", "http.server", "8000"])
	quit()
elif len(sys.argv) >= 2:
	print("Unknown option: "+sys.argv[1]+"\n");
	quit()


if os.path.isdir("html"):
	shutil.rmtree("html", ignore_errors=True);
	time.sleep(2)
os.makedirs("html")
# convert ToC
subprocess.call(["pandoc", "src/toc.md", "-f", "markdown", "-t", "html", "-o", "html/toc.html"]);


# convert manual pages
convert_dir("");


# copy images and stylesheet
shutil.copyfile("html-inc/style.css", "html/style.css")

# copy libslic3r documentation
shutil.copytree("libslic3r-doc", "html/libslic3r-doc")
