Objective
The objective of Milestone 2 is to transition from a static user interface to a dynamic, AI-integrated application. 
This version leverages Large Language Models (LLMs) to process user physical metrics (Height, Weight, BMI) and fitness goals to generate professional, 
5-day tailored workout regimens in real-time.

🤖 Model Details
 * Model Name: Mistral-7B-Instruct-v0.2
 * Provider: Hugging Face Inference API
 * Library: huggingface_hub.InferenceClient
   
📝 Prompt Design Explanation
The application uses a Dual-Layer Prompting strategy to ensure high-quality outputs:
 * System Role: Explicitly defines the AI's persona as a "Certified Professional Fitness Trainer" to set the tone and authority of the response.
 * Dynamic Context: The build_prompt function injects real-time variables (Name, BMI, Gender, Equipment) into a template.
 * Safety Logic: Includes specific instructions to adjust intensity based on the calculated BMI Category and to avoid high-impact or unsafe exercises for beginners.
   
🛠️ Steps Performed
 * API Integration: Implemented model_api.py using the InferenceClient to handle secure communication with Hugging Face servers.
 * Business Logic: Created prompt_builder.py to handle the mathematical heavy lifting (BMI calculation) and string formatting.
 * Frontend Development: Built a multi-page Streamlit interface using st.sidebar for seamless navigation between the profile form, results, and AI generation.
 * State Management: Utilized st.session_state to ensure user data persists while switching between the "BMI Result" and "AI Workout Plan" pages.
 * Inference Testing: Validated model responses to ensure the max_tokens and temperature settings provide a balance between creative variety and structured technical accuracy.
   
🚀 Deployment
Hugging Face Space:(https://huggingface.co/spaces/kanakkk789/FitPlanAI2)

📊 Sample Generated Output
Name: purti
BMI: 29.08
Category: Overweight
Here’s a 5-day beginner-friendly, muscle-building (hypertrophy) workout plan for Purti, tailored for bodyweight training with progressive intensity to ensure safety and effectiveness. Since she has no equipment, the plan focuses on compound movements, resistance bands (if available), and household items for progressive overload.
Key Notes for Purti’s Plan:
✅ Goal: Hypertrophy (muscle growth) at a beginner level—emphasis on controlled movements, proper form, and progressive difficulty (not weight). ✅ BMI Adjustment: Overweight (29.08) – Lower impact, focus on joint safety, engage core for stability, and avoid extreme ranges of motion (e.g., deep squats, full ROM push-ups). ✅ Progression: Increase difficulty by slowing tempo, adding pulses, single-leg variations, or holding positions (e.g., push-up hold → push-up). ✅ Rest: 60–90 sec for hypertrophy (longer if needed for recovery). ✅ Warm-Up: 5–10 min of dynamic stretches (arm circles, leg swings, bodyweight squats, lunges, cat-cow) before each workout. ✅ Cool-Down: 5 min of static stretching (hamstrings, chest, shoulders, back) + deep breathing.

Day 1: Full-Body Strength (Beginner Focus)
Objective: Build foundational strength with controlled movements.

Bodyweight Squats (Legs: Quads, Glutes)

3 sets × 10–12 reps
Rest: 60 sec
Modification: Sit back into a chair for a partial squat if full ROM is uncomfortable.
Wall Push-Ups (Chest, Shoulders, Triceps)

3 sets × 10–12 reps
Rest: 60 sec
Progression: Move hands slightly closer to the wall or elevate feet on a low surface.
Glute Bridges (Glutes, Hamstrings, Lower Back)

3 sets × 12 reps (hold peak contraction for 2 sec)
Rest: 60 sec
Modification: Place a book under hips to reduce range of motion if needed.
Plank on Knees (Core: Abs, Obliques)

3 sets × 20–30 sec
Rest: 45 sec
Progression: Lift knees off the floor for a full plank (if possible


