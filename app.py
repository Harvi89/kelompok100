from dotenv import load_dotenv

load_dotenv()

from flask import Flask, render_template, request, jsonify

from chatbot.retrieval import retrieve
from chatbot.llm import generate_answer