from flask import Flask, render_template_string

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Akanksha Mandar Parkar | Portfolio</title>

<style>
*{box-sizing:border-box;}
body{
    margin:0;
    font-family:'Poppins', sans-serif;
    overflow:hidden;
}

.slider{
    display:flex;
    width:600vw;
    height:100vh;
    transition:transform 1s ease-in-out;
}

.slide{
    width:100vw;
    height:100vh;
    padding:60px;
    display:flex;
    justify-content:center;
    align-items:center;
    flex-direction:column;
    text-align:center;
}

.content{
    max-width:800px;
}

h1{font-size:3rem;margin-bottom:10px;}
h2{font-size:2.4rem;margin-bottom:15px;}
p,li{font-size:1.05rem;line-height:1.6;}

.slide:nth-child(1){background:linear-gradient(135deg,#fbc2eb,#a6c1ee);}
.slide:nth-child(2){background:linear-gradient(135deg,#ffecd2,#fcb69f);}
.slide:nth-child(3){background:linear-gradient(135deg,#cfd9df,#e2ebf0);}
.slide:nth-child(4){background:linear-gradient(135deg,#fddb92,#d1fdff);}
.slide:nth-child(5){background:linear-gradient(135deg,#e0c3fc,#8ec5fc);}
.slide:nth-child(6){background:linear-gradient(135deg,#fdfbfb,#ebedee);}

ul{padding-left:20px;text-align:left;}

@media(max-width:768px){
    .slide{
        padding:40px 20px;
    }
    h1{font-size:2.2rem;}
    h2{font-size:1.8rem;}
    .content{max-width:95%;}
}
</style>
</head>

<body>

<div class="slider" id="slider">

<!-- Slide 1 -->
<div class="slide">
<div class="content">
<h1>Hi, I'm Akanksha 👋</h1>
<p><b>Akanksha Mandar Parkar</b></p>
<p>Python Developer • Web Designer • Educator</p>
<p>📱 +91 8169289015<br>📧 akanksha.mparkar08@gmail.com</p>
</div>
</div>

<!-- Slide 2 -->
<div class="slide">
<div class="content">
<h2>Objective</h2>
<p>
Motivated and detail-oriented individual seeking an opportunity in a reputed
organization where my technical knowledge, professional attitude and practical
experience contribute to organizational growth and my career development.
</p>
</div>
</div>

<!-- Slide 3 -->
<div class="slide">
<div class="content">
<h2>Education</h2>
<ul>
<li><b>B.Sc IT</b> – Kirti M. Doongursee College (2025) – 75%</li>
<li><b>HSC</b> – Model College of Science & Commerce (2022) – 51.67%</li>
<li><b>SSC</b> – Chanakya Vidyalay (2020) – 80.40%</li>
</ul>
</div>
</div>

<!-- Slide 4 -->
<div class="slide">
<div class="content">
<h2>Skills & Certifications</h2>
<ul>
<li>Python, JavaScript, Node.js, C, C++, PHP</li>
<li>MongoDB, MySQL</li>
<li>Power BI, Tally, JMeter, Figma</li>
<li>AI Course – Anudip (IBM)</li>
<li>Deloitte & Tata Virtual Internship</li>
</ul>
</div>
</div>

<!-- Slide 5 -->
<div class="slide">
<div class="content">
<h2>Projects</h2>
<ul>
<li><b>Apla Kokan</b> – Tourism Website</li>
<li><b>VetPulse</b> – React & Node.js</li>
<li><b>QuizWiz</b> – Python</li>
<li><b>QubeHealth Review</b></li>
</ul>
</div>
</div>

<!-- Slide 6 -->
<div class="slide">
<div class="content">
<h2>Work & Hobbies</h2>
<p><b>Suyash Sanstha Trust</b> – Assistant Accountant & Trainer</p>
<p><b>Gurukul Academy</b> – Teacher</p>
<p>🎵 Music • 📚 Reading • 🎨 Drawing • 🍳 Cooking</p>
</div>
</div>

</div>

<script>
let index = 0;
setInterval(()=>{
    index = (index + 1) % 6;
    document.getElementById("slider").style.transform =
    `translateX(-${index * 100}vw)`;
}, 5000);
</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(html)

if __name__ == "__main__":
    app.run(debug=True)
