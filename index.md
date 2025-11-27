---
title: "Adaline Powell"
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
</style>


<!-- NAVIGATION BAR -->
<nav>
  <a href="index.html">Home</a>
  <a href="about.html">About Me</a>
  <a href="education.html">Education</a>
  <a href="work_history.html">Work History</a>
  <a href="projects.html">Projects</a>
</nav>


<!-- PROFILE IMAGE -->
<img src="https://media.licdn.com/dms/image/v2/D5603AQEHjz5RR88hHg/profile-displayphoto-crop_800_800/B56ZmENjc9J0AI-/0/1758859771265?e=1764201600&v=beta&t=YTDNeqb6IpxfrjRsmodOAAmIZbsG44KM6HNE8fsvtms" 
     width="250" 
     alt="Adaline Powell" 
     style="border-radius: 50%; display: block; margin: 50px auto; box-shadow:0 6px 12px rgba(75, 54, 33, 0.18);" />

# Welcome

Hi, I'm **Adaline Powell**!  
I am a Master’s student in Data Science at UW–Milwaukee.  

This site highlights my **projects, visualizations, and research work**, all centered around data science, analytics, and machine learning.

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
