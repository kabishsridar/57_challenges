sitename = input("Site name: ")
author = input("Author: ")
folder_js = input("Do you want a folder for Javascript? (y/n): ")
folder_css = input("Do you want a folder for CSS? (y/n): ")

fhtml = open('index.html', 'w+')
fjs = open('javascript.js','w')
jcss = open('stylesheet.css','w')

fhtml.write(f"""<!DOCTYPE html>
<html lang="en-US">
<head>
    <meta charset="UTF-8">
    <meta name="author" content="james">
    <title>kabish</title>
</head>
<body>
        <h1>WELCOME TO kabish</h1>
</body>
</html>""")
print(f"Created ./{sitename}")
print(f"Created ./{sitename}/index.html")
print(f"Created ./{sitename}/js" if folder_js == "y" else f"Created ./{sitename}")
print(f"Created ./{sitename}/css" if folder_css == "y" else f"Created ./{sitename}")
