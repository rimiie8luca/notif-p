from flask import Flask, render_template_string

app = Flask(_name_)

html_code = """
<!DOCTYPE html>
<html>
<head>
<title>Notification</title>
<style>
body { display: flex; justify-content: center; align-items: center; height: 100vh; }
.modal { background-color: white; padding: 20px; border: 1px solid #ccc; text-align: center; }
</style>
</head>
<body>
<div class="modal">
    <p id="message">Read the text?</p>
    <button id="yesButton">Yes</button>
</div>

<script>
document.getElementById('yesButton').onclick = function() {
    document.getElementById('message').textContent = "ₘₕₘ";
    this.style.display = 'none';
};
</script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(html_code)

if _name_ == '_main_':
    app.run(debug=True)
