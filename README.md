<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Muzammil Haider - GitHub Profile</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: #0a0a0a;
            color: #e4e4e7;
            line-height: 1.6;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            padding: 40px 20px;
        }

        .header {
            text-align: center;
            margin-bottom: 60px;
            padding: 40px 0;
            background: linear-gradient(135deg, #18181b 0%, #27272a 100%);
            border-radius: 20px;
            border: 1px solid #3f3f46;
        }

        .header h1 {
            font-size: 3.5rem;
            font-weight: 300;
            margin-bottom: 10px;
            background: linear-gradient(45deg, #a855f7, #06b6d4);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }

        .header .subtitle {
            font-size: 1.2rem;
            color: #a1a1aa;
            margin-bottom: 30px;
        }

        .social-links {
            display: flex;
            justify-content: center;
            gap: 20px;
            margin-top: 20px;
        }

        .social-links a {
            padding: 10px 20px;
            background: #27272a;
            color: #e4e4e7;
            text-decoration: none;
            border-radius: 8px;
            border: 1px solid #3f3f46;
            transition: all 0.3s ease;
            font-size: 0.9rem;
        }

        .social-links a:hover {
            background: #3f3f46;
            transform: translateY(-2px);
        }

        .section {
            margin-bottom: 50px;
            padding: 30px;
            background: #18181b;
            border-radius: 15px;
            border: 1px solid #27272a;
        }

        .section h2 {
            font-size: 2rem;
            font-weight: 400;
            margin-bottom: 20px;
            color: #f4f4f5;
        }

        .about-text {
            font-size: 1.1rem;
            color: #d4d4d8;
            margin-bottom: 30px;
        }

        .focus-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
            gap: 15px;
            margin-top: 20px;
        }

        .focus-item {
            padding: 20px;
            background: #27272a;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #3f3f46;
            transition: transform 0.3s ease;
        }

        .focus-item:hover {
            transform: translateY(-5px);
        }

        .focus-item h4 {
            color: #a855f7;
            margin-bottom: 8px;
            font-size: 1rem;
        }

        .focus-item p {
            color: #a1a1aa;
            font-size: 0.9rem;
        }

        .projects-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 25px;
        }

        .project-card {
            background: #27272a;
            border-radius: 12px;
            padding: 25px;
            border: 1px solid #3f3f46;
            transition: all 0.3s ease;
        }

        .project-card:hover {
            transform: translateY(-5px);
            border-color: #a855f7;
        }

        .project-card h3 {
            color: #f4f4f5;
            margin-bottom: 10px;
            font-size: 1.3rem;
        }

        .project-card .description {
            color: #d4d4d8;
            margin-bottom: 15px;
            font-size: 0.95rem;
        }

        .tech-stack {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 15px;
        }

        .tech-tag {
            background: #3f3f46;
            color: #e4e4e7;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: 0.8rem;
            border: 1px solid #52525b;
        }

        .project-link {
            display: inline-block;
            color: #a855f7;
            text-decoration: none;
            font-weight: 500;
            transition: color 0.3s ease;
        }

        .project-link:hover {
            color: #06b6d4;
        }

        .skills-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
        }

        .skill-category {
            background: #27272a;
            padding: 20px;
            border-radius: 10px;
            border: 1px solid #3f3f46;
        }

        .skill-category h4 {
            color: #f4f4f5;
            margin-bottom: 15px;
            font-size: 1.1rem;
        }

        .skill-list {
            display: flex;
            flex-wrap: wrap;
            gap: 8px;
        }

        .skill-item {
            background: #3f3f46;
            color: #e4e4e7;
            padding: 6px 12px;
            border-radius: 15px;
            font-size: 0.85rem;
            border: 1px solid #52525b;
        }

        .stats-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
            margin-top: 20px;
        }

        .stat-card {
            background: #27272a;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            border: 1px solid #3f3f46;
        }

        .footer {
            text-align: center;
            padding: 40px 0;
            color: #71717a;
            font-style: italic;
        }

        @media (max-width: 768px) {
            .header h1 {
                font-size: 2.5rem;
            }
            
            .projects-grid {
                grid-template-columns: 1fr;
            }
            
            .social-links {
                flex-direction: column;
                align-items: center;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <!-- Header -->
        <div class="header">
            <h1>Muzammil Haider</h1>
            <p class="subtitle">AI Engineer & Full-Stack Developer</p>
            <p style="color: #a1a1aa; margin-bottom: 20px;">Computer Science @ NUML University • CGPA: 3.60/4.0</p>
            
            <div class="social-links">
                <a href="mailto:muzamilhaider444@gmail.com">Email</a>
                <a href="https://linkedin.com/in/muzamil-haider-89286329b">LinkedIn</a>
                <a href="https://github.com/haideransari444">GitHub</a>
                <a href="https://x.com/nfak_ism_">Twitter</a>
            </div>
        </div>

        <!-- About Section -->
        <div class="section">
            <h2>About</h2>
            <p class="about-text">
                I'm passionate about building intelligent systems that solve real-world problems. 
                Currently exploring advanced neural architectures, natural language processing, 
                and creating scalable web applications.
            </p>
            
            <div class="focus-grid">
                <div class="focus-item">
                    <h4>Neural Networks</h4>
                    <p>Training next-gen AI models</p>
                </div>
                <div class="focus-item">
                    <h4>Backend Systems</h4>
                    <p>Scalable web applications</p>
                </div>
                <div class="focus-item">
                    <h4>NLP Research</h4>
                    <p>Language understanding</p>
                </div>
                <div class="focus-item">
                    <h4>Open Source</h4>
                    <p>Community contributions</p>
                </div>
            </div>
        </div>

        <!-- Projects Section -->
        <div class="section">
            <h2>Featured Projects</h2>
            <div class="projects-grid">
                <div class="project-card">
                    <h3>🎓 Alif - AI Tutor</h3>
                    <p class="description">
                        Adaptive learning platform with ML-powered insights, voice-enabled interaction, 
                        and real-time performance analytics.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-tag">FastAPI</span>
                        <span class="tech-tag">PyTorch</span>
                        <span class="tech-tag">Gemini API</span>
                    </div>
                    <a href="https://github.com/haideransari444/Alif-AI-Tutor" class="project-link">View Project →</a>
                </div>

                <div class="project-card">
                    <h3>⚖️ Qanoon - Legal AI</h3>
                    <p class="description">
                        Advanced legal document analysis system with multilingual processing and 
                        semantic search across Pakistani law database.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-tag">LangChain</span>
                        <span class="tech-tag">Transformers</span>
                        <span class="tech-tag">spaCy</span>
                    </div>
                    <a href="https://github.com/haideransari444/Qanoon-Legal-AI" class="project-link">View Project →</a>
                </div>

                <div class="project-card">
                    <h3>💻 Easy-Terminal</h3>
                    <p class="description">
                        Natural language to shell command converter with intelligent safety validation 
                        and context-aware suggestions.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-tag">OpenAI API</span>
                        <span class="tech-tag">NLP</span>
                        <span class="tech-tag">Shell</span>
                    </div>
                    <a href="https://github.com/haideransari444/Easy-Terminal" class="project-link">View Project →</a>
                </div>

                <div class="project-card">
                    <h3>🎮 Mario-RL</h3>
                    <p class="description">
                        Reinforcement learning agent using Proximal Policy Optimization with 
                        performance visualization and reward optimization.
                    </p>
                    <div class="tech-stack">
                        <span class="tech-tag">Stable Baselines3</span>
                        <span class="tech-tag">OpenAI Gym</span>
                        <span class="tech-tag">PPO</span>
                    </div>
                    <a href="https://github.com/haideransari444/Mario-RL" class="project-link">View Project →</a>
                </div>
            </div>
        </div>

        <!-- Skills Section -->
        <div class="section">
            <h2>Technical Skills</h2>
            <div class="skills-grid">
                <div class="skill-category">
                    <h4>AI & Machine Learning</h4>
                    <div class="skill-list">
                        <span class="skill-item">TensorFlow</span>
                        <span class="skill-item">PyTorch</span>
                        <span class="skill-item">LangChain</span>
                        <span class="skill-item">Transformers</span>
                        <span class="skill-item">OpenAI API</span>
                        <span class="skill-item">Scikit-Learn</span>
                        <span class="skill-item">OpenCV</span>
                    </div>
                </div>

                <div class="skill-category">
                    <h4>Web Development</h4>
                    <div class="skill-list">
                        <span class="skill-item">Django</span>
                        <span class="skill-item">FastAPI</span>
                        <span class="skill-item">Streamlit</span>
                        <span class="skill-item">React</span>
                        <span class="skill-item">JavaScript</span>
                        <span class="skill-item">HTML/CSS</span>
                    </div>
                </div>

                <div class="skill-category">
                    <h4>Tools & Technologies</h4>
                    <div class="skill-list">
                        <span class="skill-item">Python</span>
                        <span class="skill-item">Docker</span>
                        <span class="skill-item">Git</span>
                        <span class="skill-item">PostgreSQL</span>
                        <span class="skill-item">Redis</span>
                        <span class="skill-item">Linux</span>
                    </div>
                </div>
            </div>
        </div>

        <!-- Stats Section -->
        <div class="section">
            <h2>GitHub Stats</h2>
            <div class="stats-container">
                <div class="stat-card">
                    <img src="https://github-readme-stats.vercel.app/api?username=haideransari444&show_icons=true&theme=dark&bg_color=27272a&title_color=a855f7&text_color=e4e4e7&icon_color=a855f7&border_color=3f3f46&border_radius=10" alt="GitHub Stats" style="width: 100%; max-width: 400px;">
                </div>
                <div class="stat-card">
                    <img src="https://github-readme-streak-stats.herokuapp.com/?user=haideransari444&theme=dark&background=27272a&border=3f3f46&stroke=a855f7&ring=a855f7&fire=06b6d4&currStreakLabel=a855f7&sideLabels=e4e4e7&currStreakNum=e4e4e7&sideNums=e4e4e7&dates=e4e4e7&border_radius=10" alt="GitHub Streak" style="width: 100%; max-width: 400px;">
                </div>
            </div>
        </div>

        <!-- Footer -->
        <div class="footer">
            <p>"The best way to predict the future is to create it through code."</p>
            <p style="margin-top: 10px; font-size: 0.9rem;">Always ready for exciting AI/ML projects and innovative challenges</p>
        </div>
    </div>
</body>
</html>
