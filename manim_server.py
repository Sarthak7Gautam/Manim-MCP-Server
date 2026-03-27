import subprocess
from fastmcp import FastMCP
import os

mcp = FastMCP(name="Manim-MCP-Server")

Working_Directory = os.path.expanduser(
    r"C:\Users\dell\OneDrive\Desktop\Manim MCP Server"
)

os.makedirs(Working_Directory, exist_ok=True)


@mcp.tool()
def render_manim_code(code: str, scene_name: str = "ManimAnimation") -> str:
    """
    param code : The full manim python script code
    param scene_name : The name of the scene class to render
    Create a very simple and basic animation
    and a short animation
    """

    file_path = os.path.join(Working_Directory, "temp_scene.py")
    with open(file_path, "w") as f:
        f.write(code)

    result = subprocess.run(
        ["manim", "-ql", "--progress_bar", file_path, scene_name],
        cwd=Working_Directory,
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        return f"Successfully created the {scene_name}.Video saved in {Working_Directory}/media/videos/."
    else:
        return f"Error rendering:{result.stderr}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
