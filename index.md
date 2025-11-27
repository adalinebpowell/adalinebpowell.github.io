---
title: "Adaline Powell"
project:
  type: website

website:
  title: ""        # removes the blue text
  navbar: false    # disables Quarto's navbar completely

format:
  html:
    theme: none

---

<style>

/* -------- GLOBAL THEME -------- */
body {
  background-color: #f7f3ee;        /* soft cream */
  color: #4b3621;                   /* deep brown text */
  font-family: 'Inter', sans-serif;
  line-height: 1.6;
}

/* -------- NAVIGATION BAR -------- */
nav {
  width:100%;
  background:#7a5c3d;               /* warm brown */
  padding:14px 0;
  display:flex;
  justify-content:center;
  gap:40px;
  position:sticky;
  top:0;
  z-index:1000;
  border-bottom: 2px solid #4b3621;
}

nav a {
  color:#f7f3ee;
  font-size:18px;
  text-decoration:none;
  font-weight:500;
  transition:0.3s ease;
}

nav a:hover {
  color:#e8dfd6;                    /* soft beige */
  border-bottom:2px solid #e8dfd6;
  padding-bottom:3px;
}

/* -------- PROJECT IMAGES -------- */
.project-img {
  width:250px;
  border-radius:12px;
  filter:grayscale(100%);
  transition: all 0.3s ease;
  box-shadow:0 4px 8px rgba(75, 54, 33, 0.15);
}

.project-img:hover {
  filter:grayscale(0%);
  transform:scale(1.04);
}

/* -------- HEADERS -------- */
h1, h2, h3 {
  color:#4b3621;
  font-weight:700;
}

/* cute small divider */
.hr-cute {
  border:0;
  height:2px;
  width:60%;
  background:#d7c3a3;               /* light coffee */
  margin:40px auto;
  border-radius:50px;
}

  .icon-bar {
  position: absolute;
  top: 85px;              /* adjust if needed depending on your nav height */
  right: 40px;            /* moves icons to the right edge */
  display: flex;
  gap: 12px;
  z-index: 2000;
}

.icon-img {
  width: 28px;            /* small + clean */
  height: 28px;
  opacity: 0.85;
  transition: 0.3s ease;
}

.icon-img:hover {
  opacity: 1;
  transform: scale(1.1);
}
</style>


<!-- NAVIGATION BAR -->
<nav>
  <a href="index.html">Home</a>
  <a href="about.html">About Me</a>
  <a href="education.html">Education</a>
  <a href="work_history.html">Work History</a>
  <a href="projects.html">Projects</a>
</nav>

<!-- TOP RIGHT ICON BAR -->
<div class="icon-bar">
  <a href="mailto:adalinebrynnpowell@gmail.com" class="icon-link" title="Email Me">
    <img src="https://cdn-icons-png.flaticon.com/512/561/561127.png" alt="Email" class="icon-img">
  </a>
  <a href="https://www.linkedin.com/in/adaline-powell177/" class="icon-link" title="LinkedIn" target="_blank">
    <img src="https://cdn-icons-png.flaticon.com/512/174/174857.png" alt="LinkedIn" class="icon-img">
  </a>
</div>

<!-- PROFILE IMAGE -->
<img src="photodata.png"
     width="700"
     alt="Adaline Powell"
     style="border-radius: 50%; display: block; margin: 50px auto; box-shadow:0 6px 12px rgba(75, 54, 33, 0.18);" />


# Welcome

Hi, I'm Adaline Powell!  

This site highlights my projects, visualizations, and research work!

<h2 style="text-align:center; margin-top:40px;">Featured Projects</h2>

<div style="display:flex; justify-content:center; gap:30px; flex-wrap:wrap; margin-top:25px;">

  <a href="negotiations.html" style="text-decoration:none;">
    <img src="cow.png" alt="Predicting Negotiations" class="project-img" />
  </a>

  <a href="variableimportance.html" style="text-decoration:none;">
    <img src="variableimportance.png" alt="PulseML Visualization" class="project-img" />
  </a>

  <a href="Missingness.html" style="text-decoration:none;">
    <img src="missingness.png" alt="Missingness Analysis" class="project-img" />
  </a>

</div>

<hr class="hr-cute">
