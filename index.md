---
title: "Adaline Powell"
format:
  html:
    theme: none
---

<style>

/* ========== YOUR FULL CSS ========== */

body {
  background:#f7f3ee;
  color:#4b3621;
  font-family: Inter, sans-serif;
  margin:0;
}

/* NAVBAR */
.nav {
  width:100%;
  background:#7a5c3d;
  padding:16px 0;
  display:flex;
  justify-content:center;
  gap:40px;
  border-bottom:2px solid #4b3621;
  position:sticky;
  top:0;
  z-index:999;
}
.nav a {
  color:#f7f3ee;
  text-decoration:none;
  font-size:18px;
  font-weight:600;
}
.nav a:hover {
  color:#e8dfd6;
}

/* ICON BAR */
.icon-bar {
  position:absolute;
  top:22px;
  right:30px;
  display:flex;
  gap:12px;
}
.icon-img {
  width:28px;
  opacity:0.9;
  transition:0.3s;
}
.icon-img:hover {
  opacity:1;
  transform:scale(1.1);
}

/* HERO SECTION */
.hero {
  text-align:center;
  margin-top:60px;
}
.hero-img {
  width:300px;
  border-radius:50%;
  box-shadow:0 6px 12px rgba(75,54,33,0.2);
}
.hero-title {
  font-size:48px;
  font-weight:800;
  margin-top:25px;
}
.hero-subtitle {
  font-size:22px;
  color:#6a4c33;
  margin-bottom:20px;
}
.resume-btn {
  background:#7a5c3d;
  padding:12px 20px;
  color:white;
  text-decoration:none;
  border-radius:8px;
  font-weight:600;
  transition:0.3s;
}
.resume-btn:hover {
  background:#5c4033;
}

/* ABOUT SECTION */
.about p {
  max-width:850px;
  margin:20px auto;
  font-size:18px;
  text-align:center;
}

/* PROJECTS */
.projects-grid {
  display:flex;
  justify-content:center;
  gap:30px;
  flex-wrap:wrap;
  margin-top:25px;
}
.project-img {
  width:260px;
  border-radius:12px;
  filter:grayscale(95%);
  transition:0.3s;
  box-shadow:0 4px 8px rgba(75,54,33,0.12);
}
.project-img:hover {
  filter:none;
  transform:scale(1.04);
}
.project-caption {
  text-align:center;
  margin-top:10px;
  font-weight:600;
}

/* SKILLS GRID */
.skills-grid {
  max-width:1100px;
  margin:40px auto;
  display:grid;
  grid-template-columns:repeat(auto-fit, minmax(250px,1fr));
  gap:25px;
}
.skill-card {
  background:#f2e7da;
  padding:22px;
  border-radius:12px;
  border-left:5px solid #7a5c3d;
  box-shadow:0 4px 10px rgba(75,54,33,0.1);
}
.skill-card h3 {
  margin-top:0;
  font-size:22px;
  font-weight:700;
}
.skill-card ul {
  list-style:none;
  padding:0;
}
.skill-card li {
  font-size:16px;
  margin:6px 0;
}

/* FOOTER */
.footer {
  text-align:center;
  padding:25px;
  color:#6a4c33;
  font-size:14px;
  margin-top:50px;
}

/* DIVIDER */
.hr-cute {
  width:60%;
  height:2px;
  margin:50px auto;
  background:#d7c3a3;
  border-radius:50px;
  border:0;
}

</style>

<!-- ========== NAVIGATION BAR ========== -->
<nav class="nav">
  <a href="index.html">Home</a>
  <a href="about.html">About Me</a>
  <a href="education.html">Education</a>
  <a href="work_history.html">Work History</a>
  <a href="projects.html">Projects</a>
</nav>

<!-- ========== ICONS ========== -->
<div class="icon-bar">
  <a href="mailto:adalinebrynnpowell@gmail.com" title="Email">
    <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" class="icon-img">
  </a>
  <a href="https://www.linkedin.com/in/adaline-powell177/" target="_blank" title="LinkedIn">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" class="icon-img">
  </a>
</div>

<!-- ========== HERO SECTION ========== -->
<section class="hero">
  <img src="photodata.png" alt="Adaline Powell" class="hero-img">
  <h1 class="hero-title">Adaline Powell</h1>
  <p class="hero-subtitle">Data Scientist •Political Scientist • Researcher</p>

  <a href="resume.pdf" target="_blank" class="resume-btn">Download Résumé</a>
</section>

<hr class="hr-cute">

<!-- ========== ABOUT ========== -->
<section class="about">
  <h2>Welcome</h2>
  <p>
    I’m a political scientist and data scientist with experience in
    statistical modeling, spatial analysis, and data visualization.
    I use R, Python, ArcGIS, and machine learning techniques to answer complex questions.
  </p>
</section>

<hr class="hr-cute">

<!-- ========== PROJECTS ========== -->
<h2 style="text-align:center;">Featured Projects</h2>

<div class="projects-grid">
  <a href="negotiations.html">
    <img src="cow.png" class="project-img">
    <div class="project-caption">Predicting Negotiation Outcomes</div>
  </a>

  <a href="variableimportance.html">
    <img src="variableimportance.png" class="project-img">
    <div class="project-caption">Variable Importance ML Visualization</div>
  </a>

  <a href="Missingness.html">
    <img src="missingness.png" class="project-img">
    <div class="project-caption">Missingness Diagnostics</div>
  </a>
</div>

<hr class="hr-cute">

<!-- ========== SKILLS ========== -->
<h2 style="text-align:center;">Skills & Tools</h2>

<div class="skills-grid">
  <div class="skill-card">
    <h3>Programming</h3>
    <ul>
      <li>R & RStudio</li>
      <li>Python</li>
      <li>Stata</li>
      <li>SPSS</li>
      <li>Excel (Advanced)</li>
    </ul>
  </div>

  <div class="skill-card">
    <h3>Modeling</h3>
    <ul>
      <li>Regression (OLS, Logistic, Multinomial)</li>
      <li>Predictive Modeling</li>
      <li>Machine Learning (Foundational)</li>
      <li>Bayesian Modeling</li>
    </ul>
  </div>


  <div class="skill-card">
    <h3>Tools</h3>
    <ul>
      <li>ArcGIS</li>
      <li>GitHub</li>
      <li>Quarto / R Markdown</li>
      <li>SQL (Basic)</li>
    </ul>
  </div>
</div>

<hr class="hr-cute">

<footer class="footer">
  © 2025 Adaline Powell • Data & Political Science
</footer>
