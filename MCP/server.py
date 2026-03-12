from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo MCP server")

@mcp.tool()
def add_number(a:int, b:int)->int:
    "Add two numbers"
    return a+b

@mcp.tool()
def greet(name:str)->str:
    return f"Hello {name}"

if __name__=="__main__":
    mcp.run()