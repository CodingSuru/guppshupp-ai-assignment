from flask import Flask, render_template, request, jsonify
import json
from memory_engine.extractor import extract_memory
from personality_engine.transformer import generate_all_personalities

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/extract_memory', methods=['POST'])
def extract_memory_route():
    try:
        data = request.json
        messages = data.get('messages', '').strip().split('\n')
        messages = [msg.strip() for msg in messages if msg.strip()]
        
        if len(messages) < 5:
            return jsonify({
                'success': False,
                'error': 'Please provide at least 5 messages for better analysis.'
            })
        
        memory = extract_memory(messages)
        
        return jsonify({
            'success': True,
            'memory': memory
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/generate_personality', methods=['POST'])
def generate_personality_route():
    try:
        data = request.json
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({
                'success': False,
                'error': 'Please provide a message.'
            })
        
        # Generate neutral response based on keywords
        neutral_response = generate_neutral_response(user_message)
        
        # Generate all personality responses
        responses = generate_all_personalities(neutral_response)
        
        return jsonify({
            'success': True,
            'responses': responses
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

def generate_neutral_response(message):
    """Generate a neutral response based on message keywords"""
    msg_lower = message.lower()
    
    # Stress/Anxiety related
    if any(word in msg_lower for word in ['stress', 'stressed', 'anxiety', 'anxious', 'overwhelm', 'worried', 'pressure']):
        return "You should take a break and manage your time better. Try focusing on one task at a time and practice deep breathing exercises. Breaking large tasks into smaller steps can make them feel more manageable."
    
    # Sadness/Depression
    elif any(word in msg_lower for word in ['sad', 'depressed', 'down', 'unhappy', 'lonely', 'upset']):
        return "It's okay to feel this way. Consider talking to someone you trust, engaging in activities you enjoy, and remember that these feelings are temporary. Taking care of yourself is important."
    
    # Anger/Frustration
    elif any(word in msg_lower for word in ['angry', 'mad', 'frustrated', 'annoyed', 'irritated', 'furious']):
        return "Take a moment to cool down. Try to identify the root cause of your frustration and address it calmly. Deep breaths can help. Consider taking a short walk or doing something you enjoy."
    
    # Excitement/Happiness
    elif any(word in msg_lower for word in ['excited', 'happy', 'glad', 'joy', 'thrilled', 'great', 'awesome']):
        return "That's wonderful! Enjoy this positive energy and consider channeling it into productive activities or sharing it with others. Celebrate your wins, big or small."
    
    # Work/Study related
    elif any(word in msg_lower for word in ['work', 'job', 'study', 'exam', 'project', 'assignment', 'deadline', 'boss', 'colleague']):
        return "Create a clear plan with specific goals. Break tasks into smaller steps, set realistic deadlines, and don't forget to take regular breaks. Prioritize what's most important and tackle one thing at a time."
    
    # Relationship issues
    elif any(word in msg_lower for word in ['friend', 'family', 'relationship', 'partner', 'spouse', 'parent']):
        return "Communication is key. Try to express your feelings clearly and listen actively. Consider the other person's perspective as well. Healthy relationships require effort from both sides."
    
    # Goals/Dreams
    elif any(word in msg_lower for word in ['goal', 'dream', 'want to', 'wish', 'aspire', 'hope', 'plan']):
        return "That's a great ambition. Break it down into achievable milestones, create an action plan, and stay consistent with your efforts. Small daily progress adds up to big results."
    
    # Health related
    elif any(word in msg_lower for word in ['tired', 'exhausted', 'sleep', 'health', 'sick', 'ill', 'fatigue']):
        return "Your health is important. Ensure you're getting adequate rest, eating well, and exercising regularly. If issues persist, consult a healthcare professional. Self-care is not selfish."
    
    # Learning/Skills
    elif any(word in msg_lower for word in ['learn', 'skill', 'course', 'tutorial', 'practice', 'training', 'education']):
        return "Continuous learning is excellent. Set aside dedicated time for practice, use multiple resources, and apply what you learn through projects. Consistency is more important than intensity."
    
    # Career/Future
    elif any(word in msg_lower for word in ['career', 'future', 'job search', 'interview', 'resume', 'opportunity']):
        return "Focus on building relevant skills and networking. Update your resume regularly, practice interview skills, and don't be discouraged by rejections. Every experience teaches you something valuable."
    
    # Motivation/Confidence
    elif any(word in msg_lower for word in ['confidence', 'motivation', 'doubt', 'fear', 'worry', 'nervous']):
        return "Self-doubt is normal, but don't let it stop you. Focus on your strengths and past successes. Take small steps forward and celebrate progress. You're more capable than you think."
    
    # Default response
    else:
        return "I understand what you're saying. Taking things one step at a time often helps. Consider breaking down what you're dealing with into smaller, manageable parts. Would you like to share more details?"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)