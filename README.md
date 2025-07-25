# QR Code Generator

A FastAPI-based web app that generates customized QR codes from user input. Deployed serverlessly using Vercel.

## Features
- Input any URL
- Customize QR colors (foreground/background)
- Generate and preview QR code instantly
- Download-ready PNG output

## Tech Stack
- FastAPI + qrcode + Pillow (Python)
- HTML/CSS frontend
- Vercel serverless deployment

## Run locally
pip install -r requirements.txt
uvicorn test_local:app --reload

## Deploy
vercel
