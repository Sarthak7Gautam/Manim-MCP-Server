"""
1. YOUR CODE → LLM
   llm_with_tools.ainvoke(messages)
   "Create a bouncing ball animation"
        │
        ▼

2. LLM → YOUR CODE  (just a suggestion, nothing executed yet)
   AIMessage with tool_calls:
   {
     "name": "render_manim_code",
     "args": {"code": "...", "scene_name": "MyScene"}
   }
        │
        ▼

3. YOUR CODE → MANIM SERVER
   tools[0].ainvoke(tool_call["args"])
   Actually executes render_manim_code()
   Writes temp_scene.py
   Runs: manim -ql temp_scene.py
        │
        ▼

4. MANIM SERVER → YOUR CODE  (raw result)
   "Successfully created MyScene. Video saved in .../media/videos/"
        │
        ▼

5. YOUR CODE → LLM  (wrapped in ToolMessage)
   llm_with_tools.ainvoke(messages)
   "Here is the result of the tool, now format it nicely"
        │
        ▼

6. LLM → YOUR CODE  (final formatted reply)
   "I have created a simple bouncing ball animation for you!
    You can find the video at .../media/videos/"
```

The LLM is involved in **step 2 and step 6 only** — suggesting and formatting. Everything in between (steps 3, 4, 5) is just your Python code talking directly to the Manim server. The LLM never touches the actual animation generation."""
