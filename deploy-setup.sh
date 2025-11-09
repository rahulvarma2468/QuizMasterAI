#!/bin/bash
# Quick deployment setup script

echo "🚀 QuizMasterAI Deployment Setup"
echo "================================="
echo ""

# Check if git is initialized
if [ ! -d .git ]; then
    echo "📦 Initializing Git repository..."
    git init
    git add .
    git commit -m "Initial commit - QuizMasterAI"
    echo "✅ Git initialized"
else
    echo "✅ Git already initialized"
fi

echo ""
echo "📋 Next Steps:"
echo ""
echo "1. Create a GitHub repository"
echo "2. Push your code:"
echo "   git remote add origin https://github.com/YOUR_USERNAME/QuizMasterAI.git"
echo "   git branch -M main"
echo "   git push -u origin main"
echo ""
echo "3. Choose a deployment option:"
echo "   📘 See DEPLOYMENT_GUIDE.md for detailed instructions"
echo ""
echo "🌟 RECOMMENDED: Vercel (Frontend) + Render (Backend)"
echo "   - 100% FREE tier available"
echo "   - Automatic deployments from GitHub"
echo "   - SSL certificates included"
echo ""
echo "Ready to deploy? Check out DEPLOYMENT_GUIDE.md! 🎉"
