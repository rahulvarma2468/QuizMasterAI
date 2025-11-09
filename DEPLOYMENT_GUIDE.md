# 🚀 QuizMasterAI Deployment Guide

## Quick Start Deployment Options

### ⭐ RECOMMENDED: Vercel + Render (Free Tier)

This is the easiest and most cost-effective option for deploying your full-stack app.

---

## 📋 Pre-Deployment Checklist

Before deploying, make sure you have:
- [x] GitHub account
- [x] Your code pushed to a GitHub repository
- [x] Gemini API key
- [x] Accounts on deployment platforms (Vercel, Render, etc.)

---

## 🎯 Option 1: Vercel (Frontend) + Render (Backend)

### Step 1: Deploy Backend to Render

1. **Go to [render.com](https://render.com)** and sign up/login

2. **Create PostgreSQL Database:**
   - Click "New +" → "PostgreSQL"
   - Name: `quizmaster-db`
   - Select free tier
   - Click "Create Database"
   - Copy the "Internal Database URL" (starts with `postgresql://`)

3. **Create Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Settings:
     ```
     Name: quizmaster-backend
     Region: Oregon (US West)
     Branch: main
     Root Directory: backend
     Runtime: Python 3
     Build Command: pip install -r requirements.txt
     Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
     ```

4. **Add Environment Variables:**
   - Click "Environment" tab
   - Add:
     ```
     GEMINI_API_KEY = AIzaSyDcJLf2IJpKPWDB...
     DATABASE_URL = postgresql://... (from step 2)
     ```

5. **Deploy:**
   - Click "Create Web Service"
   - Wait 5-10 minutes for deployment
   - Copy your backend URL: `https://quizmaster-backend.onrender.com`

### Step 2: Deploy Frontend to Vercel

1. **Go to [vercel.com](https://vercel.com)** and sign up/login

2. **Import Project:**
   - Click "Add New" → "Project"
   - Import your GitHub repository
   - Framework Preset: Vite
   - Root Directory: `frontend`
   - Build Command: `npm run build`
   - Output Directory: `dist`

3. **Add Environment Variable:**
   - Go to "Settings" → "Environment Variables"
   - Add:
     ```
     VITE_API_BASE_URL = https://quizmaster-backend.onrender.com
     ```

4. **Deploy:**
   - Click "Deploy"
   - Your app will be live at: `https://your-project.vercel.app`

5. **Update Backend CORS:**
   - Update `backend/main.py` CORS settings:
   ```python
   app.add_middleware(
       CORSMiddleware,
       allow_origins=["https://your-project.vercel.app"],
       allow_credentials=True,
       allow_methods=["*"],
       allow_headers=["*"],
   )
   ```
   - Push to GitHub
   - Render will auto-deploy

### ✅ Done! Your app is live!

**Access:**
- Frontend: `https://your-project.vercel.app`
- Backend API: `https://quizmaster-backend.onrender.com`
- API Docs: `https://quizmaster-backend.onrender.com/docs`

---

## 🚂 Option 2: Railway (All-in-One - EASIEST)

### Step 1: Deploy to Railway

1. **Go to [railway.app](https://railway.app)** and sign up with GitHub

2. **Create New Project:**
   - Click "New Project"
   - Choose "Deploy from GitHub repo"
   - Select your QuizMasterAI repository
   - Railway will auto-detect both frontend and backend

3. **Add PostgreSQL:**
   - Click "New" → "Database" → "PostgreSQL"
   - Railway will automatically set `DATABASE_URL`

4. **Configure Backend Service:**
   - Click on the backend service
   - Go to "Variables" tab
   - Add:
     ```
     GEMINI_API_KEY = AIzaSyDcJLf2IJpKPWDB...
     ```
   - Go to "Settings" tab
   - Set:
     ```
     Root Directory: backend
     Build Command: pip install -r requirements.txt
     Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT
     ```

5. **Configure Frontend Service:**
   - Click on the frontend service
   - Go to "Variables" tab
   - Add:
     ```
     VITE_API_BASE_URL = https://[your-backend].up.railway.app
     ```
   - Go to "Settings" tab
   - Set:
     ```
     Root Directory: frontend
     Build Command: npm install && npm run build
     Start Command: npm run preview
     ```

6. **Generate Domains:**
   - Click on each service → "Settings" → "Generate Domain"
   - Copy the frontend URL - that's your live app!

### ✅ Done! Railway handles everything automatically!

**Note:** Railway gives $5 free credit monthly, then $5/month after trial.

---

## 💜 Option 3: Heroku

### Step 1: Install Heroku CLI

```bash
# Download from https://devcenter.heroku.com/articles/heroku-cli
```

### Step 2: Deploy Backend

```bash
cd backend
heroku login
heroku create quizmaster-backend
heroku addons:create heroku-postgresql:mini
heroku config:set GEMINI_API_KEY=AIzaSyDcJLf2IJpKPWDB...
git push heroku main
```

### Step 3: Deploy Frontend

Deploy frontend to Vercel (see Option 1, Step 2)

**Cost:** ~$7/month minimum

---

## ☁️ Option 4: AWS (Production Grade)

### Requirements:
- EC2 instance (t2.micro free tier)
- RDS PostgreSQL
- Route53 for domain
- SSL certificate

### Steps:
1. Launch EC2 Ubuntu instance
2. Install dependencies:
   ```bash
   sudo apt update
   sudo apt install python3-pip nodejs npm nginx postgresql-client
   ```
3. Clone repository and setup
4. Configure Nginx reverse proxy
5. Setup PM2 for process management
6. Configure RDS PostgreSQL
7. Setup SSL with Let's Encrypt

**Detailed guide:** [AWS Full-Stack Deployment Tutorial](https://docs.aws.amazon.com/elasticbeanstalk/)

**Cost:** ~$15-30/month

---

## 🌊 Option 5: DigitalOcean App Platform

### Step 1: Deploy

1. **Go to [digitalocean.com](https://www.digitalocean.com/)**
2. Click "Create" → "Apps"
3. Connect GitHub repository
4. DigitalOcean auto-detects:
   - Backend: Python app
   - Frontend: Static site
5. Add managed PostgreSQL database ($15/month)
6. Set environment variables
7. Deploy!

**Cost:** ~$12-20/month

---

## 🔐 Environment Variables Needed

### Backend:
```env
DATABASE_URL=postgresql://user:pass@host:5432/dbname
GEMINI_API_KEY=AIzaSyDcJLf2IJpKPWDB...
PORT=8000 (usually auto-set by platform)
```

### Frontend:
```env
VITE_API_BASE_URL=https://your-backend-url.com
```

---

## 📊 Comparison Table

| Platform | Cost | Difficulty | Auto-Deploy | SSL | Database |
|----------|------|------------|-------------|-----|----------|
| **Vercel + Render** | Free* | Easy | ✅ | ✅ | ✅ Free |
| **Railway** | $5/mo | Easiest | ✅ | ✅ | ✅ Included |
| **Heroku** | $7/mo | Easy | ✅ | ✅ | ✅ Addon |
| **AWS** | $15-30/mo | Hard | ❌ | ✅ | ✅ RDS |
| **DigitalOcean** | $12-20/mo | Medium | ✅ | ✅ | ✅ Managed |

*Free tier with limitations (backend may sleep after inactivity)

---

## 🚨 Common Deployment Issues

### Issue: CORS Errors
**Solution:** Update `backend/main.py` to allow your frontend domain:
```python
allow_origins=["https://your-frontend-domain.com"]
```

### Issue: Database Connection Failed
**Solution:** Check `DATABASE_URL` format:
```
postgresql://user:password@host:port/database
```

### Issue: Build Failed
**Solution:** Check Python/Node.js versions match deployment platform requirements

### Issue: API Key Not Working
**Solution:** Make sure environment variables are set in deployment platform dashboard

### Issue: Backend Sleeping (Free Tier)
**Solution:** 
- Upgrade to paid tier, or
- Use a service like [UptimeRobot](https://uptimerobot.com) to ping your backend every 5 minutes

---

## 🎉 Post-Deployment

After successful deployment:

1. **Test your app thoroughly:**
   - Generate a quiz
   - Check history
   - Verify database persistence

2. **Monitor performance:**
   - Check backend logs
   - Monitor API response times
   - Watch database usage

3. **Setup custom domain (optional):**
   - Buy domain from Namecheap/GoDaddy
   - Point to Vercel/Render
   - Add SSL certificate

4. **Enable analytics (optional):**
   - Google Analytics
   - Vercel Analytics
   - Sentry for error tracking

---

## 🆘 Need Help?

- **Vercel Docs:** https://vercel.com/docs
- **Render Docs:** https://render.com/docs
- **Railway Docs:** https://docs.railway.app
- **FastAPI Deployment:** https://fastapi.tiangolo.com/deployment/

---

## 🎯 Recommended Path

**For Learning/Portfolio:** → Vercel + Render (Free)
**For Small Production:** → Railway ($5/mo, easiest)
**For Serious Production:** → AWS/DigitalOcean (scalable)

---

**Good luck with your deployment! 🚀**
