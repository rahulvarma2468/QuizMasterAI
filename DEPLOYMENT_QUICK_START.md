# 🚀 Quick Deployment Reference

## ⭐ FASTEST: Railway (Recommended for Beginners)
```
1. Go to railway.app
2. Sign in with GitHub
3. "New Project" → "Deploy from GitHub repo"
4. Select QuizMasterAI
5. Add PostgreSQL database
6. Add GEMINI_API_KEY to environment variables
7. Generate domains
8. Done! ✅
```
**Time:** ~10 minutes | **Cost:** $5/month after free trial

---

## 🆓 FREE OPTION: Vercel + Render

### Backend (Render):
```
1. render.com → New PostgreSQL → Free tier
2. New Web Service → Connect GitHub
3. Root Directory: backend
4. Start: uvicorn main:app --host 0.0.0.0 --port $PORT
5. Add env vars: GEMINI_API_KEY, DATABASE_URL
```

### Frontend (Vercel):
```
1. vercel.com → Import Project → GitHub
2. Root Directory: frontend
3. Build: npm run build
4. Add env: VITE_API_BASE_URL=[render backend URL]
5. Deploy
```

**Time:** ~20 minutes | **Cost:** FREE (with sleep mode on backend)

---

## 📝 Environment Variables Needed

### Backend:
- `GEMINI_API_KEY` = AIzaSyDcJLf2IJpKPWDB...
- `DATABASE_URL` = postgresql://...
- `PORT` = (auto-set by platform)

### Frontend:
- `VITE_API_BASE_URL` = https://your-backend.com

---

## 🔧 Before Deploying

1. ✅ Push code to GitHub
2. ✅ Update CORS in `backend/main.py`:
   ```python
   allow_origins=["https://your-frontend-domain.com"]
   ```
3. ✅ Test locally one more time
4. ✅ Have your Gemini API key ready

---

## 📚 Full Details

See **DEPLOYMENT_GUIDE.md** for complete step-by-step instructions!
